from tkinter import * 
from constants import Constants
import billing
import homepage
import cardpayment
import cod


class Payment:
    def payNow():
        y_1 = StringVar()
        y_2 = StringVar()
        y_3 = StringVar()
        y_4 = StringVar()
        y_5 = StringVar()
        y_1.set("")
        y_2.set("")
        y_3.set("")
        y_4.set("")
        y_5.set("")

        v = StringVar(Constants.master, "1")

        Constants.payNow = Frame(bg = "green")
        Constants.payNow.place(x = 0, y = 0, width = 400, height = 500)


        heading = Label(Constants.payNow, text = "Enter Billing Details", font = "times 25 bold")
        heading.place(x = 50, y = 20)

        home_button = Button(Constants.payNow, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)

        customer_name = Label(Constants.payNow, text = "Enter Your Name: ", font = "times 10 bold")
        customer_name.place(x = 10, y = 80)

        customer_name_entry=Entry(Constants.payNow, font=("rockwell",13), textvariable=y_1)
        customer_name_entry.place(x = 250,y = 80)

        customer_mobile = Label(Constants.payNow, text = "Enter Your Mobile Number: ", font = "times 10 bold")
        customer_mobile.place(x = 10, y = 110)

        customer_mobile_entry=Entry(Constants.payNow, font=("rockwell",13), textvariable=y_2)
        customer_mobile_entry.place(x = 250,y = 110)

        customer_address = Label(Constants.payNow, text = "Enter Address: ", font = "times 10 bold")
        customer_address.place(x = 10, y = 140)

        customer_address_entry=Entry(Constants.payNow, font=("rockwell",13), textvariable= y_3)
        customer_address_entry.place(x = 250,y = 140)

        heading_2 = Label(Constants.payNow, text = "Select Payment Option", font = "times 15 bold")
        heading_2.place(x = 90, y = 180)

        
        cod_option = Radiobutton(Constants.payNow, text = "COD", font = "times 10 bold", variable=v, value="1",command=(lambda :cod.Cod.cash (customer_name_entry.get())))
        cod_option.place(x = 150, y = 220)

        prepaid_option = Radiobutton(Constants.payNow, text = "Credit Card/Debit Card", font = "times 10 bold", variable=v, value="2", command=cardpayment.CardPayment.card)
        prepaid_option.place(x = 150, y = 250)

      

