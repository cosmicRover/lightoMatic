from yeelight import discover_bulbs
from yeelight import Bulb
from BulbModel import *  # Our data model to hold bulb data
import asyncio  # to await for a response


# using asyncio creating a coroutine to get json from local bulb
# note that result is an array of objects, used to get info on multiple bulbs
async def discoverLocalBulbs() -> BulbModel:
    result = discover_bulbs()
    ip = result[0]["ip"]
    port = result[0]["port"]
    status = result[0]["capabilities"]["power"]

    bulbData: BulbModel = BulbModel(ip, port, status)

    return bulbData


# waits for previous func to finish and returns the ip address and status of the bulb
async def determineBulbStatusAndIp() -> BulbModel:
    loop = asyncio.get_event_loop()
    data: BulbModel = loop.run_until_complete(discoverLocalBulbs())
    loop.close()

    return data


# using the ip address and the status of the bulb, we turn the bulb on/off
# also waits for the previous func to finish first
def switchBulbStatus() -> None:
    loop = asyncio.get_event_loop()
    bulbStatusAndIp: BulbModel = loop.run_until_complete(discoverLocalBulbs())
    loop.close()

    bulb = Bulb(bulbStatusAndIp.ip)

    bulb.turn_off() if bulbStatusAndIp.status == "on" else bulb.turn_on()


if __name__ == '__main__':
    switchBulbStatus()
