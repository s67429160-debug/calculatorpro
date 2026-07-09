import customtkinter as ctk
# window
app = ctk.CTk()
app.geometry("400x200")

entry = ctk.CTkEntry(app)
entry.pack(pady=20)
button = ctk.CTkButton(
    app,
    text="print",
  command=lambda: print(entry.get())
 )
button.pack()
app.mainloop()
