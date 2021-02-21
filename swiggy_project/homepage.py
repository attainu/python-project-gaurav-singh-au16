
from tkinter import *
from constants import Constants
import secondpage





class Homepage:
    def home():
    
        Constants.home_screen = Frame(bg = "Orange")
        Constants.home_screen.place(x = 0, y = 0, width = 400, height = 500)

        backgroung_image = PhotoImage(file = r"assets\images\bg.png")
        Label(Constants.home_screen, image = backgroung_image).pack()

        order_online_button = Button(Constants.home_screen, text = "Order Online", font = ("rockwell", 13),command=secondpage.Dashboard.orderOnline)
        order_online_button.place(x = 140, y = 250)

        vendor_button = Button(Constants.home_screen, text = "For Vendor/Resturant", font = ("rockwell", 13),command=secondpage.Dashboard.vendor)
        vendor_button.place(x = 110, y = 300)

        creater = Label(Constants.home_screen, text = "Made By Gaurav Singh", font = "rockwell 10 bold", bg="red")
        creater.place(x = 245, y = 480)
       
       
        Constants.home_screen.mainloop()