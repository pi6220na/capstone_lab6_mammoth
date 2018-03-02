import folium
from folium import plugins
import csv

mammoth_map = folium.Map(location=[40, -120], zoom_start=3, tiles='Stamen Terrain')

lat_lng = []

#ith open('mammoth_data.csv', 'r') as mammoth_csv:
with open('test.txt', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__()
    print(firstline)

    for line in reader:

        #print(line)
        lat = line[3]
        lon = line[4]
        lat_lng.append([lat, lon])
        marker_text = '%s found in %s, %s. %s' % (line[0], line[6], line[5], line[7])
        if line[1]:
            marker_text += ' %s %s ' % (line[1], line[2])

        marker = folium.Marker([lat, lon], popup=marker_text)

        marker.add_to(mammoth_map)

mammoth_map.save('mammoth_map.html')

heatmap = folium.Map(location=[40, -120], zoom_start=3)
heatmap.add_children(plugins.HeatMap(lat_lng))
heatmap.save('mammoth_heatmap.html')


