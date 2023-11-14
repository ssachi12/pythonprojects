import folium
m=folium.Map(location=[14.001005720989902, 74.54051787704682], zoom_start=12)

folium.Marker([14.093984678737547, 74.48993896477188]
              ,popup="<h1>My favourite place</h1><img scr='murudeshwara.jpg' width=400px><p>best place for vacation</p>"
              ,tooltip='Murudeshwara temple',
              icon=folium.Icon(icon='heart', icon_color='red')).add_to(m)


Cicon=folium.features.CustomIcon('heart.png', icon_size=(50, 50))

folium.Marker([14.028233935772318, 74.49563686398979]
              ,popup="<h1>best sea walk</h1><img scr='beach.jpg' width=400px><p>best place for vacation</p>"
              ,tooltip='alvekodi sea walk',
              icon=Cicon).add_to(m)


folium.Circle(
    location=(14.063947221595999, 74.49611856416675)
    ,radius= 5000,
    popup="home town",
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m)


m.save('map.html')