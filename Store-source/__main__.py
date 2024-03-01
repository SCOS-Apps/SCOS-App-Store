import tkinter as tk

window = tk.Tk()
window.title("SCOS App Store")
window.geometry("800x400")
window.resizable(False, False)
exit = tk.Button(text="Exit", command="exit")
exit.grid(row=1, column=2)

if __name__ == "__main__":
    window.mainloop()
else:
    print("Sorry, you cannot run the store from another app.")