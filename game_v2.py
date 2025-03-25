import tkinter

menu = tkinter.Tk()
menu.title("MENU")
quit = tkinter.Button(menu, text="QUIT", width=25, command=menu.destroy)
quit.pack()
menu.mainloop()