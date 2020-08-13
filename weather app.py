import requests
class weather:
    def get(self):
        try:
            #gets data from openweathermap api
            #converting that info to json
            #accessing json files
            #printing the info here

            global city,api_address,mainweather,descriptio,wind,name
            name = input("enter your name: ")
            city = input("enter the city you want to know: ")
            api_address = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=0c42f7f6b53b244c78a418f4f181282a".format(city)
            json_data = requests.get(api_address).json()
            mainweather = json_data["weather"][0]["main"]
            descriptio = json_data["weather"][0]["description"]
            wind = json_data["wind"]["speed"]
            print("     ")
        except KeyError as wea:
            #most common error is adding a location which is invalid (only valid input from user is location)

            print("""
            ---------------------------------------------
            | invalid city name, please give a valid one |
            ---------------------------------------------
            """)

        else:
            print("""           hi {}, It is nice to see you. your selected location is {} and according to my observation I
                 can see {} ({}) there, wind speed is {} km/hr.""".format(name,city,mainweather,descriptio,wind))

b=weather()
b.get()

