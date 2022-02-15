
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• Iam A Bot Project by MwK MusicS\n• I Can Manage Group VC's\n\n• Hit /help to know about available commands.</b>"
HELP = """
🎧 <b><>𝐼 𝐶𝑎𝑛 𝑃𝑙𝑎𝑦 𝑀𝑢𝑠𝑖𝑐,𝑌𝑇 𝐿𝑖𝑣𝑒𝑠 𝑂𝑛 𝑉𝑜𝑖𝑐𝑒 𝐶ℎ𝑎𝑡🤪</b>

🎶 **Common Commands**:
• `/current`  __Show current playing song__
• `/help` __Show help for commands__
• `/mwk` __Shows the playlist__
• `/stickerid` __To Get Id Of Replied Sticker__

🎶 **Admin Commands**:
• `/play`  __Reply to an audio file or YouTube link to play it or use /p <song name>__
• `/dplay` __Play music from Deezer, Use /d <song name>__
• `/skip [n]` __...Skip current or n where n >= 2__
• `/join`  __Join voice chat__
• `/leave`  __Leave current voice chat__
• `/mwk`  __Check which VC is joined__
• `/stop`  __Stop playing__
• `/radio` __Start Radio__
• `/stopradio` __Stops Radio Stream__
• `/replay`  __Play from the beginning__
• `/clear`  __Remove unused RAW PCM files__
• `/pause` __Pause playing__
• `/resume` __Resume playing__
• `/mute`  __Mute in VC__
• `/unmute`  __Unmute in VC__
• `/update` __Update Current Settings n Restarts the Bot__


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("❔ How To Use Me ❔", callback_data="help"),
                ],[
                InlineKeyboardButton('👨‍💻𝕯𝖊𝖛', url='https://t.me/Joseph_Alex_TG'),
                InlineKeyboardButton('💬𝚂𝚞𝚙𝚙𝚘𝚛𝚝', url='https://t.me/TGOpensource'
            ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
            [
                InlineKeyboardButton('👨‍💻𝕯𝖊𝖛', url='https://t.me/Joseph_Alex_TG'),
                InlineKeyboardButton('💬𝚂𝚞𝚙𝚙𝚘𝚛𝚝', url='https://t.me/TGOpensource')
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
