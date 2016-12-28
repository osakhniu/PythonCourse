'''
Creator - Oksana Sakhniuk, 12/26/2016
The source code reads "Volcanoes-USA.txt" file, and creates a map with pointers
where volcanoes are located. The color of the marker is determined based on the
volcanoe's elevation value.

'''

import folium
import pandas

df=pandas.read_csv('Volcanoes-USA.txt')
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start=4, tiles='Stamen Terrain')


def color(elev):
    if elev in range(0,1000):
        col='green'
    elif elev in range(1000,3000):
        col='orange'
    else:
        col='red'
    return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'],df['NAME'], df['ELEV']):
    map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev)) ))

map.save(outfile='/Users/oksanasakhniuk/Documents/PythonCourse/WebMap/map1.html')
