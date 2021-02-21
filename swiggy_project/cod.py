from constants import Constants
from tkinter import * 
import payment
import billing
import homepage
import random
from tkinter import messagebox


class Cod:
    def cash(name):
        x = random.randint(11111111, 99999999)
        y = random.randint(111111, 999999)
        z = random.randint(99, 9999)

        Constants.cash = Frame(bg = "green")
        Constants.cash.place(x = 0, y = 0, width = 400, height = 500)

    

        details_1 = Label(Constants.cash, text = f"Hello, {name}!!!" , font = "rockwell 15 bold", fg="red")
        details_1.place(x = 90, y = 20)

        home_button = Button(Constants.cash, text = "Order Again", font = ("rockwell", 13),foreground = 'red', command=homepage.Homepage.home)
        home_button.place(x = 120, y = 370)

        exit = Button(Constants.cash, text = "EXIT", font = ("rockwell", 13),foreground = 'red', command=Constants.master.destroy)
        exit.place(x = 150, y = 420)

        confirmation = Label(Constants.cash, text = f"Your Transaction is Sucessfull!!!\nTransaction Number: {x}\nOrder Number: OD{y}\nInvoice Number: #{z}\n\nPayment Has Been Received\n\nYour Order is Under Processing\n\nYour Food Get Delivered Soon", font = "times 15 bold", fg="red")
        confirmation.place(x = 50, y = 100)

        messagebox.showinfo("Sucessfull", "Your food Is Delivered!!!")

    
        Constants.cash.mainloop()