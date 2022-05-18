import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime

now = datetime.datetime.now()

st.write(f"Date : {now.year}/{now.month}/{now.day} ")
st.write(f"Time : {now.hour}:{now.minute}:{now.second} ")

st.write(""" # UBC Bus Loop Queue Counter 
Check the number of people standing in queue in different location
and the estimated waiting time
""")

from PIL import Image
image = Image.open('bus-image.png')


bus_stop = st.sidebar.selectbox("Select Bus Stop Number", ( "Show Map" ," [4] Powell ", " [44] Downtown ", 
                     " [14] Hastings ", " [84] VCC-Clark Stn", " [9] Boundary ", 
                     " [258] West Vancouver ", " [33] 29th Avenue Stn ", " [258] West Vancouver ", 
                     " [25] Brentwood Stn ", " [41] Joyce Stn " , " [43] Joyce Stn ", 
                     " [49] Metrotown Stn ", " [68] Lower Mall ", " [70] Wesbrook Mall ",
                     " [480] Bridgeport Stn ", " [84] VCC-Clark Stn ", " [99] B-Line ", 
                     " [N17] Downtown "))

if bus_stop == "Show Map":
    st.write(f" # Map of buses from UBC Exchange" )
    st.image(image, caption='UBC Busloop Map')
else:
    st.write(f" # {bus_stop} " )

    df = pd.DataFrame(
        np.random.randint(20, size=(24,2)),
        columns = ['In Line', 'Not in Line']
    )

    st.write(f" Number of people waiting in line now : ",  df._get_value(now.hour, 'In Line'))
    st.write(f" Number of people not waiting in line now : ",  df._get_value(now.hour, 'Not in Line'))
    # print(now.hour)


    st.write(f" Number of people waiting in line last hour : ",  df._get_value(23, 'In Line'))

    st.write(f"Estimated Waiting time: ", df._get_value(23, 'In Line')/2 , "minutes")

    # st.write(f"Last 24 hrs data for  {bus_stop} bus stop")

    # print(df)

    # print("Queue count last hour  ", df._get_value(now.hour-1, 'In Line'))

    # print("Queue count now ", df._get_value(now.hour, 'In Line'))

    # st.bar_chart(df)

    st.line_chart(df)

import streamlit as st
import pandas as pd
import pydeck as pdk

from urllib.error import URLError

# @st.cache
# def from_data_file(filename):
#     # url = (
#     #     "http://raw.githubusercontent.com/streamlit/"
#     #     "example-data/master/hello/v1/%s" % filename)
    
#     # data = pd.read_json(url)

#     data = {'address': ['49', '99', '101'], 
#             'racks': [2, 5, 3], 
#             'spaces': [4, 5, 3],
#             'lon': [-123.2460, -123.2660, -123.2470],
#             'lat': [49.2606, 49.2604, 49.2606]}
#     print(data['lon'])
#     data['lon'] =  -123.2460
#     data['lat'] = 49.2606
#     return data

# try:
#     ALL_LAYERS = {
#         "Bus Stops": pdk.Layer(
#             "HexagonLayer",
#             data=from_data_file("bike_rental_stats.json"),
#             get_position=["lon", "lat"],
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             extruded=True,
#         ),
#     }

#     print(from_data_file("bike_rental_stats.json"))
    
#     st.sidebar.markdown('### Map Layers')
#     selected_layers = [
#         layer for layer_name, layer in ALL_LAYERS.items()
#         if st.sidebar.checkbox(layer_name, True)]
#     if selected_layers:
#         st.pydeck_chart(pdk.Deck(
#             map_style="mapbox://styles/mapbox/light-v9",
#             initial_view_state={"latitude": 49.2606,
#                                 "longitude": -123.2460, "zoom": 13, "pitch": 50},
#             layers=selected_layers,
#         ))
#     else:
#         st.error("Please choose at least one layer above.")
# except URLError as e:
#     st.error("""
#         **This demo requires internet access.**

#         Connection error: %s
#     """ % e.reason)