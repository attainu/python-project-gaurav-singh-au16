from tkinter import *
from constants import Constants
import homepage
import payment

class Billing:
    def calculateMaincourse(item_1, item_2, item_3, item_4, item_5):
        Constants.calculate = Frame(bg = "green")
        Constants.calculate.place(x = 0, y = 0, width = 400, height = 500)

        heading = Label(Constants.calculate, text = "Billing Details", font = "times 25 bold")
        heading.place(x = 90, y = 20)

        home_button = Button(Constants.calculate, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)


        order_1 = Constants.menu_price_1[0]*int(item_1)
        order_2 = Constants.menu_price_1[1]*int(item_2)
        order_3 = Constants.menu_price_1[2]*int(item_3)
        order_4 = Constants.menu_price_1[3]*int(item_4)
        order_5 = Constants.menu_price_1[4]*int(item_5)
        total_1 = order_1 + order_2 +order_3 +order_4 +order_5

        cgst_1 = (total_1 * 9) / 100
        sgst_1 = (total_1 * 9) / 100

        final_1 = total_1 + cgst_1 + sgst_1

        if total_1 > 0:

            billing_details_1 = Label(Constants.calculate, text = "Thankyou For Ordering Food!!!", font = "times 15 bold")
            billing_details_1.place(x = 60, y = 80)

            billing_details_1 = Label(Constants.calculate, text = f"Your Total Bill Is Rs.{final_1}" , font = "rockwell 20 bold")
            billing_details_1.place(x = 30, y = 120)

            billing_details_1 = Label(Constants.calculate, text = "Amount Details" , font = "rockwell 15 bold")
            billing_details_1.place(x = 90, y = 165)

            billing_details_1 = Label(Constants.calculate, text = f"Order Amount     : {total_1}" , font = "rockwell 15 bold")
            billing_details_1.place(x = 80, y = 200)

            billing_details_1 = Label(Constants.calculate, text = f"CGST             : {cgst_1}" , font = "rockwell 15 bold")
            billing_details_1.place(x = 80, y = 230)

            billing_details_1 = Label(Constants.calculate, text = f"SGST              : {sgst_1}" , font = "rockwell 15 bold")
            billing_details_1.place(x = 80, y = 260)

            billing_details_1 = Label(Constants.calculate, text = f"Final To Be Paid : {final_1}" , font = "rockwell 15 bold")
            billing_details_1.place(x = 80, y = 290)

            pay_button = Button(Constants.calculate, text = "Pay Now", font = ("rockwell", 13),foreground = 'red', command=payment.Payment.payNow)
            pay_button.place(x = 140, y = 330)

        else:
            
            billing_details_1 = Label(Constants.calculate, text = "You Have Not Order Anything", font = "rockwell 15 bold")
            billing_details_1.place(x = 60, y = 170)
            billing_details_1 = Label(Constants.calculate, text = "Checkout Again And Order \nYour Favourite Dish!!!", font = "rockwell 15 bold")
            billing_details_1.place(x = 60, y = 200)

    def calculateParatha(item_1, item_2, item_3, item_4, item_5):

        Constants.calculate = Frame(bg = "green")
        Constants.calculate.place(x = 0, y = 0, width = 400, height = 500)

        heading = Label(Constants.calculate, text = "Billing Details", font = "times 25 bold")
        heading.place(x = 90, y = 20)

        home_button = Button(Constants.calculate, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)
        
        

        order_1 = Constants.menu_price_2[0]*int(item_1)
        order_2 = Constants.menu_price_2[1]*int(item_2)
        order_3 = Constants.menu_price_2[2]*int(item_3)
        order_4 = Constants.menu_price_2[3]*int(item_4)
        order_5 = Constants.menu_price_2[4]*int(item_5)
        total_2 = order_1 + order_2 +order_3 +order_4 +order_5

        cgst_2 = (total_2 * 9) / 100
        sgst_2 = (total_2 * 9) / 100

        final_2 = total_2 + cgst_2 + sgst_2
        
        if total_2 > 0:

            billing_details_2 = Label(Constants.calculate, text = "Thankyou For Ordering Food!!!", font = "times 15 bold")
            billing_details_2.place(x = 60, y = 80)

            billing_details_2 = Label(Constants.calculate, text = f"Your Total Bill Is Rs.{final_2}" , font = "rockwell 20 bold")
            billing_details_2.place(x = 30, y = 120)

            billing_details_2 = Label(Constants.calculate, text = "Amount Details" , font = "rockwell 15 bold")
            billing_details_2.place(x = 90, y = 165)

            billing_details_2 = Label(Constants.calculate, text = f"Order Amount     : {total_2}" , font = "rockwell 15 bold")
            billing_details_2.place(x = 80, y = 200)

            billing_details_2 = Label(Constants.calculate, text = f"CGST             : {cgst_2}" , font = "rockwell 15 bold")
            billing_details_2.place(x = 80, y = 230)

            billing_details_2 = Label(Constants.calculate, text = f"SGST              : {sgst_2}" , font = "rockwell 15 bold")
            billing_details_2.place(x = 80, y = 260)

            billing_details_2 = Label(Constants.calculate, text = f"Final To Be Paid : {final_2}" , font = "rockwell 15 bold")
            billing_details_2.place(x = 80, y = 290)

            pay_button = Button(Constants.calculate, text = "Pay Now", font = ("rockwell", 13),foreground = 'red', command=payment.Payment.payNow)
            pay_button.place(x = 140, y = 330)

        else:
            
            billing_details_1 = Label(Constants.calculate, text = "You Have Not Order Anything", font = "rockwell 15 bold")
            billing_details_1.place(x = 60, y = 170)
            billing_details_1 = Label(Constants.calculate, text = "Checkout Again And Order \nYour Favourite Dish!!!", font = "rockwell 15 bold")
            billing_details_1.place(x = 60, y = 200)

    def calculateChinese(item_1, item_2, item_3, item_4, item_5):
    
        Constants.calculate = Frame(bg = "green")
        Constants.calculate.place(x = 0, y = 0, width = 400, height = 500)

        heading = Label(Constants.calculate, text = "Billing Details", font = "times 25 bold")
        heading.place(x = 90, y = 20)

        home_button = Button(Constants.calculate, text = "Home", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 10, y = 450)
        
        

        order_1 = Constants.menu_price_3[0]*int(item_1)
        order_2 = Constants.menu_price_3[1]*int(item_2)
        order_3 = Constants.menu_price_3[2]*int(item_3)
        order_4 = Constants.menu_price_3[3]*int(item_4)
        order_5 = Constants.menu_price_3[4]*int(item_5)
        total_3 = order_1 + order_2 +order_3 +order_4 +order_5

        cgst_3 = (total_3 * 9) / 100
        sgst_3 = (total_3 * 9) / 100

        final_3 = total_3 + cgst_3 + sgst_3

        if total_3 > 0:
    
            billing_details_3 = Label(Constants.calculate, text = "Thankyou For Ordering Food!!!", font = "times 15 bold")
            billing_details_3.place(x = 60, y = 80)

            billing_details_3 = Label(Constants.calculate, text = f"Your Total Bill Is Rs.{final_3}" , font = "rockwell 20 bold")
            billing_details_3.place(x = 30, y = 120)

            billing_details_3 = Label(Constants.calculate, text = "Amount Details" , font = "rockwell 15 bold")
            billing_details_3.place(x = 90, y = 165)

            billing_details_3 = Label(Constants.calculate, text = f"Order Amount     : {total_3}" , font = "rockwell 15 bold")
            billing_details_3.place(x = 80, y = 200)

            billing_details_3 = Label(Constants.calculate, text = f"CGST             : {cgst_3}" , font = "rockwell 15 bold")
            billing_details_3.place(x = 80, y = 230)

            billing_details_3 = Label(Constants.calculate, text = f"SGST              : {sgst_3}" , font = "rockwell 15 bold")
            billing_details_3.place(x = 80, y = 260)

            billing_details_3 = Label(Constants.calculate, text = f"Final To Be Paid : {final_3}" , font = "rockwell 15 bold")
            billing_details_3.place(x = 80, y = 290)

            pay_button = Button(Constants.calculate, text = "Pay Now", font = ("rockwell", 13),foreground = 'red', command=payment.Payment.payNow)
            pay_button.place(x = 140, y = 330)
            

        else:
            
            billing_details_1 = Label(Constants.calculate, text = "You Have Not Order Anything", font = "rockwell 15 bold")
            billing_details_1.place(x = 60, y = 170)
            billing_details_1 = Label(Constants.calculate, text = "Checkout Again And Order \nYour Favourite Dish!!!", font = "rockwell 15 bold")
            billing_details_1.place(x = 60, y = 200)
