from tkinter import *
from constants import Constants
import homepage
import existing_vendor
import billing

class PriceUpdate:
    def maincours_update():
        Constants.maincours_update = Frame(bg = "orange")
        Constants.maincours_update.place(x = 0, y = 0, width = 400, height = 500)

        y_1 = IntVar()
        y_2 = IntVar()
        y_3 = IntVar()
        y_4 = IntVar()
        y_5 = IntVar()
        y_1.set(0)
        y_2.set(0)
        y_3.set(0)
        y_4.set(0)
        y_5.set(0)

        maincours_update = Frame(bg = "pink")
        Constants.maincours_update.place(x = 0, y = 0, width = 400, height = 500)

        sub_heading_1 = Label(Constants.maincours_update, text = "Items", font = "times 15 bold")
        sub_heading_1.place(x = 10, y = 70)

        sub_heading_2 = Label(Constants.maincours_update, text = "Price", font = "times 15 bold")
        sub_heading_2.place(x = 180, y = 70)

        sub_heading_3 = Label(Constants.maincours_update, text = "Update Price", font = "times 15 bold")
        sub_heading_3.place(x = 300, y = 70)

        back_button = Button(Constants.maincours_update, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command=existing_vendor.ExistingVendor.existing)
        back_button.place(x = 10, y = 10)

        home_button = Button(Constants.maincours_update, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        payment_button = Button(Constants.maincours_update, text = "Update Data", font = ("rockwell", 15),foreground = 'red',command=(lambda :Constants.updateData(add_cart_1.get(), add_cart_2.get(),add_cart_3.get(),add_cart_4.get(),add_cart_5.get())))
        payment_button.place(x = 140, y = 280)

        # Food Items List 1

        item_1 = Label(Constants.maincours_update, text = Constants.menu_1[0], font = "times 10 bold")
        item_1.place(x = 10, y = 100)

        price_1 = Label(Constants.maincours_update, text = Constants.menu_price_1[0], font = "times 10 bold")
        price_1.place(x = 180, y = 100)

        add_cart_1=Entry(Constants.maincours_update, font=("rockwell",13), textvariable=y_1)
        add_cart_1.place(x = 300,y = 100)

        item_2 = Label(Constants.maincours_update, text = Constants.menu_1[1], font = "times 10 bold")
        item_2.place(x = 10, y = 130)

        price_2 = Label(Constants.maincours_update, text = Constants.menu_price_1[1], font = "times 10 bold")
        price_2.place(x = 180, y = 130)

        add_cart_2=Entry(Constants.maincours_update, font=("rockwell",13), textvariable=y_2)
        add_cart_2.place(x = 300,y = 130)

        item_3 = Label(Constants.maincours_update, text = Constants.menu_1[2], font = "times 10 bold")
        item_3.place(x = 10, y = 160)

        price_3 = Label(Constants.maincours_update, text = Constants.menu_price_1[2], font = "times 10 bold")
        price_3.place(x = 180, y = 160)

        add_cart_3=Entry(Constants.maincours_update, font=("rockwell",13), textvariable=y_3)
        add_cart_3.place(x = 300,y = 160)

        item_4 = Label(Constants.maincours_update, text = Constants.menu_1[3], font = "times 10 bold")
        item_4.place(x = 10, y = 190)

        price_4 = Label(Constants.maincours_update, text = Constants.menu_price_1[3], font = "times 10 bold")
        price_4.place(x = 180, y = 190)

        add_cart_4=Entry(Constants.maincours_update, font=("rockwell",13), textvariable=y_4)
        add_cart_4.place(x = 300,y = 190)

        item_5 = Label(Constants.maincours_update, text = Constants.menu_1[4], font = "times 10 bold")
        item_5.place(x = 10, y = 220)

        price_5 = Label(Constants.maincours_update, text = Constants.menu_price_1[4], font = "times 10 bold")
        price_5.place(x = 180, y = 220)

        add_cart_5=Entry(Constants.maincours_update, font=("rockwell",13), textvariable=y_5)
        add_cart_5.place(x = 300,y = 220)

    def paratha():

        y_1 = IntVar()
        y_2 = IntVar()
        y_3 = IntVar()
        y_4 = IntVar()
        y_5 = IntVar()
        y_1.set(0)
        y_2.set(0)
        y_3.set(0)
        y_4.set(0)
        y_5.set(0)

        Constants.paratha = Frame(bg = "pink")
        Constants.paratha.place(x = 0, y = 0, width = 400, height = 500)

        sub_heading_1 = Label(Constants.paratha, text = "Items", font = "times 15 bold")
        sub_heading_1.place(x = 10, y = 70)

        sub_heading_2 = Label(Constants.paratha, text = "Price", font = "times 15 bold")
        sub_heading_2.place(x = 180, y = 70)

        sub_heading_3 = Label(Constants.paratha, text = "Add Cart", font = "times 15 bold")
        sub_heading_3.place(x = 300, y = 70)

        back_button = Button(Constants.paratha, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command = menu.Menu.food)
        back_button.place(x = 10, y = 10)

        home_button = Button(Constants.paratha, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        payment_button = Button(Constants.paratha, text = "Payment", font = ("rockwell", 15),foreground = 'red',command=(lambda :billing.Billing.calculateParatha (add_cart_1.get(), add_cart_2.get(),add_cart_3.get(),add_cart_4.get(),add_cart_5.get())))
        payment_button.place(x = 140, y = 280)

        # Food Items List 2

        item_1 = Label(Constants.paratha, text = Constants.menu_2[0], font = "times 10 bold")
        item_1.place(x = 10, y = 100)

        price_1 = Label(Constants.paratha, text = Constants.menu_price_2[0], font = "times 10 bold")
        price_1.place(x = 180, y = 100)

        add_cart_1=Entry(Constants.paratha, font=("rockwell",13), textvariable=y_1)
        add_cart_1.place(x = 300,y = 100)

        item_2 = Label(Constants.paratha, text = Constants.menu_2[1], font = "times 10 bold")
        item_2.place(x = 10, y = 130)

        price_2 = Label(Constants.paratha, text = Constants.menu_price_2[1], font = "times 10 bold")
        price_2.place(x = 180, y = 130)

        add_cart_2=Entry(Constants.paratha, font=("rockwell",13),textvariable=y_2)
        add_cart_2.place(x = 300,y = 130)

        item_3 = Label(Constants.paratha, text = Constants.menu_2[2], font = "times 10 bold")
        item_3.place(x = 10, y = 160)

        price_3 = Label(Constants.paratha, text = Constants.menu_price_2[2], font = "times 10 bold")
        price_3.place(x = 180, y = 160)

        add_cart_3=Entry(Constants.paratha, font=("rockwell",13), textvariable=y_3)
        add_cart_3.place(x = 300,y = 160)

        item_4 = Label(Constants.paratha, text = Constants.menu_2[3], font = "times 10 bold")
        item_4.place(x = 10, y = 190)

        price_4 = Label(Constants.paratha, text = Constants.menu_price_2[3], font = "times 10 bold")
        price_4.place(x = 180, y = 190)

        add_cart_4=Entry(Constants.paratha, font=("rockwell",13), textvariable=y_4)
        add_cart_4.place(x = 300,y = 190)

        item_5 = Label(Constants.paratha, text = Constants.menu_2[4], font = "times 10 bold")
        item_5.place(x = 10, y = 220)

        price_5 = Label(Constants.paratha, text = Constants.menu_price_2[4], font = "times 10 bold")
        price_5.place(x = 180, y = 220)

        add_cart_5=Entry(Constants.paratha, font=("rockwell",13), textvariable=y_5)
        add_cart_5.place(x = 300,y = 220)

    def chinese():

        y_1 = IntVar()
        y_2 = IntVar()
        y_3 = IntVar()
        y_4 = IntVar()
        y_5 = IntVar()
        y_1.set(0)
        y_2.set(0)
        y_3.set(0)
        y_4.set(0)
        y_5.set(0)

        Constants.chinese = Frame(bg = "pink")
        Constants.chinese.place(x = 0, y = 0, width = 400, height = 500)

        sub_heading_1 = Label(Constants.chinese, text = "Items", font = "times 15 bold")
        sub_heading_1.place(x = 10, y = 70)

        sub_heading_2 = Label(Constants.chinese, text = "Price", font = "times 15 bold")
        sub_heading_2.place(x = 180, y = 70)

        sub_heading_3 = Label(Constants.chinese, text = "Add Cart", font = "times 15 bold")
        sub_heading_3.place(x = 300, y = 70)

        back_button = Button(Constants.chinese, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command = menu.Menu.food)
        back_button.place(x = 10, y = 10)

        home_button = Button(Constants.chinese, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        payment_button = Button(Constants.chinese, text = "Payment", font = ("rockwell", 15),foreground = 'red',command=(lambda :billing.Billing.calculateChinese (add_cart_1.get(), add_cart_2.get(),add_cart_3.get(),add_cart_4.get(),add_cart_5.get())))
        payment_button.place(x = 140, y = 280)

        # Food Items List 3

        item_1 = Label(Constants.chinese, text = Constants.menu_3[0], font = "times 10 bold")
        item_1.place(x = 10, y = 100)

        price_1 = Label(Constants.chinese, text = Constants.menu_price_3[0], font = "times 10 bold")
        price_1.place(x = 180, y = 100)

        add_cart_1=Entry(Constants.chinese, font=("rockwell",13),textvariable=y_1)
        add_cart_1.place(x = 300,y = 100)

        item_2 = Label(Constants.chinese, text = Constants.menu_3[1], font = "times 10 bold")
        item_2.place(x = 10, y = 130)

        price_2 = Label(Constants.chinese, text = Constants.menu_price_3[1], font = "times 10 bold")
        price_2.place(x = 180, y = 130)

        add_cart_2=Entry(Constants.chinese, font=("rockwell",13),textvariable=y_2)
        add_cart_2.place(x = 300,y = 130)

        item_3 = Label(Constants.chinese, text = Constants.menu_3[2], font = "times 10 bold")
        item_3.place(x = 10, y = 160)

        price_3 = Label(Constants.chinese, text = Constants.menu_price_3[2], font = "times 10 bold")
        price_3.place(x = 180, y = 160)

        add_cart_3=Entry(Constants.chinese, font=("rockwell",13),textvariable=y_3)
        add_cart_3.place(x = 300,y = 160)

        item_4 = Label(Constants.chinese, text = Constants.menu_3[3], font = "times 10 bold")
        item_4.place(x = 10, y = 190)

        price_4 = Label(Constants.chinese, text = Constants.menu_price_3[3], font = "times 10 bold")
        price_4.place(x = 180, y = 190)

        add_cart_4=Entry(Constants.chinese, font=("rockwell",13),textvariable=y_4)
        add_cart_4.place(x = 300,y = 190)

        item_5 = Label(Constants.chinese, text = Constants.menu_3[4], font = "times 10 bold")
        item_5.place(x = 10, y = 220)

        price_5 = Label(Constants.chinese, text = Constants.menu_price_3[4], font = "times 10 bold")
        price_5.place(x = 180, y = 220)

        add_cart_5=Entry(Constants.chinese, font=("rockwell",13), textvariable=y_5)
        add_cart_5.place(x = 300,y = 220)

    