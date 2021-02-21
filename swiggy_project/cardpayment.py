from tkinter import *
from constants import Constants
import payment
import homepage
import cod


class CardPayment:
    def card():
        

        v = StringVar(Constants.master, "1")

        Constants.card = Frame(bg = "green")
        Constants.card.place(x = 0, y = 0, width = 400, height = 500)

        heading = Label(Constants.card, text = "Enter Card Details", font = "times 20 bold")
        heading.place(x = 90, y = 20)

        home_button = Button(Constants.card, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        card_number = Label(Constants.card, text = "Enter Card Number: ", font = "times 10 bold")
        card_number.place(x = 10, y = 80)

        card_number_entry=Entry(Constants.card, font=("rockwell",13))
        card_number_entry.place(x = 250,y = 80)

        expiry_date = Label(Constants.card, text = "Expiry Date: ", font = "times 10 bold")
        expiry_date.place(x = 10, y = 110)

        expiry_date_entry=Entry(Constants.card, font=("rockwell",13))
        expiry_date_entry.place(x = 250,y = 110)

        cvv = Label(Constants.card, text = "CVV: ", font = "times 10 bold")
        cvv.place(x = 10, y = 140)

        cvv_entry=Entry(Constants.card, font=("rockwell",13))
        cvv_entry.place(x = 250,y = 140)

        card_type = Label(Constants.card, text = "Enter Card Type:  ", font = "times 10 bold")
        card_type.place(x = 10, y = 170)

        master = Radiobutton(Constants.card, text = "Master", font = "times 10 bold", variable=v, value="1")
        master.place(x = 170, y = 170)

        visa = Radiobutton(Constants.card, text = "visa", font = "times 10 bold", variable=v, value="2")
        visa.place(x = 250, y = 170)

        rupay = Radiobutton(Constants.card, text = "Rupay", font = "times 10 bold", variable=v, value="3")
        rupay.place(x = 320, y = 170)
        
        back_button = Button(Constants.card, text = "<< Back", font = ("rockwell", 11),foreground = 'blue', command = payment.Payment.payNow)
        back_button.place(x = 10, y = 10)

        pay_button = Button(Constants.card, text = "Make Payment", font = ("rockwell", 13),foreground = 'red', command=cod.Cod.cash("Friend"))
        pay_button.place(x = 140, y = 220)
        
