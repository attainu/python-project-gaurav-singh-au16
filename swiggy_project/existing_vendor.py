
from priceupdate import PriceUpdate
from tkinter import *
from constants import Constants
import homepage
import secondpage
import priceupdate


class ExistingVendor:
    def existing():
        
        # add frame

        Constants.existing = Frame(bg = "orange")
        Constants.existing.place(x = 0, y = 0, width = 400, height = 500)

        backgroung_image = PhotoImage(file = r"assets\images\existing_vendor.png")
        Label(Constants.existing, image = backgroung_image).pack()

        # add details label

        heading = Label(Constants.existing, text = "Select Your Resturant", font = "times 15 bold")
        heading.place(x = 100, y = 20)

        # existing vendors

        main_course_button = Button(Constants.existing, text = "<<<Punjabi Tadka>>>", font = ("rockwell", 20), bg="yellow", command=priceupdate.PriceUpdate.maincours_update)
        main_course_button.place(x = 50, y = 100)

        paratha_button = Button(Constants.existing, text = "<<<Paratha King>>>", font = ("rockwell", 20), bg="yellow")
        paratha_button.place(x = 60, y = 155)

        chinese_button = Button(Constants.existing, text = "<<<Foody Corner>>>", font = ("rockwell", 20), bg="yellow")
        chinese_button.place(x = 50, y = 210)

        
        home_button = Button(Constants.existing, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        back_button = Button(Constants.existing, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command = secondpage.Dashboard.vendor)
        back_button.place(x = 10, y = 10)

        Constants.existing.mainloop()
        