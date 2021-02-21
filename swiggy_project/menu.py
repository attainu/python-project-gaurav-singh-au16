from tkinter import *
from constants import Constants
import fooditems
import homepage
import secondpage



class Menu:

    def food():
        Constants.food_screen = Frame(bg = "pink")
        Constants.food_screen.place(x = 0, y = 0, width = 400, height = 500)

        heading = Label(Constants.food_screen, text = "MENU", font = "times 25 bold")
        heading.place(x = 140, y = 20)

        backgroung_image = PhotoImage(file = r"assets\images\menu.png")
        Label(Constants.food_screen, image = backgroung_image).pack()

        main_course_button = Button(Constants.food_screen, text = ">>>Main Course<<<", font = ("rockwell", 20), command = fooditems.Fooditems.maincourse)
        main_course_button.place(x = 60, y = 100)

        paratha_button = Button(Constants.food_screen, text = ">>>Paratha<<<", font = ("rockwell", 20), command = fooditems.Fooditems.paratha)
        paratha_button.place(x = 90, y = 155)

        chinese_button = Button(Constants.food_screen, text = ">>>Chinese<<<", font = ("rockwell", 20), command = fooditems.Fooditems.chinese)
        chinese_button.place(x = 85, y = 210)

        

        back_button = Button(Constants.food_screen, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command = secondpage.Dashboard.orderOnline)
        back_button.place(x = 10, y = 10)

        home_button = Button(Constants.food_screen, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        Constants.food_screen.mainloop()