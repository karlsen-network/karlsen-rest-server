# encoding: utf-8

from pydantic import BaseModel
from starlette.responses import PlainTextResponse

from helper import get_kls_price, get_kls_market_data
from server import app


class PriceResponse(BaseModel):
    price: float = 0.025235


@app.get("/info/price", response_model=PriceResponse | str, tags=["Karlsen network info"])
async def get_price(stringOnly: bool = False):
    """
    Returns the current price for Karlsen in USD.
    """
    if stringOnly:
        return PlainTextResponse(content=str(await get_kls_price()))

    return {"price": await get_kls_price()}


@app.get("/info/market-data",
         tags=["Karlsen network info"],
         include_in_schema=False)
async def get_market_data():
    """
    Returns market data for karlsen.
    """
    return await get_kls_market_data()
