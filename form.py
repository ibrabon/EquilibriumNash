import tkinter as tk

import calculations as calc


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.rqText = tk.StringVar()
        self.rgLabel = tk.Label(self, text="r^g").pack()
        self.rqEntry = tk.Entry(self, textvariable=self.rqText).pack()


        self.rpText = tk.StringVar()
        self.rpLabel = tk.Label(self, text="r^p").pack()
        self.rpEntry = tk.Entry(self, textvariable=self.rpText).pack()

        self.okButton = tk.Button(self, text="Calculate", command=self.calculate).pack(side="top")

    def calculate(self):
        amount = self.rpText.get()
        return calc.Equilibrium().makeStep(amount)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
