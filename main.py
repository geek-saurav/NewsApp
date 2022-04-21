import tkinter as tk
from typing_extensions import Self
import requests
from PIL import Image,ImageTk

#creating a window for the Gui
Window = tk.Tk()
Window.geometry("1300x600")
Window.title("News App")
Window.config(bg='white')

#creating an icon for the app
ico = Image.open('C:/Users/Saurav/Pictures/Camera Roll/icons.png')
photo = ImageTk.PhotoImage(ico)
Window.wm_iconphoto(False, photo)

#creating a function for scraping news
def findNews():
    api = 'a9d5f53a3b8a49a4b95ce418c64633dd'
    url= 'https://newsapi.org/v2/top-headlines?country=in&apiKey='+api
    news = requests.get(url).json()
    
    articles = news["articles"]

    my_articles=[]
    my_news = ""
    
    for article in articles:
        my_articles.append(article['title'])

    for i in range(15):
        my_news = my_news +str(i+1)+" ."+ my_articles[i] + '\n'

    label.config(text=my_news)

#button
button = tk.Button(Window, font=24, text = "latest news", command = findNews, bg="#E9EFC0")
button.pack(pady = 20)

label = tk.Label(Window, font= 18 ,justify = "left", bg="white")
label.pack(pady=20)

#image of news
img = Image.open('C:/Users/Saurav/Pictures/Camera Roll/news.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

label1 = tk.Label(Window,image=img, bg='white')
label1.pack()

#main loop
findNews()
Window.mainloop()