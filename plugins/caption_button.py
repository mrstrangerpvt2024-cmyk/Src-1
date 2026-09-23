# ---------------------------------------------------
# File Name: caption_button.py
# Purpose: Reusable inline URL button for uploaded files
# Works with the project's Telethon-based upload handlers.
# ---------------------------------------------------

import os
from telethon import Button


# Set these in Railway Variables, or change the defaults below.
BUTTON_TEXT = os.getenv("CAPTION_BUTTON_TEXT", "🔗 Join Channel")
BUTTON_URL = os.getenv("CAPTION_BUTTON_URL", "https://t.me/your_channel")


def get_caption_buttons():
    """
    Returns the inline URL button(s) that should appear below
    uploaded media/file captions.

    Railway Variables:
      CAPTION_BUTTON_TEXT = button text
      CAPTION_BUTTON_URL  = Telegram channel/group/website URL
    """
    if not BUTTON_URL:
        return None

    return [
        [Button.url(BUTTON_TEXT, BUTTON_URL)]
    ]


def get_caption_button():
    """
    Convenience helper for handlers that expect a single row/list
    of Telethon buttons.
    """
    buttons = get_caption_buttons()
    return buttons if buttons else []
