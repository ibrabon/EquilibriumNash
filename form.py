import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.rgLabel = tk.Label(self, text="r^g").pack()
        self.rqText = tk.Text(self, height=1, width=20).pack()

        self.rpLabel = tk.Label(self, text="r^p").pack()
        self.rpText = tk.Text(self, height=1, width=20).pack()

        self.okButton = tk.Button(self, text="Calculate", command=root.destroy).pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
