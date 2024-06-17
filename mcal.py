from tkinter import *

def perform_operation():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        choice = operator.get()

        if choice == '+':
            result.set(a + b)
        elif choice == '-':
            result.set(a - b)
        elif choice == '*':
            result.set(a * b)
        elif choice == '/':
            result.set(a / b)
        elif choice == '%':
            result.set(a % b)
        else:
            result.set("Invalid operator")
    except ValueError:
        result.set("Invalid input")

app = Tk()
app.geometry("400x300")
app.title("Calculator")

Label(app, text="Please enter the first number:").pack(pady=5)
entry1 = Entry(app, font=("Courier New", 12, 'bold'))
entry1.pack(pady=5)

Label(app, text="Please enter the second number:").pack(pady=5)
entry2 = Entry(app, font=("Courier New", 12, 'bold'))
entry2.pack(pady=5)

Label(app, text="Available operations: +, -, *, /, %").pack(pady=5)
operator = StringVar()
entry3 = Entry(app, textvariable=operator, font=("Courier New", 12, 'bold'))
entry3.pack(pady=5)

Button(app, text="Calculate", command=perform_operation, font=("Courier New", 12, 'bold')).pack(pady=10)

result = StringVar()
Label(app, textvariable=result, font=("Courier New", 12, 'bold')).pack(pady=10)

app.mainloop()
