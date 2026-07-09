import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

def say_hello():
    print("Hello Shivam!")

button = ctk.CTkButton(
    app,
    text="Click Me",
    command=say_hello
)

button.pack(pady=40)

app.mainloop()