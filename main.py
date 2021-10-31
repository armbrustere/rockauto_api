import requests
import asyncio
from rockauto import *

import json


async def main():
    loop = asyncio.get_event_loop()
    make = "dodge"
    makeReturn = loop.run_in_executor(None, get_makes)
    await makeReturn
    #print(response1)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


#
# for model in get_models():
#
#
#
#
# task =
# returned_years = get_years(make)
# print(returned_years)
