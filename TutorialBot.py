import logging
import os
from dotenv import load_dotenv

load_dotenv()


from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler,
)
from telegram.constants import ParseMode

logger = logging.getLogger(__name__)

# Store bot screaming status
screaming = False

# Pre-assign menu text
FIRST_MENU = "<b>Menu 1</b>\n\nA beautiful menu with a shiny inline button."
SECOND_MENU = "<b>Menu 2</b>\n\nA better menu with even more shiny inline buttons."

# Pre-assign button text
NEXT_BUTTON = "Next"
BACK_BUTTON = "Back"
TUTORIAL_BUTTON = "Tutorial"

# Build keyboards
FIRST_MENU_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton(NEXT_BUTTON, callback_data=NEXT_BUTTON)]]
)
SECOND_MENU_MARKUP = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(BACK_BUTTON, callback_data=BACK_BUTTON)],
        [
            InlineKeyboardButton(
                TUTORIAL_BUTTON, url="https://core.telegram.org/bots/api"
            )
        ],
    ]
)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This function would be added to the dispatcher as a handler for messages coming from the Bot API
    """

    # Print to console
    print(f"{update.message.from_user.first_name} wrote {update.message.text}")

    if screaming and update.message.text:
        await context.bot.send_message(
            update.message.chat_id,
            update.message.text.upper(),
            # To preserve the markdown, we attach entities (bold, italic...)
            entities=update.message.entities,
        )
    else:
        # This is equivalent to forwarding, without the sender's name
        await update.message.copy(update.message.chat_id)


async def scream(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This function handles the /scream command
    """

    global screaming
    screaming = True
    await update.message.reply_text("I will now scream your messages!")


async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This function handles /whisper command
    """

    global screaming
    screaming = False
    await update.message.reply_text("I will now whisper your messages!")


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    await context.bot.send_message(
        update.message.from_user.id,
        FIRST_MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=FIRST_MENU_MARKUP,
    )


async def button_tap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    query = update.callback_query
    await query.answer()  # Answer the callback query to remove the loading state

    data = query.data
    text = ""
    markup = None

    if data == NEXT_BUTTON:
        text = SECOND_MENU
        markup = SECOND_MENU_MARKUP
    elif data == BACK_BUTTON:
        text = FIRST_MENU
        markup = FIRST_MENU_MARKUP

    # Update message content with corresponding menu section
    await query.edit_message_text(
        text=text, parse_mode=ParseMode.HTML, reply_markup=markup
    )


async def post_init(application: Application) -> None:
    """Function to run after the bot is initialized"""
    print("Bot is starting...")


def main() -> None:
    # Configure logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    # Get token from environment variable or replace with your token
    token = os.getenv("TELEGRAM_BOT_TOKEN") or None

    if token is None:
        print("Please set your Telegram bot token!")
        return

    # Create Application
    application = Application.builder().token(token).post_init(post_init).build()

    # Register handlers
    application.add_handler(CommandHandler("scream", scream))
    application.add_handler(CommandHandler("whisper", whisper))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button_tap))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
