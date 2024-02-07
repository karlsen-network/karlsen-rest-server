# encoding: utf-8

from pydantic import BaseModel

from endpoints import sql_db_only
from server import app, karlsend_client
from fastapi.responses import PlainTextResponse


class CoinSupplyResponse(BaseModel):
    circulatingSupply: str = "1000900697580640180"
    maxSupply: str = "2900000000000000000"


@app.get("/info/coinsupply", response_model=CoinSupplyResponse, tags=["Karlsen network info"])
async def get_coinsupply():
    """
    Get $KLS coin supply information
    """
    resp = await karlsend_client.request("getCoinSupplyRequest")
    return {
        "circulatingSupply": resp["getCoinSupplyResponse"]["circulatingSompi"],
        "totalSupply": resp["getCoinSupplyResponse"]["circulatingSompi"],
        "maxSupply": resp["getCoinSupplyResponse"]["maxSompi"]
    }

@app.get("/info/coinsupply/circulating", tags=["Karlsen network info"],
         response_class=PlainTextResponse)
async def get_circulating_coins(in_billion : bool = False):
    """
    Get circulating amount of $KLS token as numerical value
    """
    resp = await karlsend_client.request("getCoinSupplyRequest")
    coins = str(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 100000000)
    if in_billion:
        return str(round(float(coins) / 1000000000, 2))
    else:
        return coins


@app.get("/info/coinsupply/total", tags=["Karlsen network info"],
         response_class=PlainTextResponse)
async def get_total_coins():
    """
    Get total amount of $KLS token as numerical value
    """
    resp = await karlsend_client.request("getCoinSupplyRequest")
    return str(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 100000000)


@app.get("/info/coinsupply/max", tags=["Karlsen network info"],
         response_class=PlainTextResponse)
async def get_max_coins():
    """
    Get maximum amount of $KLS token as numerical value
    """
    resp = await karlsend_client.request("getCoinSupplyRequest")
    return str(float(resp["getCoinSupplyResponse"]["maxSompi"]) / 100000000)
