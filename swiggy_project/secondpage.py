
from tkinter import * 
from constants import Constants
from menu import *
from resturants import Resturants

from existing_vendor import ExistingVendor
import homepage

class Dashboard:
    
   
    def orderOnline():

        Constants.order_online_screen = Frame(bg = "pink")
        Constants.order_online_screen.place(x = 0, y = 0, width = 400, height = 500)

        backgroung_image = PhotoImage(file = r"assets\images\online_order_image.png")
        Label(Constants.order_online_screen, image = backgroung_image).pack()

        order_by_menu = Button(Constants.order_online_screen, text = "Order By Menu", font = ("rockwell", 13), command = Menu.food)
        order_by_menu.place(x = 130, y = 250)

        order_by_resturant = Button(Constants.order_online_screen, text = "Order By Resturants", font = ("rockwell", 13), command = Resturants.resturant)
        order_by_resturant.place(x = 110, y = 300)

        home_button = Button(Constants.order_online_screen, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        Constants.order_online_screen .mainloop()

    
    def vendor():
    
        Constants.vendor_screen = Frame(bg = "Orange")
        Constants.vendor_screen.place(x = 0, y = 0, width = 400, height = 500)

        backgroung_image = PhotoImage(file = r"assets\images\vendor.png")
        Label(Constants.vendor_screen, image = backgroung_image).pack()

        
        existing_vendor_button = Button(Constants.vendor_screen, text = "Choose Your Resturant", font = ("rockwell", 13), command = ExistingVendor.existing)
        existing_vendor_button.place(x = 90, y = 200)
        
        home_button = Button(Constants.vendor_screen, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)
        
        Constants.vendor_screen.mainloop()
    