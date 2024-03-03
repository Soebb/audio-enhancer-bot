import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from process_audio import AudioProcessing

Bot = Client(
    "PersianTranscriberBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TXT = """
Hi {}, I'm Audio Enhancer Bot.

Send an audio to get started.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/soebb/'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )



@Bot.on_message(filters.private & filters.audio)
async def enhance(_, m):
    msg = await m.reply("Downloading..")
    await m.download("input.mp3")
    await msg.edit_text("Processing..")
    enhancer = AudioProcessing("input.mp3", "input", m.audio.file_name, "./")
    enhancer.run()
    await m.reply_document(m.audio.file_name + ".mp3")
    os.remove("input.mp3")


Bot.run()