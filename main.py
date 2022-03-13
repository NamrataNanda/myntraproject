import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# creating login page

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-11 at 7.41.46 PM (1).jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text='Login', bg='ivory', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=100, pady=100)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=200, y=190)

        # creating a register window

        def register():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="deep sky blue")
            l1.place(x=100, y=5)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=500, y=5)

            l2 = tk.Label(window, text="Password:", font=("Arial", 15), bg="deep sky blue")
            l2.place(x=100, y=35)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x=500, y=35)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="deep sky blue")
            l3.place(x=100, y=65)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x=500, y=65)

            l4 = tk.Label(window, text="Email:", font=("Arial", 15), bg="deep sky blue")
            l4.place(x=100, y=95)
            t4 = tk.Entry(window, width=30, bd=5)
            t4.place(x=500, y=95)

            l5 = tk.Label(window, text="Address:", font=("Arial", 15), bg="deep sky blue")
            l5.place(x=100, y=125)
            t5 = tk.Entry(window, width=30, bd=5)
            t5.place(x=500, y=125)

            l6 = tk.Label(window, text="Contact number:", font=("Arial", 15), bg="deep sky blue")
            l6.place(x=100, y=155)
            t6 = tk.Entry(window, width=30, bd=5)
            t6.place(x=500, y=155)

            l7 = Label(window, text="Gender:", width=20, font=("Arial", 15), bg="deep sky blue")
            l7.place(x=25, y=190)
            var = IntVar()
            t7 = tk.Radiobutton(window, text="Male", padx=20, variable=var, value=1).place(x=500, y=190)
            t7 = tk.Radiobutton(window, text="Female", padx=20, variable=var, value=2).place(x=600, y=190)

            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "" or t4.get() != "" or t5.get() != "" or t6.get() != "" or t7.get() != "":
                    if t2.get() == t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get() + "," + t2.get() + "\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")

            b1 = tk.Button(window, text="Sign in", font=("Arial", 15), bg="#ffc22a", command=check)
            b1.place(x=350, y=250)

            window.geometry("800x350")
            window.mainloop()

        B2 = tk.Button(self, text="Register", bg="dark orange", font=("Arial", 15), command=register)
        B2.place(x=650, y=40)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-11 at 7.41.46 PM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Label_1 = tk.Label(self, text="Welcome to Myntra", font=('Arial', 25))
        Label_1.place(x=100, y=100)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)

        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)

    # creating 3rd page


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # bg image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # now we are adding products in our category

        # 1st

        Button = tk.Button(self, text="TELEVISION", font=("Arial", 15),
                           command=lambda: controller.show_frame(FourthPage))
        Button.place(x=10, y=40)

        load_1 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.11 AM (2).jpeg")
        photo_1 = ImageTk.PhotoImage(load_1)
        label_1 = tk.Label(self, image=photo_1)
        label_1.image = photo_1
        label_1.place(x=10, y=90)

        # 2nd

        Button = tk.Button(self, text="MOBILE", font=("Arial", 15), command=lambda: controller.show_frame(FifthPage))
        Button.place(x=320, y=40)

        load_2 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.10 AM.jpeg")
        photo_2 = ImageTk.PhotoImage(load_2)
        label_2 = tk.Label(self, image=photo_2)
        label_2.image = photo_2
        label_2.place(x=300, y=90)

        # 3rd

        Button = tk.Button(self, text="LAPTOP", font=("Arial", 15), command=lambda: controller.show_frame(EighthPage))
        Button.place(x=300, y=250)

        load_3 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM (1).jpeg")
        photo_3 = ImageTk.PhotoImage(load_3)
        label_3 = tk.Label(self, image=photo_3)
        label_3.image = photo_3
        label_3.place(x=300, y=300)

        # 4th

        Button = tk.Button(self, text="HEADPHONES", font=("Arial", 15),
                           command=lambda: controller.show_frame(SeventhPage))
        Button.place(x=10, y=250)

        load_4 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.11 AM.jpeg")
        photo_4 = ImageTk.PhotoImage(load_4)
        label_4 = tk.Label(self, image=photo_4)
        label_4.image = photo_4
        label_4.place(x=10, y=300)

        # 5th

        Button = tk.Button(self, text="SPEAKERS", font=("Arial", 15), command=lambda: controller.show_frame(SixthPage))
        Button.place(x=590, y=40)

        load_5 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.23 PM.jpeg")
        photo_5 = ImageTk.PhotoImage(load_5)
        label_5 = tk.Label(self, image=photo_5)
        label_5.image = photo_5
        label_5.place(x=590, y=90)

        # 6th

        Button = tk.Button(self, text="REFRIGERATOR", font=("Arial", 15),
                           command=lambda: controller.show_frame(NinthPage))
        Button.place(x=590, y=250)

        load_6 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.24 PM.jpeg")
        photo_6 = ImageTk.PhotoImage(load_6)
        label_6 = tk.Label(self, image=photo_6)
        label_6.image = photo_6
        label_6.place(x=590, y=300)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=450)

        Button = tk.Button(self, text="Quit", font=("Arial", 15), command=lambda: controller.show_frame(TenthPage))
        Button.place(x=590, y=450)


# creating 4th page
class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # product1 TV

        load1 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.11 AM (1).jpeg")
        photo1 = ImageTk.PhotoImage(load1)
        label_1 = tk.Label(self, image=photo1)
        label_1.image = photo1
        label_1.place(x=10, y=50)

        Label = tk.Label(self, text="Mi 4A Horizon Edtion 100 cm(40inch)Full HD LED Smart Android TV",
                         font=('Arial', 10))
        Label.place(x=440, y=100)

        Label = tk.Label(self, text="MRP ₹29,999", font=('Arial', 10))
        Label.place(x=440, y=120)

        def message():
            messagebox.showinfo("Message", f"Your order is successfully placed !")

        Button = tk.Button(self, text="BUY", font=("Arial", 15), command=message)
        Button.place(x=440, y=160)

        Button = tk.Button(self, text="Log-Out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=430)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=450)


# creating 5th page
class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # product2  mobile

        load2 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.24 PM (1).jpeg")
        photo2 = ImageTk.PhotoImage(load2)
        label_2 = tk.Label(self, image=photo2)
        label_2.image = photo2
        label_2.place(x=10, y=50)

        Label = tk.Label(self, text="OnePlus Nord 2 5G (8 GB RAM, 128 GB ROM, Gray Sierra", font=('Arial', 10))
        Label.place(x=440, y=100)

        Label = tk.Label(self, text="MRP ₹29,999", font=('Arial', 10))
        Label.place(x=440, y=120)

        def message():
            messagebox.showinfo("Message", f"Your order is successfully placed !")

        Button = tk.Button(self, text="BUY", font=("Arial", 15), command=message)
        Button.place(x=440, y=170)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=500)

        Button = tk.Button(self, text="Log-Out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=600, y=490)


# creating 6th page
class SixthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # product3 speaker

        load3 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.23 PM (1).jpeg")
        photo3 = ImageTk.PhotoImage(load3)
        label_3 = tk.Label(self, image=photo3)
        label_3.image = photo3
        label_3.place(x=10, y=50)

        Label = tk.Label(self, text="Sony SA-40 4.1 Channel Multimedia Speaker System with Bluetooth (BLACK)",
                         font=('Arial', 10))
        Label.place(x=10, y=350)

        Label = tk.Label(self, text="MRP ₹8,490", font=('Arial', 10))
        Label.place(x=10, y=380)

        def message():
            messagebox.showinfo("Message", f"Your order is successfully placed !")

        Button = tk.Button(self, text="BUY", font=("Arial", 15), command=message)
        Button.place(x=440, y=170)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=500)

        Button = tk.Button(self, text="Log-Out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=600, y=490)


# creating 7th page
class SeventhPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # product4 headphones
        load1 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.22 PM (2).jpeg")
        photo1 = ImageTk.PhotoImage(load1)
        label_1 = tk.Label(self, image=photo1)
        label_1.image = photo1
        label_1.place(x=0, y=30)

        Label = tk.Label(self, text="boAt Rockerz 610 Bluetooth Headphone (Brown) with Easy Tap Controls",
                         font=('Arial', 10))
        Label.place(x=410, y=250)

        Label = tk.Label(self, text="Wireless & Wired Modes, Superior User Comfort", font=('Arial', 10))
        Label.place(x=410, y=270)

        Label = tk.Label(self, text="MRP ₹3,999", font=('Arial', 10))
        Label.place(x=430, y=290)

        def message():
            messagebox.showinfo("Message", f"Your order is successfully placed !")

        Button = tk.Button(self, text="BUY", font=("Arial", 15), command=message)
        Button.place(x=440, y=340)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=500)

        Button = tk.Button(self, text="Log-Out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=600, y=500)


# creating 8th page
class EighthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # product5 laptop

        load2 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.22 PM.jpeg")
        photo2 = ImageTk.PhotoImage(load2)
        label_2 = tk.Label(self, image=photo2)
        label_2.image = photo2
        label_2.place(x=10, y=50)

        Label = tk.Label(self, text="Dell Inspiron 3501 D560413WIN9S 11th Gen Intel i5 Processor/4 GB RAM ",
                         font=('Arial', 10))
        Label.place(x=400, y=100)
        Label = tk.Label(self, text="/1 TB HDD + 256 GB SSD/15.6 FHD Display/Intel UHD Graphics/Win 10/MSO ",
                         font=('Arial', 10))
        Label.place(x=390, y=125)

        Label = tk.Label(self, text="MRP ₹57,999", font=('Arial', 10))
        Label.place(x=400, y=150)

        def message():
            messagebox.showinfo("Message", f"Your order is successfully placed !")

        Button = tk.Button(self, text="BUY", font=("Arial", 15), command=message)
        Button.place(x=420, y=180)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=500)

        Button = tk.Button(self, text="Log-Out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=600, y=500)


# creating 9th page
class NinthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        # product6  refrigerator

        load2 = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 4.15.22 PM (1).jpeg")
        photo2 = ImageTk.PhotoImage(load2)
        label_2 = tk.Label(self, image=photo2)
        label_2.image = photo2
        label_2.place(x=10, y=20)

        Label = tk.Label(self, text="Samsung 253 Ltr 2 Star Frost Free Double Door Refrigerator (RT28A3132S9 , Silver)",
                         font=('Arial', 10))
        Label.place(x=240, y=100)

        Label = tk.Label(self, text="MRP ₹24,999", font=('Arial', 10))
        Label.place(x=240, y=120)

        def message():
            messagebox.showinfo("Message", f"Your order is successfully placed !")

        Button = tk.Button(self, text="BUY", font=("Arial", 15), command=message)
        Button.place(x=240, y=170)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=480)

        Button = tk.Button(self, text="Log-Out", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=600, y=480)


# creating 10th page
class TenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image
        load = Image.open("C:/Users/nabhendu/Downloads/WhatsApp Image 2022-03-13 at 9.07.12 AM.jpeg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Label = tk.Label(self, text="THANK YOU FOR VISITING OUR APP", font=('Arial', 20))
        Label.place(x=240, y=100)

        Label = tk.Label(self, text="DO VISIT NEXT TIME", font=('Arial', 20))
        Label.place(x=240, y=140)


class Application(tk.Tk):
    def __init__(self, *args, ):
        tk.Tk.__init__(self, )

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=550)
        window.grid_columnconfigure(0, minsize=850)

        self.frames = {}
        for F in (
        FirstPage, SecondPage, ThirdPage, FourthPage, FifthPage, SixthPage, SeventhPage, EighthPage, NinthPage,
        TenthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(850, 550)
app.mainloop()