#calculator
import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

BG = "#000000"
BTN = "#080808"
BTN_PRESS = "#000000"

window = tk.Tk()
window.title("Calculator")
window.geometry("500x690")
window.resizable(False, False)
window.configure(bg=BG)

frame = tk.Frame(window, bg=BG)
frame.pack(fill="both", expand=True, padx=5, pady=5)

label = tk.Label(
    frame,
    text="0",
    font=("Arial", 45),
    bg=BG,
    fg="white",
    anchor="e",
    padx=10
)
label.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 5))

A = ""
B = ""
operator = None
new_number = True

def update_display():
    text = label["text"]

    if len(text) > 12:
        text = text[-12:]

    label["text"] = text

    length = len(text)
    if length <= 6:
        label.config(font=("Arial", 45))
    elif length <= 9:
        label.config(font=("Arial", 35))
    else:
        label.config(font=("Arial", 25))

def button_clicked(value):
    global A, B, operator, new_number

    if value == "AC":
        A = B = ""
        operator = None
        new_number = True
        label["text"] = "0"
        update_display()
        return

    if value == "+/-":
        label["text"] = label["text"].lstrip("-") if label["text"].startswith("-") else "-" + label["text"]
        update_display()
        return

    if value == "%":
        try:
            label["text"] = str(float(label["text"]) / 100)
        except:
            label["text"] = "Error"
        update_display()
        return

    if value == "√":
        try:
            num = float(label["text"])
            if num < 0:
                raise ValueError
            label["text"] = str(num ** 0.5)
        except:
            label["text"] = "Error"
        update_display()
        return

    if value in ["÷", "×", "-", "+"]:
        A = label["text"]
        operator = value
        new_number = True
        return

    if value == "=":
        if operator and A:
            B = label["text"]
            try:
                a, b = float(A), float(B)
                result = {
                    "÷": a / b,
                    "×": a * b,
                    "-": a - b,
                    "+": a + b
                }[operator]
                label["text"] = str(result)
            except:
                label["text"] = "Error"

        operator = None
        new_number = True
        update_display()
        return

    if value.isdigit() or value == ".":
        if new_number:
            label["text"] = value if value != "." else "0."
            new_number = False
        else:
            if value == "." and "." in label["text"]:
                return
            label["text"] += value

        update_display()

for r in range(len(button_values)):
    for c in range(len(button_values[r])):
        val = button_values[r][c]

        btn = tk.Button(
            frame,
            text=val,
            font=("Arial", 26),
            bg=BTN,
            fg="white",
            activebackground=BTN_PRESS,
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda v=val: button_clicked(v)
        )

        btn.grid(row=r+1, column=c, sticky="nsew", padx=4, pady=4)

for i in range(6):
    frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

window.update_idletasks()
x = (window.winfo_screenwidth() // 2) - 250
y = (window.winfo_screenheight() // 2) - 345
window.geometry(f"500x690+{x}+{y}")

window.mainloop()