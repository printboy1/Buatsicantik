import turtle
import tkinter as tk
import random
import threading

# Fungsi gambar teddy bear
def draw_teddy():
    turtle.clearscreen()
    teddy = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("#FFF4F4")
    teddy.speed(8)
    teddy.pensize(3)

    def circle(color, radius, x, y):
        teddy.penup()
        teddy.goto(x, y - radius)
        teddy.pendown()
        teddy.fillcolor(color)
        teddy.begin_fill()
        teddy.circle(radius)
        teddy.end_fill()

    # Kepala
    circle("#5E3B22", 70, 0, 50)
    circle("#5E3B22", 25, -45, 100)
    circle("#F5C396", 15, -45, 105)
    circle("#5E3B22", 25, 45, 100)
    circle("#F5C396", 15, 45, 105)
    circle("#F5C396", 40, 0, 20)
    circle("black", 6, -20, 60)
    circle("black", 6, 20, 60)
    circle("black", 8, 0, 30)

    # Mulut (senyum)
    teddy.penup()
    teddy.goto(-20, 10)
    teddy.pendown()
    teddy.setheading(-60)
    teddy.circle(20, 120)
    teddy.penup()

    # Tulisan
    teddy.goto(0, -150)
    teddy.color("#E75480")
    teddy.write("Maafin Aku Ya 🧸💘", align="center", font=("Comic Sans MS", 20, "bold"))

    teddy.goto(0, -180)
    teddy.write("Semoga kamu ngk marah lagi~", align="center", font=("Comic Sans MS", 14, "italic"))

    teddy.hideturtle()
    turtle.done()

# GUI Interaksi
click_count = 0

def start_app():
    root = tk.Tk()
    root.title("Halo Kamu :)")
    root.geometry("500x400")
    root.configure(bg="#FFF4F4")

    label = tk.Label(root, text="Halo kamu, apa kabar?", font=("Comic Sans MS", 16), bg="#FFF4F4")
    label.pack(pady=20)

    def after_choice():
        label.config(text="Klik tombol di bawah untuk munculin teddy bear lucu ya 😊")

        def moving_button_click():
            global click_count
            click_count += 1
            if click_count < 4:
                btn.place(x=random.randint(50, 350), y=random.randint(150, 300))
            else:
                btn.config(text="Klik lagi dong wkwkw 😜", command=final_click)
                btn.place(x=150, y=250)

        def final_click():
            root.destroy()
            threading.Thread(target=draw_teddy).start()

        btn.config(text="Klik Aku!", command=moving_button_click)
        btn.place(x=150, y=250)

    # Pilihan Jawaban
    frame = tk.Frame(root, bg="#FFF4F4")
    frame.pack()

    def make_button(text):
        return tk.Button(frame, text=text, font=("Comic Sans MS", 12), bg="#FFD1DC", command=after_choice)

    b1 = make_button("Baik")
    b2 = make_button("Biasa aja")
    b3 = make_button("Nggak tau")
    b1.grid(row=0, column=0, padx=10, pady=10)
    b2.grid(row=0, column=1, padx=10, pady=10)
    b3.grid(row=0, column=2, padx=10, pady=10)

    # Tombol moving disiapkan dulu
    btn = tk.Button(root, text="Klik Aku!", font=("Comic Sans MS", 12), bg="#FFC0CB")

    root.mainloop()

from playsound import playsound
threading.Thread(target=lambda: playsound("videoplayback.mp3"), daemon=True).start()


start_app()
