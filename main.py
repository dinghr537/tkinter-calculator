import tkinter as tk

# basic view of tkinter
window = tk.Tk()
window.title("calculator")
window.geometry("400x200")

answer = tk.StringVar()
on_hit = False
entry1 = tk.Entry(window, show=None)
entry2 = tk.Entry(window, show=None)
text = tk.Text(window, height=6, bg="#F0F0FF")


# a very simple version to implement "plus"
# TODO: to elegantly implement a new "plus"
def plus():
    try:
        var1 = float(entry1.get())
    except ValueError:
        text.insert('end', "shit!" + "\n")
        return
    try:
        var2 = float(entry2.get())
    except ValueError:
        text.insert('end', "shit!" + "\n")
        return
    ans = var1 + var2
    text.insert('end', str(ans) + "\n")


# button
button = tk.Button(window,
                   text="plus",
                   width=15,
                   height=2,
                   command=plus)

# pack
entry1.pack()
entry2.pack()
# label.pack()
button.pack()
text.pack()

window.mainloop()
