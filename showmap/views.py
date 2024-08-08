from django.shortcuts import render
import folium


def index(request):
    template = 'showmap/index.html'
    usermap = folium.Map(location=(60.178582, 29.969587),
                         tiles="cartodb positron")
    folium.Marker(
        location=[60.178582, 29.969587],
        tooltip="Click me!",
        popup="Mt. Hood Meadows",
        icon=folium.Icon(icon="cloud"),
    ).add_to(usermap)
    usermap = usermap._repr_html_()
    context = {
        'usermap': usermap}
    return render(request, template, context)
