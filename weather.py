import requests


def get_weather(city):
    # variables to store the API key/token and the URL
    api_key = "bb488a390f508c273897a99e0e8f0f21"
    base_url = "https://api.openweathermap.org/data/2.5/weather?units=metric"

    # receive input from user and store the city name in the variable city
    city = city
    # complete URL address and store in complete url variable
    complete_url = base_url + "&q=" + city + "&appid=" + api_key
    # get method of requests model and return response object
    response = requests.get(complete_url)
    # json method of response object, convert json format data into python format data
    converted_response = response.json()
    # converted_response contains list of nested dictionaries
    # check the value of "cod" key is equal to "404", means city is found otherwise is not found
    if converted_response["cod"] != "404":
        # store the value of "main"
        # key in variable
        y = converted_response["main"]
        # store the value corresponding to the "temp" and "humidity"
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        # store the value of "weather"
        # key in variable z  your_weather = weather.get_weather()
        z = converted_response["weather"]
        # store the value corresponding to the "description" key at the 0th index of z
        weather_description = z[0]["description"]
        # store the weather icon
        weather_icon = z[0]["icon"]
        # print following values
        return ("Temperature (in celcius) for " + str(city) + " = " + str(current_temperature) +
                "\n humidity (in percentage) = " + str(current_humidity) + "\n description ="
                " " + str(weather_description) + "\n " + weather_icon)
    else:
        # return city not found if an unknown city / incorrect city is entered
        return "City not found!"