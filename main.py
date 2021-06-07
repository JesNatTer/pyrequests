import requests
from tkinter import *
import tkinter.font as tfont
from tkinter import messagebox

# creates window of program
root = Tk()
root.geometry('400x500')
root.config(bg='#222')
root.title('Weather App')
root.resizable(0, 0)

# creating different font sizes
font1 = tfont.Font(family='Helvetica', size=40)
font2 = tfont.Font(family='Helvetica', size=20)
font3 = tfont.Font(family='Helvetica', size=15)
font4 = tfont.Font(family='Helvetica', size=10)

#  label and entry for input of city
citylabel = Label(root, text="Enter A City:", font=font2, bg='#222', fg='white')
citylabel.place(x=130, y=15)
cityentry = Entry(root, width=15, bd=0, justify='center')
cityentry.place(x=140, y=60)

templ = Label(root, text='', font=font1, fg='#222', bg='#222')
templ.place(x=140, y=150)
tempminl = Label(root, text='', font=font4, fg='#222', bg='#222')
tempminl.place(x=135, y=200)
tempmaxl = Label(root, text='', font=font4, fg='#222', bg='#222')
tempmaxl.place(x=200, y=200)
cover = Label(root, text='', width=20, font=font3, fg='#222', bg='#222', justify='center')
cover.place(x=90, y=230)
cloud = Label(root, text='', font=font3, fg='#222', bg='#222')
cloud.place(x=125, y=290)
humidity = Label(root, text='', font=font3, fg='#222', bg='#222')
humidity.place(x=135, y=330)
wind = Label(root, text='', font=font3, fg='#222', bg='#222')
wind.place(x=99, y=370)


#  fetches and displays relevant weather data in labels
def getdata():
    city = cityentry.get()
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0bcce0200aa079df12eb18d5a972d541")
        data = response.json()
        temp = int(data['main']['temp'] - 273.15)
        templ.config(text=str(temp) + '°C', fg='white', bg='#222')
        tempmin = int(data['main']['temp_min'] - 273.15)
        tempminl.config(text='Min:'+str(tempmin)+'°C', fg='white', bg='#222')
        tempmax = int(data['main']['temp_max'] - 273.15)
        tempmaxl.config(text='Max: '+str(tempmax)+'°C', fg='white', bg='#222')
        cover.config(text=str(data['weather'][0]['main']),width=20, fg='white', bg='#222', justify='center')
        cloud.config(text='Cloud Cover: ' + str(data['clouds']['all']) + '%', fg='white', bg='#222')
        humidity.config(text='Humidity: ' + str(data['main']['humidity']) + '%', fg='white', bg='#222')
        wind.config(text='Wind Speed: ' + str(data['wind']['speed']) + ' km/h', fg='white', bg='#222')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a name of a city.")


#  button for function 'getdata'
button = Button(root, text='Enter', bd=0, relief='raised', fg='white', bg='#444', command=getdata)
button.place(x=172, y=90)


def clear():
    cityentry.delete(0, END)
    templ.config(text='')
    tempminl.config(text='')
    tempmaxl.config(text='')
    cover.config(text='')
    cloud.config(text='')
    humidity.config(text='')
    wind.config(text='')


clearbtn = Button(root, text='Clear', fg='white', bg='#222', command=clear)
clearbtn.place(x=180, y=450)

root.mainloop()
