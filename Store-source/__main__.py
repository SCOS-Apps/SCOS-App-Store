import tkinter as tk

window = tk.Tk()
window.title("SCOS App Store")
window.resizable(False, False)

if __name__ == "__main__":
    window.mainloop()
else:
    print("Sorry, you cannot run the store from another app.")