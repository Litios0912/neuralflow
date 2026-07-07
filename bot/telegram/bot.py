import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import httpx
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = os.getenv("API_URL", "http://backend:8000")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

user_sessions = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🤖 Chat IA", callback_data="agent_chat")],
        [InlineKeyboardButton("🕸️ Web Scraper", callback_data="agent_web_scraper")],
        [InlineKeyboardButton("✍️ Content Generator", callback_data="agent_content_generator")],
        [InlineKeyboardButton("📊 Data Analyzer", callback_data="agent_data_analyzer")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "⚡ *NeuralFlow Bot*\n\n"
        "Selecciona un agente para comenzar:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    agent_type = query.data.replace("agent_", "")
    user_sessions[query.from_user.id] = {"agent_type": agent_type}
    await query.edit_message_text(
        f"✅ Agente seleccionado: *{agent_type}*\n\n"
        "Envía tu consulta:",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id not in user_sessions:
        await update.message.reply_text("Primero selecciona un agente con /start")
        return

    session = user_sessions[user_id]
    await update.message.reply_text("⏳ Procesando...")

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"{API_URL}/agents/1/run",
                json={
                    "input": text,
                    "config": {"agent_type": session["agent_type"]}
                }
            )
            if resp.status_code == 200:
                data = resp.json()
                await update.message.reply_text(
                    f"*{data.get('agent_name', 'AI')}:*\n\n{data['output'][:4000]}",
                    parse_mode="Markdown"
                )
            else:
                await update.message.reply_text(f"❌ Error: {resp.text[:200]}")
    except Exception as e:
        await update.message.reply_text(f"❌ Connection error: {str(e)[:200]}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *NeuralFlow Bot*\n\n"
        "Comandos:\n"
        "/start - Iniciar y seleccionar agente\n"
        "/help - Mostrar esta ayuda\n"
        "/reset - Reiniciar sesión\n\n"
        "Selecciona un agente con /start y luego envíale consultas.",
        parse_mode="Markdown"
    )

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in user_sessions:
        del user_sessions[user_id]
    await update.message.reply_text("🔄 Sesión reiniciada. Usa /start para empezar de nuevo.")

def main():
    if not BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not set")
        return
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
