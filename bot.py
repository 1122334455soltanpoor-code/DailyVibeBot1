import os
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from telegram import Bot
from telegram.constants import ChatPermissions


TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

IRAN_TZ = ZoneInfo("Asia/Tehran")


async def set_day_mode(bot):
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_photos=True,
        can_send_videos=False,
        can_send_audios=False,
        can_send_documents=False,
        can_send_voice_notes=False,
        can_send_video_notes=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
    )

    await bot.set_chat_permissions(
        chat_id=CHAT_ID,
        permissions=permissions,
        use_independent_chat_permissions=True,
    )

    print("DAY MODE: فقط عکس")


async def set_night_mode(bot):
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_photos=False,
        can_send_videos=False,
        can_send_audios=False,
        can_send_documents=False,
        can_send_voice_notes=False,
        can_send_video_notes=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
    )

    await bot.set_chat_permissions(
        chat_id=CHAT_ID,
        permissions=permissions,
        use_independent_chat_permissions=True,
    )

    print("NIGHT MODE: فقط متن")


async def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده")

    if not CHAT_ID:
        raise ValueError("CHAT_ID تنظیم نشده")

    bot = Bot(TOKEN)
    last_mode = None

    while True:
        now = datetime.now(IRAN_TZ)
        hour = now.hour

        # 07:00 تا 23:59 = عکس
        if 7 <= hour < 24:
            mode = "day"
        else:
            mode = "night"

        if mode != last_mode:
            if mode == "day":
                await set_day_mode(bot)
            else:
                await set_night_mode(bot)

            last_mode = mode

        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
