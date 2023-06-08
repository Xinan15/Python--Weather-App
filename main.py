import streamlit as st
import plotly.express as px
from backend import get_data

# here we import the express module of the plotly
# and rename it as px
# here is the front-end code of the app


# Here we add title, text input, slider, selectbox, and subheader widgets

st.title("Weather Forecast for the Next Days")

st.write("Enter the city name, and drag the days on the slider to see the weather forecast for the next few days.")

place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of the forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky Condition"))

# st.subheader(f"{option} for the next {days} days in {place}")

if place:

    try:

        st.subheader(f"{option} for the next {days} days in {place}")
        # if place exits as a string

        # get the data
        filtered_data = get_data(place, days)

        # create a temperature plot

        # create a line graph here
        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures"})
            st.plotly_chart(figure)

        # st.plotly_chart() is a method that responsible to create a graph
        # the method here gets a figure object as input
        # a figure object is from a plotting library such as Plotly or Bokeh
        # plotly is a data visualisation library
        if option == "Sky Condition":
            images={
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            Sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in Sky_conditions]
            st.image(image_paths, width=100)

    except KeyError:
        st.write("This place does not exit.")

