from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_frh = (temp_kelvin - 273.15) * 9/5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city,country,temp_kelvin,temp_celsius,temp_frh,icon,weather)
        return final
    else:
        return None

def search():
    global img
    cityN = city_name.get()
    weather = get_weather(cityN)

    if weather:
        lable1['text'] = '{}, {}'.format(weather[0],weather[1])
        img["file"] = 'W_icons/{}.png'.format(weather[5])
        lable2['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[3],weather[4])
        lable3['text'] = weather[6]
    else:
        messagebox.showerror('Error',"cannot find city {}".format(cityN))

app = Tk()
app.title("My Weather App")
app.geometry('350x350')

bag = ImageTk.PhotoImage(Image.open("Weatherbg.jpg"))
My_c = Canvas(app,width = 350, height = 350,bg = 'blue')
My_c.pack(fill ='both', expand =True, anchor = "nw")
My_c.create_image( 0, 0, image = bag)


city_name = StringVar()
city_entry = Entry(app,textvariable = city_name)
city_entry_w = My_c.create_window(120,10,anchor = "nw",window = city_entry)

btn = Button(app,text = "Search",command = search, bg = '#4774d6')
btn_w = My_c.create_window(160,35,anchor = "nw",window = btn)

lable1 = Label(text = "",font = ("Bold",20), bg = '#4774d6')
lable1_w = My_c.create_window(125,75,anchor = "nw",window = lable1)
#a = My_c.create_text(180,75,text = ' ',font = ("Bold",20),fill = 'white')

img = PhotoImage(file= "")
Image = Label(app, image = img,bg = '#8dc9bd')
image_w = My_c.create_window(135,120,anchor = "nw",window = Image)

lable2 = Label(text = '', bg = '#4774d6')
lable2_w = My_c.create_window(145,230,anchor = "nw",window = lable2)
#b = My_c.create_text(185,125,text = ' ',fill = 'white')

lable3 = Label(text = '', bg = '#4774d6')
lable3_w = My_c.create_window(150,255,anchor = "nw",window = lable3)
#c = My_c.create_text(185,145,text = ' ',fill = 'white')


app.mainloop()