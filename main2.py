import customtkinter as ctk
#----------------------------
# create window
#----------------------------
app = ctk.CTk()

app.title("my first gui")
app.geometry("400x300")

#--------------------------
# create.label
#-------------------------
label = ctk.CTkLabel(
    app, 
    text="hello there",
    font=("Arial", 25),
    text_color="orange")
label.pack(pady=20)

#----------------------------
# change the label after creating it
label.configure(text="i change")
#-------------------------
#----------------------------
app.mainloop()