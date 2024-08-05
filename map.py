import folium

m = folium.Map(location=(60.178582, 29.969587), tiles="cartodb positron")
folium.Marker(
    location=[60.178582, 29.969587],
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)
m.save("index.html")
