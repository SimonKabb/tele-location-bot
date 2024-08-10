# Импорт вашей модели
from text import TOKEN
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os
import django
from asgiref.sync import sync_to_async

# Установите переменную окружения DJANGO_SETTINGS_MODULE и настройте Django


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("Отправить геолокацию", request_location=True)],
        [KeyboardButton("Обзор")],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Пожалуйста, отправьте вашу геолокацию:", reply_markup=reply_markup)


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Получено сообщение с данными")  # Проверка вызова обработчика
    user_location = update.message.location
    if user_location:
        user_id = update.message.from_user.id
        latitude = user_location.latitude
        longitude = user_location.longitude

        # Сохранение данных в базу данных (асинхронно)
        await sync_to_async(UserLocation.objects.create)(user_id=user_id, latitude=latitude, longitude=longitude)

        print(
            f"Пользователь отправил геолокацию: широта={latitude}, долгота={longitude}")
        await update.message.reply_text(f"Спасибо! Ваша геолокация сохранена: широта={latitude}, долгота={longitude}")
    else:
        print("Геолокация не найдена в сообщении.")


def main():
    # Укажите токен вашего бота
    bot_token = TOKEN

    # Создайте приложение и добавьте обработчики
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.LOCATION, location))

    # Запуск опроса для получения сообщений и обновлений
    app.run_polling()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showmytrip.settings')
    django.setup()
    from showmap.models import UserLocation
    main()
