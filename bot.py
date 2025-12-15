from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN, WEBAPP_URL

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(
            text="💳 Оплатить 3 TON",
            web_app=types.WebAppInfo(
                url=f"{WEBAPP_URL}/index.html?amount=3"
            )
        )
    )
    await msg.answer(
        "🔐 Подписка\n\n💰 Цена: 3 TON\n⏳ Срок: 30 дней",
        reply_markup=kb
    )

if __name__ == "__main__":
    executor.start_polling(dp)
