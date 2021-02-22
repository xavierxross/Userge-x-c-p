""" Battery Status """

# By @Krishna_Singhal moded by @r4v4n4

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import Message, userge
from userge.utils.exceptions import StopConversation


@userge.on_cmd(
    "b1",
    about={
        "header": "@rn5pbot gives battery information of my First Phone",
        "flags": {"No Flag"},
        "usage": "{tr}b1 [Reply to user]",
    },
)
async def buttery1_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get first phone Battery Status...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@rn5pbot"
    await message.edit("```Getting Battery information of First Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @rn5pbot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/battery".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    battery1 = "Battery"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(battery1):
                await message.edit(f"`{msg.text}`")



@userge.on_cmd(
    "b2",
    about={
        "header": "@rn5pbot gives information of my Second Phone",
        "flags": {"No Flag"},
        "usage": "{tr}b2 [Reply to user]",
    },
)
async def buttery2_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get Second Phone Battery Status...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@ravanaphonebot"
    await message.edit("```Getting Battery information of Second Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @ravanaphonebot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/battery".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    battery2 = "Battery"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(battery2):
                await message.edit(f"`{msg.text}`")
                
                
@userge.on_cmd(
    "v1",
    about={
        "header": "@rn5pbot gives volume information of my First Phone",
        "flags": {"No Flag"},
        "usage": "{tr}v1 [Reply to user]",
    },
)
async def volume1_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get First Phone Volume Status...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@rn5pbot"
    await message.edit("```Getting Volume information of First Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @rn5pbot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/volume".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    volume1 = "System"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(volume1):
                await message.edit(f"`{msg.text}`")



@userge.on_cmd(
    "v2",
    about={
        "header": "@ravanaphonebot gives volume information of my Second Phone",
        "flags": {"No Flag"},
        "usage": "{tr}v2 [Reply to user]",
    },
)
async def volume2_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to get Second Phone Volume Status...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@ravanaphonebot"
    await message.edit("```Getting Volume information of Second Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @ravanaphonebot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/volume".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    volume2 = "System"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(volume2):
                await message.edit(f"`{msg.text}`")
                
                
@userge.on_cmd(
    "c1",
    about={
        "header": "@rn5pbot cancels for my First Phone",
        "flags": {"No Flag"},
        "usage": "{tr}c1 [Reply to user]",
    },
)
async def c1_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to cancel...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@rn5pbot"
    await message.edit("```Cancelling information of First Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @rn5pbot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("Cancel".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    c1 = "OK"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(c1):
                await message.edit(f"`{msg.text}`")



@userge.on_cmd(
    "c2",
    about={
        "header": " cancels for my Second Phone",
        "flags": {"No Flag"},
        "usage": "{tr}c2 [Reply to user]",
    },
)
async def c2_(message: Message):
    """ Get User's Phone Status"""
    replied = message.reply_to_message
    if not replied:
        await message.err("```Reply to cancel...```", del_in=5)
        return
    user = replied.from_user.id
    chat = "@ravanaphonebot"
    await message.edit("```Cancelling information of Second Phone```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked @ravanaphonebot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("Cancel".format(user))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    c2 = "OK"
    username = "Username History"
    for msg in msgs:
        if "-u" in message.flags:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Username...```", del_in=5)
                return
            if msg.text.startswith(username):
                await message.edit(f"`{msg.text}`")
        else:
            if msg.text.startswith("No records found"):
                await message.edit("```User never changed his Name...```", del_in=5)
                return
            if msg.text.startswith(c2):
                await message.edit(f"`{msg.text}`")
