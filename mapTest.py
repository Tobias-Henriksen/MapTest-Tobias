import pandas as pd
import folium as F
import csv
with open('LongBoi.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for line in data:
    print(line)

longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472
map = F.Map(location=(56.14646760709516, 10.134188410872792), zoom_start=12)

F.Marker((55.044840182700774, 159.0897375749511), popup='Binaur').add_to(map)
F.Marker((56.15565249964541, 10.18747412813329), popup='Binaur').add_to(map)

F.PolyLine(locations=[(55.044840182700774, 159.0897375749511), (56.15565249964541, 10.18747412813329)], color='blue').add_to(map)
map.show_in_browser()
map.save("Map.html")
input("wait for exit")