import logging
from telegram import Update
from telegram.ext import ContextTypes

# إعداد اللوق (سجل الأخطاء)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# =========================
# دالة فحص المفتاح (API KEY)
# =========================
def check_key(api_key: str) -> bool:
    """
    هنا تضع منطق التحقق من المفتاح
    حاليا مجرد مثال بسيط
    """
    if not api_key:
        return False

    # مثال: المفتاح لازم يكون طوله أكبر من 10
    if len(api_key) < 10:
        return False

    return True


# =========================
# أمر /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحبا بك!\n"
        "ارسل /help لمعرفة الأوامر."
    )


# =========================
# أمر /help
# =========================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 الأوامر المتاحة:\n"
        "/start - بدء البوت\n"
        "/checkkey <key> - فحص المفتاح"
    )


# =========================
# أمر فحص المفتاح
# =========================
async def checkkey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) == 0:
            await update.message.reply_text("❌ أرسل المفتاح بعد الأمر")
            return

        key = context.args[0]

        if check_key(key):
            await update.message.reply_text("✅ المفتاح صحيح")
        else:
            await update.message.reply_text("❌ المفتاح غير صالح")

    except Exception as e:
        logger.error(f"Error in checkkey: {e}")
        await notify_error(update, context, e)


# =========================
# إرسال الأخطاء إلى تيليجرام
# =========================
async def notify_error(update: Update, context: ContextTypes.DEFAULT_TYPE, error: Exception):
    error_message = f"⚠️ حدث خطأ:\n{str(error)}"

    try:
        await update.message.reply_text(error_message)
    except:
        pass

    # لو عندك ID أدمن تقدر ترسل له هنا
    admin_id = context.bot_data.get("admin_id")

    if admin_id:
        try:
            await context.bot.send_message(
                chat_id=admin_id,
                text=error_message
            )
        except Exception as e:
            logger.error(f"Failed to send error to admin: {e}")
