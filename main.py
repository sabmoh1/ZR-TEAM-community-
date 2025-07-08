from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import requests
from datetime import datetime
import asyncio

BOT_TOKEN = "7694605774:AAFmghA-wropGxBMPWyBKBftxZNyIs82S7c"

# /acc command
async def acc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        wait_msg = await update.message.reply_text(
            "⏳ 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡... 🔄",
            reply_to_message_id=update.message.message_id,
        )
        await asyncio.sleep(3)
        await wait_msg.delete()

        region = context.args[0]
        uid = context.args[1]
        url = f"https://garenafreefireaccount.vercel.app/playerpersonalshow?uid={uid}&region={region}"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            acc = json_data["AccountInfo"]
            guild = json_data["GuildInfo"]
            social = json_data["socialinfo"]

            timestamp = int(acc.get("AccountCreateTime", "0"))
            created_at = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")

            reply_text = (
                "👤 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻\n\n"
                f"🆔 𝗨𝗜𝗗: <code>{guild.get('GuildOwner', 'N/A')}</code>\n"
                f"🔹 𝗡𝗮𝗺𝗲: <code>{acc.get('AccountName', 'N/A')}</code>\n"
                f"🏅 𝗟𝗲𝘃𝗲𝗹: <code>{acc.get('AccountLevel', 'N/A')}</code>\n"
                f"❤️ 𝗟𝗶𝗸𝗲𝘀: <code>{acc.get('AccountLikes', 'N/A')}</code>\n"
                f"🌍 𝗥𝗲𝗴𝗶𝗼𝗻: <code>{acc.get('AccountRegion', 'N/A')}</code>\n"
                f"📅 𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗔𝘁: <code>{created_at}</code>\n"
                f"🎖️ 𝗕𝗥 𝗥𝗮𝗻𝗸: <code>{acc.get('BrMaxRank', 'N/A')}</code>\n"
                f"🎯 𝗖𝗦 𝗥𝗮𝗻𝗸: <code>{acc.get('CsMaxRank', 'N/A')}</code>\n"
                f"👥 𝗚𝘂𝗶𝗹𝗱: <code>{guild.get('GuildName', 'None')}</code>\n"
                f"🔢 𝗠𝗲𝗺𝗯𝗲𝗿𝘀: <code>{guild.get('GuildMember', '0')}</code>\n"
                f"📝 𝗕𝗶𝗼: <code>{social.get('AccountSignature', 'N/A')}</code>"
            )
            await update.message.reply_text(
                reply_text,
                reply_to_message_id=update.message.message_id,
                parse_mode="HTML",
            )
        else:
            await update.message.reply_text(
                "❌ Failed to fetch account data.",
                reply_to_message_id=update.message.message_id,
            )
    except Exception:
        await update.message.reply_text(
            "⚠️ Use the command like this:\n/acc sg 12345678",
            reply_to_message_id=update.message.message_id,
        )

# /bnr command
async def bnr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = await update.message.reply_text(
            "⏳ 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚 𝗜𝗠𝗔𝗚𝗘... 🔄",
            reply_to_message_id=update.message.message_id,
        )
        await asyncio.sleep(3)
        await msg.delete()

        region = context.args[0]
        uid = context.args[1]
        url = f"https://aditya-banner-v11op.onrender.com/banner-image?uid={uid}&region={region}"
        await update.message.reply_photo(url, reply_to_message_id=update.message.message_id)
    except Exception:
        await update.message.reply_text(
            "⚠️ Use the command like this:\n/bnr sg 12345678",
            reply_to_message_id=update.message.message_id,
        )

# /fit command
async def fit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = await update.message.reply_text(
            "⏳ 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚 𝗜𝗠𝗔𝗚𝗘... 🔄",
            reply_to_message_id=update.message.message_id,
        )
        await asyncio.sleep(3)
        await msg.delete()

        region = context.args[0]
        uid = context.args[1]
        url = f"https://aditya-outfit-v11op.onrender.com/outfit-image?uid={uid}&region={region}"
        await update.message.reply_photo(url, reply_to_message_id=update.message.message_id)
    except Exception:
        await update.message.reply_text(
            "⚠️ Use the command like this:\n/fit sg 12345678",
            reply_to_message_id=update.message.message_id,
        )

# /ban command
async def ban_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        msg = await update.message.reply_text(
            "⏳ 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗕𝗔𝗡 𝗦𝗧𝗔𝗧𝗨𝗦... 🔄",
            reply_to_message_id=update.message.message_id,
        )
        await asyncio.sleep(3)
        await msg.delete()

        uid = context.args[0]
        url = f"https://api-check-ban.vercel.app/check_ban/{uid}"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            data = json_data["data"]

            is_banned = data.get("is_banned", 0)
            ban_status = "Banned" if is_banned == 1 else "Not Banned"

            reply_text = (
                "👤 𝗕𝗮𝗻 𝗖𝗵𝗲𝗰𝗸 𝗥𝗲𝘀𝘂𝗹𝘁\n\n"
                f"🔹 𝗡𝗮𝗺𝗲: <code>{data.get('nickname', 'N/A')}</code>\n"
                f"🌍 𝗥𝗲𝗴𝗶𝗼𝗻: <code>{data.get('region', 'N/A')}</code>\n"
                f"🆔 𝗨𝗜𝗗: <code>{data.get('id', 'N/A')}</code>\n"
                f"🚫 𝗕𝗮𝗻 𝗦𝘁𝗮𝘁𝘂𝘀: <code>{ban_status}</code>\n"
                "📌 𝗖𝗼𝗻𝘁𝗮𝗰𝘁: @RAZOR_ZR"
            )
            await update.message.reply_text(
                reply_text,
                reply_to_message_id=update.message.message_id,
                parse_mode="HTML",
            )
        else:
            await update.message.reply_text(
                "❌ Failed to fetch ban information.",
                reply_to_message_id=update.message.message_id,
            )
    except Exception:
        await update.message.reply_text(
            "⚠️ Use the command like this:\n/ban 12345678",
            reply_to_message_id=update.message.message_id,
        )


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("acc", acc_command))
    app.add_handler(CommandHandler("bnr", bnr_command))
    app.add_handler(CommandHandler("fit", fit_command))
    app.add_handler(CommandHandler("ban", ban_command))

    app.run_polling()
