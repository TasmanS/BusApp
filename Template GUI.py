import tkinter as tk

def main():
    frame = tk.Tk()
    
    frame.geometry("480x360")

    bus1=tk.Label(frame, text="5 min").grid(row=1, column=1,
                    sticky="NESW")

    bus2=tk.Label(frame, text="10 min").grid(row=1, column=2,
                    sticky="NESW")
              
    bus3=tk.Label(frame, text="15 min").grid(row=2, column=2,
                    sticky="NESW")
    
main()


## Grid may be too limiting for application. Now that I understand the
## geometry function, place and center may be more useful. Still need to
## figure out how to adjust font sizes, or alternativetly check out another
## module that allows me to change the font, I would think it exists somewhere




## What follows below are the directions on how to update the Label within the GUI
## which will be used later, in conjunction with datetime to auto-update the app

 

##Sure you can! Just add another label to the frame, and update the text attribute whenever one of your add functions is called. Also, you can simplify that code, using one add function for all the different amounts.
##
##def main():
##    frame = Tk()
##    frame.geometry("480x360")
##
##    Label(frame, text="Enter coins.[Press Buttons]").grid(row=1, column=1)
##    display = Label(frame, text="") # we need this Label as a variable!
##    display.grid(row=2, column=1)
##
##    def add(amount):
##        global credit
##        credit += amount
##        display.configure(text="%.2f" % credit)
##
##    Button(frame, text="10p", command=lambda: add(.1)).grid(row=3, column=1)
##    Button(frame, text="20p", command=lambda: add(.2)).grid(row=4, column=1)
##    Button(frame, text="50p", command=lambda: add(.5)).grid(row=5, column=1)
##    Button(frame, text="P1",  command=lambda: add(1.)).grid(row=6, column=1)
##    frame.mainloop()

##main()
