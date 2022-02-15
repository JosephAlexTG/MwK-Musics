
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji
from utils import mp
from config import Config
playlist=Config.playlist

HELP = """

🎧 <b>𝐼 𝐶𝑎𝑛 𝑃𝑙𝑎𝑦 𝑀𝑢𝑠𝑖𝑐,𝑌𝑇 𝐿𝑖𝑣𝑒𝑠 𝑂𝑛 𝑉𝑜𝑖𝑐𝑒 𝐶ℎ𝑎𝑡🤪</b>

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


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "rp":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"😖𝑁𝑜𝑡ℎ𝑖𝑛𝑔 𝑂𝑛 𝑄𝑢𝑒 𝑆𝑒𝑟"
        else:
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Replay", callback_data="rp"),
                            InlineKeyboardButton("Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("Skip", callback_data="sk"),
                            InlineKeyboardButton("Report Bug", url="subinps_bot")
                        ]
                    ]
                )
            )

    elif query.data == "ps":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Replay", callback_data="replace"),
                            InlineKeyboardButton("Resume", callback_data="resume")
                        ],[
                            InlineKeyboardButton("Skip", callback_data="skip"),
                            InlineKeyboardButton("Updates", url='t.me/mwkBoTs')
                        ],
                    ]
                )
            )

    
    elif query.data == "rs":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Replay", callback_data="rp"),
                            InlineKeyboardButton("Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("Skip", callback_data="sk"),
                            InlineKeyboardButton("Support", url="https://t.me/redbullfed") 
                        ],
                    ]
                )
            )

    elif query.data=="sk":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Replay", callback_data="rp"),
                            InlineKeyboardButton("Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("Skip", callback_data="sk"),
                            InlineKeyboardButton("Updates", url="t.me/subin_works")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        buttons = [
            [
                InlineKeyboardButton('👨‍💻𝕯𝖊𝖛', url='https://t.me/Joseph_Alex_TG'),
                InlineKeyboardButton('💬𝚂𝚞𝚙𝚙𝚘𝚛𝚝', url='https://t.me/TGOpensource')
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )
