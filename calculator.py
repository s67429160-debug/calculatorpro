import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window

app = ctk.CTk()
app.title("Calculator")
app.geometry("350x500")

# Display
display = ctk.CTkEntry(
    app,
    width=300,
    height=50,
    font=("Arial", 24),
    justify="right"
)

display.pack(pady=20)
def button_click(number):
    current= display.get()
    display.delete(0,"end")
    display.insert(0, current + str(number))
def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, "end")
        display.insert(0, str(result))

    except:
        display.delete(0, "end")
        display.insert(0, "Error")


frame = ctk.CTkFrame(app)
frame.pack(pady = 10)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
    frame.grid_rowconfigure(i, weight=1)
button7 = ctk.CTkButton(
    frame,
    text ="7",
    width=60,
    height=60,
command=lambda: button_click(7)
)
button7.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")

button8 = ctk.CTkButton(
    frame,
    text ="8",
    width=60,
    height=60,
command=lambda: button_click(8)
    
)

button8.grid(row=0, column=1, padx=5, pady=5)
button9 = ctk.CTkButton(
    frame,
    text ="9",
    width=60,
    height=60,
    command=lambda: button_click(9)
)
button9.grid(row=0, column=2, padx=5, pady=5)
buttondiv = ctk.CTkButton(
    frame,
    text ="/",
    width=60,
    height=60,
    command=lambda: button_click('/')
)
buttondiv.grid(row=0, column=3, padx=5, pady=5)
button4 = ctk.CTkButton(
    frame,
    text ="4",
    width=60,
    height=60,
    command=lambda: button_click(4)
)
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = ctk.CTkButton(
    frame,
    text ="5",
    width=60,
    height=60,
    command=lambda: button_click(5)
)
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = ctk.CTkButton(
    frame,
    text ="6",
    width=60,
    height=60,
    command=lambda: button_click(6)
)
button6.grid(row=1, column=2, padx=5, pady=5)
button_mul = ctk.CTkButton(
    frame,
    text ="*",
    width=60,
    height=60,
    command=lambda: button_click('*')
)
button_mul.grid(row=1, column=3, padx=5, pady=5)
button1 = ctk.CTkButton(
    frame,
    text ="1",
    width=60,
    height=60,
    command=lambda: button_click(1)
)
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = ctk.CTkButton(
    frame,
    text ="2",
    width=60,
    height=60,
    command=lambda: button_click(2)
)
button2.grid(row=2, column=1, padx=5, pady=5)
button3 = ctk.CTkButton(
    frame,
    text ="3",
    width=60,
    height=60,
    command=lambda: button_click(3)
)
button3.grid(row=2, column=2, padx=5, pady=5)
buttonsub = ctk.CTkButton(
    frame,
    text ="-",
    width=60,
    height=60,
    command=lambda: button_click('-')
)
buttonsub.grid(row=2, column=3, padx=5, pady=5)
buttonclear = ctk.CTkButton(
    frame,
    text ="C",
    width=60,
    height=60,
    command=lambda: display.delete(0, "end")

)
buttonclear.grid(row=3, column=0, padx=5, pady=5)
buttonzero = ctk.CTkButton(
    frame,
    text ="0",
    width=60,
    height=60,
    command=lambda: button_click(0)
)
buttonzero.grid(row=3, column=1, padx=5, pady=5)
buttonequal = ctk.CTkButton(
    frame,
    text ="=",
    width=60,
    height=60,
    command=lambda: calculate()
)
buttonequal.grid(row=3, column=2, padx=5, pady=5)
buttonadd = ctk.CTkButton(
    frame,
    text ="+",
    width=60,
    height=60,
    command=lambda: button_click('+')
)
buttonadd.grid(row=3, column=3, padx=5, pady=5)

def clear_display():
    display.delete(0, "end")
    command=lambda: clear_display()
def key_pressed(event):
    key = event.keysym
    print("pressed:", key)

    # Numbers
    if key.isdigit():
        button_click(key)

    # Operators
    elif key in ["plus", "KP_Add"]:
        button_click("+")

    elif key in ["minus", "KP_Subtract"]:
        button_click("-")

    elif key in ["asterisk", "KP_Multiply"]:
        button_click("*")

    elif key in ["slash", "KP_Divide"]:
        button_click("/")

    # Enter
    elif key == "Return":
        calculate()

    # Backspace
    elif key == "BackSpace":
        current = display.get()
        display.delete(0, "end")
        display.insert(0, current[:-1])

    # Escape
    elif key == "Escape":
        clear_display()

 #outside the function
app.bind("<Key>", key_pressed)

app.mainloop()