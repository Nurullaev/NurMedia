import html

from aiogram import Router, types
from aiogram.filters import Command

router = Router()

START_TEXT = """👋 Привет, {name}!

Пришли ссылку на видео — я скачаю его и пришлю сюда вместе с аудиодорожкой в mp3.

📥 <b>Откуда качаю:</b> YouTube и Shorts, TikTok, Instagram Reels, X (Twitter), VK и VK Клипы, OK.ru, Rutube, Дзен, Yappy, Reddit, Pinterest, Vimeo, Dailymotion, клипы Twitch, Coub, Streamable.

🔓 Качаю только публичные видео.
📦 Если видео больше 50 МБ, пришлю одноразовую ссылку — она действует около 3 часов.
🙏 Не блокируй бота, иначе он не сможет прислать результат."""


@router.message(Command("start", "help"))
async def start(message: types.Message) -> None:
    name = html.escape(message.from_user.first_name) if message.from_user else "друг"
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text="📰 Канал с новостями", url="https://t.me/NurVPN")]]
    )
    await message.answer(START_TEXT.format(name=name), reply_markup=kb)
