import asyncio

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import userge, Message


@userge.on_cmd("qwote", about={
    'header': "Quote a message",
    'usage': "{tr}quote [text or reply to msg]"})
async def quotecmd(message: Message):
    """quotecmd"""
    chat = '@es3n1n_bot'
    args = message.input_str
    replied = message.reply_to_message
    async with userge.conversation(chat) as conv:
        try:
            if replied and not args:
                text = await conv.forward_message(replied)
            else:
                if not args:
                    await message.err("```input not found!```", del_in=5)
                    return
                text = await conv.send_message(args)
        except YouBlockedUser:
            await message.edit('first **unblock** @es3n1n_bot')
            return
        await message.edit("```Wait Plox ...```")
        await userge.send_message(chat, "/quote", reply_to_message_id=text.message_id)
        await conv.get_response(mark_read=True)
        await conv.get_response(mark_read=True)
        await conv.get_response(mark_read=True)
        await conv.get_response(mark_read=True)
        await conv.get_response(mark_read=True)
        await conv.get_response(mark_read=True)
        quote = await conv.get_response(mark_read=True)
        message_id = replied.message_id if replied else None
        sticker = await userge.get_messages(chat, quote.message_id)
        await userge.send_sticker(message.chat.id, sticker.sticker.file_id, file_ref=sticker.sticker.file_ref, reply_to_message_id=message_id)
        await message.delete()
