from tkinter import *
from add_bus import *
from passengerbooking import *
from tkinter import messagebox
from tkinter import ttk

class Choose:

    def __init__(self):

        self.register = AddBus()
        self.passenger = Booking()

    def window3(self):
        try:

            self.register = AddBus()
            self.passenger = Booking()

            self.window0=Tk()
            self.window0.title('booking')
            self.window0.geometry('1000x500')
            self.window0.configure(bg='darkorange1')

            self.lblc1passenger = Label(self.window0, bg='darkorange2', width=75, height=3, font=('Ariel', 10, 'bold'))
            self.lblc1passenger.place(x=0, y=185)

            self.lblc1 = Label(self.window0, bg='darkorange2', width=80, height=3, font=('Ariel', 10, 'bold'))
            self.lblc1.place(x=400, y=120)

            self.lblc1 = Label(self.window0, bg='darkorange2', width=40, height=3, font=('Ariel', 10, 'bold'))
            self.lblc1.place(x=340, y=250)

            self.lbl9 = Label(self.window0, text='WELCOME TO KATHMANDU DELUX', fg='black', bg='darkorange1', font=('Century', '25', 'bold'))
            self.lbl9.place(x=180, y=10)

            self.reg_but = Button(self.window0, text= "BUS REGISTER ", command=self.add1, bg='darkorange3',font=('Century','10', 'bold'))
            self.reg_but.place(x=425, y=130)

            self.pass_but = Button(self.window0, text="PASSENGER BOOKING", command=self.book1, bg='darkorange3', font=('Century', '10', 'bold'))
            self.pass_but.place(x=400, y=200)

            self.exit_but = Button(self.window0, text="EXIT", bg='darkorange3', command=self.exit, font=('Century', '10', 'bold'))
            self.exit_but.place(x=470, y=260)

            self.window0.mainloop()
        except Exception as e:
            print(e)

    def exit(self):

        self.exit = tkinter.messagebox.askyesno('passengerbooking', 'confirm if you want to exit')
        if self.exit > 0:
            self.window0.destroy()
            return

    def add1(self):
        self.window0.destroy()
        self.register = AddBus()
        self.register.bus_add()

    def book1(self):
        self.window0.destroy()
        self.passenger = Booking()
        self.passenger.booking()