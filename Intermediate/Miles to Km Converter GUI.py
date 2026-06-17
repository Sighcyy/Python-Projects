import tkinter



window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width = 300, height = 100)


input = tkinter.Entry(width = 5)
input.grid(row = 0, column = 1)

miles = tkinter.Label(text = 'Miles')
miles.grid(row = 0, column = 2)


isequal = tkinter.Label(text = 'Is equal to')
isequal.grid(row = 1, column = 0)

kmvalue = tkinter.Label(text = '0')
kmvalue.grid(row = 1, column = 1)

km = tkinter.Label(text = 'Km')
km.grid(row = 1, column = 2)

def calculate():
    miles = float(input.get())
    km = miles * 1.609
    kmvalue["text"] = str(km)


calculate = tkinter.Button(text = "Calculate", command = calculate)
calculate.grid(row = 2, column = 1)










window.mainloop()
