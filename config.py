import os
from pathlib import Path

# ==========================
# Project Paths
# ==========================

ROOT_DIR = Path(__file__).resolve().parent

ASSETS_DIR = ROOT_DIR / "assets"
TEMP_DIR = ROOT_DIR / "temp"
OUTPUT_DIR = ROOT_DIR / "output"
LOGS_DIR = ROOT_DIR / "logs"
HISTORY_DIR = ROOT_DIR / "history"

# إنشاء المجلدات تلقائياً
for folder in [
    ASSETS_DIR,
    TEMP_DIR,
    OUTPUT_DIR,
    LOGS_DIR,
    HISTORY_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# ==========================
# API Keys
# ==========================

GEMINI_KEY = os.getenv("GEMINI_KEY", "")

FAL_KEY = os.getenv("FAL_KEY", "")

PIXVERSE_KEY = os.getenv("PIXVERSE_KEY", "")

FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN", "")

FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID", "")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# ==========================
# Video Settings
# ==========================

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

FPS = 30

SCENES_COUNT = 4

SCENE_DURATION = 5

FINAL_VIDEO_DURATION = SCENES_COUNT * SCENE_DURATION

# ==========================
# Facebook
# ==========================

POST_PER_DAY = 1

# ==========================
# History
# ==========================

HISTORY_FILE = HISTORY_DIR / "history.json"

# ==========================
# Logs
# ==========================

LOG_FILE = LOGS_DIR / "bot.log"

# ==========================
# Validation
# ==========================

REQUIRED_KEYS = {
    "GEMINI_KEY": GEMINI_KEY,
    "FAL_KEY": FAL_KEY,
    "PIXVERSE_KEY": PIXVERSE_KEY,
    "FACEBOOK_ACCESS_TOKEN": FACEBOOK_ACCESS_TOKEN,
    "FACEBOOK_PAGE_ID": FACEBOOK_PAGE_ID,
    "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN,
    "TELEGRAM_CHAT_ID": TELEGRAM_CHAT_ID,
}


def missing_keys():
    """
    ترجع قائمة بالمفاتيح غير الموجودة.
    """
    return [name for name, value in REQUIRED_KEYS.items() if not value]


def all_keys_exist():
    """
    هل جميع المفاتيح موجودة؟
    """
    return len(missing_keys()) == 0
