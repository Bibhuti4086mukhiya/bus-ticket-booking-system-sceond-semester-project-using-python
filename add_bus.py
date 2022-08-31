from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from connection import MyDb
from tkinter import Button, Tk


class AddBus:

    def __init__(self):

        self.update_index = ''
        self.database = MyDb()

    def bus_add(self):
        try:
            self.window5 = Tk()
            self.window5.title('Add bus')
            self.window5.geometry('1200x500')
            self.window5.configure(bg='darkorange1')

            self.lblbox1 = Label(self.window5, bg='darkorange2', width=24, height=14, font=('Ariel', 15, 'bold'))
            self.lblbox1.place(x=15, y=95)

            self.lbl9 = Label(self.window5, text=' REGISTRATION OF BUS', fg='black', bg='darkorange1',
                              font=('Century', 25, 'bold'))
            self.lbl9.place(x=380, y=10)

            self.lbl = Label(self.window5, text='Bus Number', fg='black', bg='darkorange2',
                             font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=100)

            self.ent_bn = Entry(self.window5, bg='silver')
            self.ent_bn.place(x=180, y=105)

            self.lbl = Label(self.window5, text='Bus Company', fg='black', bg='darkorange2',
                             font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=150)

            self.bc_ent = Entry(self.window5, bg='silver')
            self.bc_ent.place(x=180, y=155)

            self.lbl = Label(self.window5, text='Driver Name', fg='black', bg='darkorange2',
                             font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=200)

            self.dn_ent = Entry(self.window5, bg='silver')
            self.dn_ent.place(x=180, y=205)

            self.lbl = Label(self.window5, text='Driver Contact', fg='black', bg='darkorange2',
                             font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=250)

            self.dc_ent = Entry(self.window5, bg='silver')
            self.dc_ent.place(x=180, y=255)

            self.lbl = Label(self.window5, text='Total Seat', fg='black', bg='darkorange2',
                             font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=300)

            self.ts_ent = Entry(self.window5, bg='silver')
            self.ts_ent.place(x=180, y=305)

            self.lbl = Label(self.window5, text='Route', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=350)

            self.r_ent = Entry(self.window5, bg='silver')
            self.r_ent.place(x=180, y=350)

            self.lbl1 = Label(self.window5, text=' Departure Time', fg='black', bg='darkorange2',
                              font=('Cambria', 12, 'bold'))
            self.lbl1.place(x=25, y=400)

            self.dt_ent = Entry(self.window5, bg='silver')
            self.dt_ent.place(x=180, y=400)

            self.style = ttk.Style()
            self.style.theme_use("default")
            self.style.configure("mystyle.Treeview", font=('Ariel', 8, 'bold'))
            self.style.configure("mystyle.Treeview.Heading", font=('Ariel', 9, 'bold'))

            self.add_tree = ttk.Treeview(self.window5, style="mystyle.Treeview",
                                         column=('n', 'w', 'p', 'm', 'c', 'g', 'h'))
            self.add_tree.place(x=450, y=95)
            self.add_tree['show'] = 'headings'
            self.add_tree.column('n', width=100)
            self.add_tree.column('w', width=100)
            self.add_tree.column('p', width=100)
            self.add_tree.column('m', width=100)
            self.add_tree.column('c', width=100)
            self.add_tree.column('g', width=100)
            self.add_tree.column('h', width=100)
            self.add_tree.heading('n', text='Bus number')
            self.add_tree.heading('w', text='Bus Company')
            self.add_tree.heading('p', text='Driver Name')
            self.add_tree.heading('m', text='Driver Contact')
            self.add_tree.heading('c', text='Total Seat')
            self.add_tree.heading('g', text='Route')
            self.add_tree.heading('h', text='Departure Time')
            self.treeview_method()

            self.addedbus_but = Button(self.window5, text="ADD", command=self.add_bus, bg='darkorange3',
                                       font=('Century', '10', 'bold'))
            self.addedbus_but.place(x=450, y=350)

            self.update1_but = Button(self.window5, text="UPDATE", command=self.update_busdetail, bg='darkorange3',
                                      font=('Century', '10', 'bold'))
            self.update1_but.place(x=500, y=350)

            self.delete1_but = Button(self.window5, text="DELETE", command=self.delete_000, bg='darkorange3',
                                      font=('Century', '10', 'bold'))
            self.delete1_but.place(x=581, y=350)

            self.back_but = Button(self.window5, text="BACK", bg='darkorange3', command=self.destroy,
                                   font=('Century', '10', 'bold'))
            self.back_but.place(x=660, y=350)

            self.window5.mainloop()

        except Exception as e:
            print(e)

    def destroy(self):
        from choose import Choose
        self.window5.destroy()
        self.pick = Choose()
        self.pick.window3()

    def add_bus(self):
        try:
            self.database = MyDb()
            bus_number = self.ent_bn.get()
            bus_company = self.bc_ent.get()
            driver_name = self.dn_ent.get()
            driver_contact = self.dc_ent.get()
            total_seat = self.ts_ent.get()
            route = self.r_ent.get()
            dep_time = self.dt_ent.get()
            if bus_number == '' or bus_company == '' or driver_name == '' or driver_contact == '' or total_seat == '' or route == '' or dep_time == '':
                messagebox.showerror('Error', ' Enter each boxes carefully!')
            # return False
            else:
                qry = '''insert into bus_register (bus_number, bus_company, driver_name, driver_contact, total_seat, route,dep_time) values(%s,%s,%s,%s,%s,%s,%s)'''
                values = (bus_number, bus_company, driver_name, driver_contact, total_seat, route, dep_time)
                self.database.iud(qry, values)
                messagebox.showinfo('Done', 'Added bus successfully!')
                self.treeview_method()
                # return True
        except Exception as e:
            print(e)
            # return False

    def data_treeview(self):
        try:
            self.database = MyDb()
            qry = '''select * from bus_register '''
            bus = self.database.get_data(qry)
            return bus
        except Exception as e:
            print(e)

    def treeview_method(self):
        try:
            buses = self.data_treeview()
            self.add_tree.delete(*self.add_tree.get_children())
            for i in buses:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                self.add_tree.bind("<Double-1>", self.select_item)
                # seleted event pass
        except Exception as e:
            print(e)

    def update_bus(self, index, bus_number, bus_company, driver_name, driver_contact, total_seat, route, dep_time):
        try:
            qry = "UPDATE bus_register SET bus_number = %s, bus_company = %s, driver_name = %s, driver_contact=%s, total_seat=%s, route =%s, dep_time =%s WHERE id = %s"
            values = (bus_number, bus_company, driver_name, driver_contact, total_seat, route, dep_time, index)
            self.database.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def update_busdetail(self):
        try:
            bus_number = self.ent_bn.get()
            bus_company = self.bc_ent.get()
            driver_name = self.dn_ent.get()
            driver_contact = self.dc_ent.get()
            total_seat = self.ts_ent.get()
            route = self.r_ent.get()
            dep_time = self.dt_ent.get()
            if self.update_index == "":
                messagebox.showerror("Error", "Select Item first")

            elif not bus_number == '' or bus_company == '' or driver_name == '' or driver_contact == '' or total_seat == '' or route == '' or dep_time == '':

                if self.update_bus(int(self.update_index), bus_number, bus_company, driver_name, driver_contact,
                                   total_seat, route, dep_time):
                    messagebox.showinfo("Item", "Item Updated")
                    self.treeview_method()
                else:
                    messagebox.showerror("Error", "Item can not be Updated")
        except Exception as e:
            print(e)

    def select_item(self, event):
        try:
            sel_row = self.add_tree.selection()[0]
            sel_item = self.add_tree.item(sel_row)
            self.update_index = self.add_tree.item(sel_row, 'text')
            selected_data = self.add_tree.item(sel_row, 'values')
            self.ent_bn.delete(0, 'end')
            self.ent_bn.insert(0, selected_data[0])
            self.bc_ent.delete(0, 'end')
            self.bc_ent.insert(0, selected_data[1])
            self.dn_ent.delete(0, 'end')
            self.dn_ent.insert(0, selected_data[2])
            self.dc_ent.delete(0, 'end')
            self.dc_ent.insert(0, selected_data[3])
            self.ts_ent.delete(0, 'end')
            self.ts_ent.insert(0, selected_data[4])
            self.r_ent.delete(0, 'end')
            self.r_ent.insert(0, selected_data[5])
            self.dt_ent.delete(0, 'end')
            self.dt_ent.insert(0, selected_data[6])
        except Exception as e:
            print(e)

    def delete_bus(self, id):
        try:
            qry = "DELETE FROM bus_register WHERE id = %s"
            values = (id)
            self.database.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_000(self):
        try:
            bus_number = self.ent_bn.get()
            bus_company = self.bc_ent.get()
            driver_name = self.dn_ent.get()
            driver_contact = self.dc_ent.get()
            total_seat = self.ts_ent.get()
            route = self.r_ent.get()
            dep_time = self.dt_ent.get()
            if self.update_index == "":
                messagebox.showerror("Error", "Select Item first")
            elif not bus_number == '' or bus_company == '' or driver_name == '' or driver_contact == '' or total_seat == '' or route == '' or dep_time == '':
                self.delete_bus(self.del_1(bus_company, bus_company))
                messagebox.showinfo("Success", "Delete success")
                self.treeview_method()
        except Exception as e:
            print(e)

    def del_1(self, bus_number, bus_company1):
        try:
            bus_number = self.ent_bn.get()
            bus_company1 = self.bc_ent.get()
            qry = '''select id from bus_register where bus_number = %s and bus_company= %s '''
            values = (bus_number, bus_company1)
            result = self.database.get_data_p(qry, values)
            mukhiya = (result[0])
            return mukhiya
        except Exception as e:
            print(e)
