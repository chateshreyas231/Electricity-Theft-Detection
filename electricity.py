import tkinter as tk
import msvcrt

window = tk.Tk()

window.title("Electricity Theft")
window.geometry("1400x800")

filename = tk.PhotoImage(file = "paint_sym1.png")
background_label = tk.Label(window, image=filename)
background_label.place( relwidth=1, relheight=1)

window.configure(background='white')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="_"*9+"Electricity Theft Detection"+"_"*9, bg="black", fg="white", width=100, height=2,
                    font=("Tempus Sans ITC",19,"bold"))
message.place(x=0, y=0)




window.mainloop()