from cgitb import reset
import tkinter as tk

def clearInput():
  radioValue.set(0)  

app = tk.Tk()
app.geometry("800x600")

radioValue = tk.IntVar()

radioOne = tk.Radiobutton(app, text="January", variable=radioValue, value="January")
radioTwo = tk.Radiobutton(app, text="February", variable=radioValue, value="February")
radioThree = tk.Radiobutton(app, text="March", variable=radioValue, value="March")
radioFour = tk.Radiobutton(app, text="April", variable=radioValue, value="April")
radioFive = tk.Radiobutton(app, text="May", variable=radioValue, value="May")
radioSix = tk.Radiobutton(app, text="June", variable=radioValue, value="June")
radioSeven = tk.Radiobutton(app, text="July", variable=radioValue, value="July")
radioEight = tk.Radiobutton(app, text="August", variable=radioValue, value="August")
radioNine = tk.Radiobutton(app, text="September", variable=radioValue, value="September")
radioTen = tk.Radiobutton(app, text="October", variable=radioValue, value="October")
radioEleven = tk.Radiobutton(app, text="November", variable=radioValue, value="November")
radioTwelve = tk.Radiobutton(app, text="December", variable=radioValue, value="December")

radioOne.grid(row=0, column=0)
radioTwo.grid(row=0, column=1)
radioThree.grid(row=0, column=2)
radioFour.grid(row=1, column=0)
radioFive.grid(row=1, column=1)
radioSix.grid(row=1, column=2)
radioSeven.grid(row=2, column=0)
radioEight.grid(row=2, column=1)
radioNine.grid(row=2, column=2)
radioTen.grid(row=3, column=0)
radioEleven.grid(row=3, column=1)
radioTwelve.grid(row=3, column=2)

label = tk.Label(app, textvariable=radioValue)

label.grid(row=4, column=0, columnspan=3)

resetButton = tk.Button(app, text="Reset", command=clearInput)
resetButton.grid(row=5, column=0)

app.mainloop()

