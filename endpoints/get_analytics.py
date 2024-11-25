# encoding: utf-8
from dbsession import async_session
from endpoints.get_circulating_supply import get_circulating_coins
from fastapi import HTTPException
from models.Balance import Balance
from pydantic import BaseModel, parse_obj_as
from server import app
from sqlalchemy import func, select, and_
from typing import List


class Balances(BaseModel):
    address: str
    amount: float
    percent: float


class TopResponse(BaseModel):
    from_supply_total: float
    from_supply_percent: float
    top_addresses: List[Balances] | None


class DistributionResponse(BaseModel):
    from_supply_total: float
    from_supply_percent: float
    from_addresses_total: int
    from_addresses_percent: float


class TotalResponse(BaseModel):
    total_addresses: int


@app.get("/analytics/addresses/top", response_model=TopResponse | str, tags=["Karlsen analytics"])
async def get_top_addresses(limit: int = 100,
                            offset: int = 0):
    """
    Returns information about the top $KLS wallet holders. The 'offset' parameter will skip the
    specified number of positions before starting to return a list of entries, which is then
    constrained by the 'limit' parameter.
    """
    if limit > 10000:
        raise HTTPException(422, "Top addresses list is limited to 10000 entries in a single batch")

    async with async_session() as s:
        amount_list = (await s.execute(select(Balance)
                                       .order_by(Balance.amount.desc()).limit(limit).offset(offset))).scalars().all()

    circulating = float(await get_circulating_coins())
    from_supply_total = 0
    rich_list = []
    if amount_list:
        for amount in amount_list:
            amount.amount = float(amount.amount / 100000000)
            from_supply_total = from_supply_total + amount.amount
            circulating_percent = amount.amount / circulating * 100

            rich_list.append({
                "address": amount.address,
                "amount": round(amount.amount, 8),
                "percent": round(circulating_percent, 3)
            })

    from_supply_percent = from_supply_total / circulating * 100

    return {
        "from_supply_total": round(from_supply_total, 8),
        "from_supply_percent": round(from_supply_percent, 2),
        "top_addresses": rich_list
    }


@app.get("/analytics/addresses/distribution", response_model=DistributionResponse | str, tags=["Karlsen analytics"])
async def get_coin_distribution(min_amount: int = 0,
                                max_amount: int = -1):
    """
    Returns amount of Karlsen addresses and total amount of $KLS between the given minimum and maximum
    amount of $KLS. A negative value for the 'max_amount' parameter indicates no limit.
    """
    async with async_session() as s:
        if max_amount < 0:
            total = (await s.execute(select(func.count())
                                     .filter(Balance.amount >= min_amount * 100000000))).scalar()
            amount = (await s.execute(select(func.sum(Balance.amount))
                                      .filter(Balance.amount >= min_amount * 100000000))).scalar()
        else:
            total = (await s.execute(select(func.count())
                                     .filter(and_(Balance.amount >= min_amount * 100000000, Balance.amount <= max_amount * 100000000)))).scalar()
            amount = (await s.execute(select(func.sum(Balance.amount))
                                      .filter(and_(Balance.amount >= min_amount * 100000000, Balance.amount <= max_amount * 100000000)))).scalar()

    if total == 0 and amount == None:
        return {
            "from_supply_total": 0,
            "from_supply_percent": 0,
            "from_addresses_total": 0,
            "from_addresses_percent": 0
        }
    else:
        amount = float(amount / 100000000)
        amount_percent = amount / float(await get_circulating_coins()) * 100
        total_percent = await get_all_addresses()
        total_percent = total / float(total_percent['total_addresses']) * 100

        return {
            "from_supply_total": round(amount, 8),
            "from_supply_percent": round(amount_percent, 2),
            "from_addresses_total": total,
            "from_addresses_percent": round(total_percent, 2)
        }


@app.get("/analytics/addresses/total", response_model=TotalResponse | str, tags=["Karlsen analytics"])
async def get_all_addresses():
    """
    Returns information about total amount of known $KLS addresses in the network.
    """
    async with async_session() as s:
        total = (await s.execute(select(func.count(Balance.id)))).scalar()

    return {
        "total_addresses": total
    }

@app.get("/analytics/addresses/range", response_model=List[Balances] | str, tags=["Karlsen analytics"])
async def get_addresses_in_range(min_amount: int = 0, max_amount: int = -1):
    """
    Returns a list of addresses within the specified balance range.
    The 'min_amount' and 'max_amount' parameters define the range of balances to include.
    """
    async with async_session() as s:
        if max_amount < 0:
            address_list = (await s.execute(select(Balance)
                                            .filter(Balance.amount >= min_amount * 100000000)
                                            .order_by(Balance.amount.desc()))).scalars().all()
        else:
            address_list = (await s.execute(select(Balance)
                                            .filter(and_(
                                                Balance.amount >= min_amount * 100000000,
                                                Balance.amount <= max_amount * 100000000))
                                            .order_by(Balance.amount.desc()))).scalars().all()

    if not address_list:
        return "No addresses found within the specified range."

    circulating = float(await get_circulating_coins())
    response = []
    for entry in address_list:
        entry.amount = float(entry.amount / 100000000)
        circulating_percent = entry.amount / circulating * 100

        response.append({
            "address": entry.address,
            "amount": round(entry.amount, 8),
            "percent": round(circulating_percent, 3)
        })

    return response
