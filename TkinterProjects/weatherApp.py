from tkinter import *
from PIL import ImageTk,Image
import json
import requests

root = Tk()
root.title("Weather App")
root.geometry("410x70")

def search():
    #requesting the api
    try :
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode= "+zipcode.get()+" &distance=25&API_KEY=A23507D6-97BA-4864-B7E8-D8306D415157")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color="#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color="#ff9900"
        elif category == "Unhealthy":
            weather_color="#ff0000"
        elif category == "Very Unhealthy":
            weather_color="#990066"
        elif category == "Hazardous":
            weather_color="#660000"

        root.configure(background=weather_color)
        mylabel = Label(root, text=city + " air quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        mylabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "api error"


zipcode = Entry(root)
zipcode.grid(row=0, column=0, sticky=W+E+N+S)

zip_btn = Button(root, text="lookup zipcode", command=search)
zip_btn.grid(row=0, column=1, sticky=W+E+N+S)




root.mainloop()