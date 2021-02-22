from userge import Message, userge
import asyncio
@userge.on_cmd(
    "chotam",
    about={
        "header": "chotam",
        "usage": "reply to media {tr}chotam caption",
    },
)
async def attachments(message: Message):
  input_str = message.input_str
  await message.client.forward_messages('@chotamreaderbot', message.chat.id, message_ids=message.reply_to_message.message_id, as_copy=True)
  await (await userge.get_history('@chotamreaderbot', limit=1))[0].reply(input_str)
  await asyncio.sleep(5)
  await (await userge.get_history('@chotamreaderbot', limit=1))[0].forward(message.chat.id, as_copy=True)
