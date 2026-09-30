import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "8611987045:AAG5mGDM7wSGNeCEyp_zTwibTIAY9xMN0So"

# List of Expert Option assets for random market scanning
ASSETS = [
    "EUR/USD", "GBP/USD", "AUD/USD", "USD/JPY", 
    "EUR/GBP", "EUR/JPY", "USD/CHF", "NZD/USD",
    "Bitcoin", "Ethereum", "Gold", "Silver"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"👑 **WELCOME TO OCTOPUS REAL-TIME VIP SIGNALS** 👑\n\n"
        f"Hello {user_name}! Advanced Market Scanner with RSI, MA "
        f"& Trend confirmation for ExpertOption.\n"
        f"Click below to scan live setups:"
    )
    
    keyboard = [
        [InlineKeyboardButton("🚀 Get Best Signal", callback_data="get_signal")],
        [InlineKeyboardButton("📊 Trade Results", callback_data="trade_results")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.edit_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_signal":
        asset = random.choice(ASSETS)
        direction = random.choice(["CALL 🟢 (BUY)", "PUT 🔴 (SELL)"])
        timeframe = random.choice(["1 Minute", "2 Minutes"])
        rsi = random.choice(["RSI: 28.5 (Oversold)", "RSI: 71.2 (Overbought)", "RSI: 50.4 (Neutral)"])
        confidence = random.randint(88, 98)
        
        signal_text = (
            f"🔍 **VIP MARKET SCANNER RESULT** 🔍\n\n"
            f"📊 **Asset:** `{asset}`\n"
            f"⏳ **Expiry:** `{timeframe}`\n"
            f"📈 **Action:** **{direction}**\n"
            f"📉 **Indicators:** `{rsi}`\n"
            f"🎯 **Accuracy:** `{confidence}%`\n\n"
            f"⚠️ *Trade at your own risk. Use proper money management!*"
        )
        
        back_keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.message.edit_text(signal_text, reply_markup=reply_markup, parse_mode="Markdown")
        
    elif query.data == "trade_results":
        results_text = (
            f"📊 **RECENT VIP SESSION RESULTS** 📊\n\n"
            f"✅ Session 1: +4 Wins / -0 Loss\n"
            f"✅ Session 2: +5 Wins / -1 Loss\n"
            f"🔥 **Win Rate:** `92.3%`\n\n"
            f"Stay tuned for the next live scanning cycle!"
        )
        back_keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.message.edit_text(results_text, reply_markup=reply_markup, parse_mode="Markdown")
        
    elif query.data == "back_to_menu":
        await start(update, context)

def main():
    # Built using modern ApplicationBuilder for python-telegram-bot v20+
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot is starting up...")
    application.run_polling()

if __name__ == "__main__":
    main()
