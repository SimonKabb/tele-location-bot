from django.shortcuts import render
import folium
from showmap.models import UserLocation  # Импортируем вашу модель
from datetime import datetime


def format_datetime(dt):
    # Пример форматирования: '2024-08-10 15:30:00'
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def index(request):
    template = 'showmap/index.html'

    # Создайте карту
    usermap = folium.Map(tiles="cartodb positron")

    # Получите все объекты из модели UserLocation
    locations = UserLocation.objects.all()

    # Добавьте маркеры на карту для каждой локации
    for location in locations:
        # Форматируйте время для отображения
        formatted_time = format_datetime(location.timestamp)

        folium.Marker(
            location=[location.latitude, location.longitude],
            tooltip=formatted_time,
            popup=formatted_time,
            icon=folium.Icon(icon="cloud"),
        ).add_to(usermap)

    # Представление карты в HTML
    usermap = usermap._repr_html_()

    # Передача карты в контексте
    context = {
        'usermap': usermap
    }

    return render(request, template, context)
