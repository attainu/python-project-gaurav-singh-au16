from tkinter import *


class Constants:
    master=Tk()
    size = master.geometry("400x500")
    master.resizable(height=0, width=0)
    
    master.title("SWIGGY: FASTEST ONLINE DELIVERY")

    


    menu_1 = ["Kadhai Paneer", "Palak Paneeer", "Butter Naan", "Aalo Gobhi", "Tandoori Roti"]
    menu_price_1 = [200, 250, 40, 180, 25]

    menu_2 = ["Aalo Paratha", "Paneer Paratha", "Ghobhi Partha", "Onion Paratha", "Egg Paratha"]
    menu_price_2 = [40, 70, 60, 50, 80]

    menu_3 = ["Hakka Noodle", "Momoes", "Manchurian", "French Fries", "Burger"]
    menu_price_3 = [80, 60, 100, 70, 50]

    new_resturant = []
    
    new_menu_1 = []
    new_menu_price_1 = []

    new_menu_2 = []
    new_menu_price_2 = []
    
    payment_option = {"COD":"1", "Credit Card/ Debit Card":"2"}


    # def updateData(update_1, update_2, update_3, update_4, update_5):

    #     menu_price_1 = [200, 250, 40, 180, 25]

    #     if update_1 != 0:
    #         menu_price_1.pop(0)
    #         menu_price_1.insert(0, update_1)
        
    #     if update_2 != 0:
    #         menu_price_1.pop(0)
    #         menu_price_1.insert(0, update_2)

    #     if update_3 != 0:
    #         menu_price_1.pop(0)
    #         menu_price_1.insert(0, update_3)

    #     if update_4 != 0:
    #         menu_price_1.pop(0)
    #         menu_price_1.insert(0, update_4)

    #     if update_5 != 0:
    #         menu_price_1.pop(0)
    #         menu_price_1.insert(0, update_5)
