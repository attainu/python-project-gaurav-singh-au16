from tkinter import *
from constants import Constants
import fooditems
import homepage
import secondpage

class Resturants:
    def resturant():

        Constants.resturant = Frame(bg = "grey")
        Constants.resturant.place(x = 0, y = 0, width = 400, height = 500)

        heading = Label(Constants.resturant, text = "Trusted Partner", font = "times 25 bold")
        heading.place(x = 90, y = 20)

        main_course_button = Button(Constants.resturant, text = "<<<Punjabi Tadka>>>", font = ("rockwell", 20), bg="yellow", command = fooditems.Fooditems.maincourse)
        main_course_button.place(x = 50, y = 100)

        paratha_button = Button(Constants.resturant, text = "<<<Paratha King>>>", font = ("rockwell", 20), bg="yellow", command = fooditems.Fooditems.paratha)
        paratha_button.place(x = 60, y = 155)

        chinese_button = Button(Constants.resturant, text = "<<<Foody Corner>>>", font = ("rockwell", 20), bg="yellow", command = fooditems.Fooditems.chinese)
        chinese_button.place(x = 50, y = 210)

        back_button = Button(Constants.new_resturant, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command = secondpage.Dashboard.orderOnline)
        back_button.place(x = 10, y = 10)

        home_button = Button(Constants.resturant, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)


