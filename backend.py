import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]
def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    # nr_values : the number of the values
    filtered_data = filtered_data[:nr_values]
    # from 0 to the number of the values

    # ("Select data to view", ("Temperature", "Sky"))
    # if option == "Temperature":
    #         filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    #
    # if option == "Sky":
    #         filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="London", forecast_days=3))

