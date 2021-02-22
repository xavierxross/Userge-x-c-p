import asyncio
import random
from userge import Message, userge
@userge.on_cmd(
    "fbun",
    about={
        "header": "fbun user",
        "usage": "{tr}reply to fbun a user",
    },
)
async def detail_hi(message: Message):
  await message.edit(f"{(await userge.get_users(message.reply_to_message.from_user.id)).first_name} has been fbunned from: \n**1. Direct Message** : **Yes**\n**2. Public Group :** {random.choice(range(0,99))} Groups\n**3. Public Channel** : {random.choice(range(0,99))} Channels\n**4. Private Group :** {random.choice(range(0,99))} Groups\n**5. Private Channel :** {random.choice(range(0,99))} Channels")
