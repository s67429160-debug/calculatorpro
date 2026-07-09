import customtkinter as ctk
#window

app = ctk.CTk()
app.title("my first app")
app.geometry("400x300")

#label
label = ctk.CTkLabel(
    app,
    text="hello",
    font=("Arial", 35)
)
label.pack(pady=20)
#
#function
def change_text():
    label.configure(text="clicked button")
    #
    # button
button = ctk.CTkButton(
    app,
    text="press me",
    command=change_text
)
button.pack()
#
# run
#
app.mainloop()