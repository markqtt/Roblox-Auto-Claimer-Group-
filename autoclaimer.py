import asyncio
import os
from roblox_py import Client
cookie = os.environ['cookie']
client = Client(cookies=cookie)
async def main():
    auth_user = await client.get_auth_user()
    await auth_user.claim_group_owner(group_id_here)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
