import urllib.request
import xml.etree.ElementTree as ET
import tkinter as tk

class busSchedule():
    def __init__(self):
        self.schedule=["--","--","--"]

    def checkRoute(self):
       
        z=urllib.request.urlopen("http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token=1c4f133b-4036-4b61-a5ce-e3b24b651047&stopcode=14443")
        try: data=z.read()
        except:
            return ["--","--","--"]
        
        f=open("rt22.xml", "wb")
        f.write(data)
        f.close()

        doc=ET.parse("rt22.xml")
        stopschedule=doc.getroot()

        schedule=[]
        for entry in stopschedule.iter("DepartureTime"):
            schedule+=[entry.text]
            
        if len(schedule)==0:
            return ["--","--","--"]
        
        print(schedule)
        return(schedule)



class Application():
    def __init__(self):
        self.w = tk.Canvas(width=1000, height=500)
        self.w.pack()
        self.w.create_rectangle(25,15,535,485, fill="dim gray", width=10)
        self.w.create_rectangle(555,15,975,240, fill="dim gray", width=10)
        self.w.create_rectangle(555,260,975,485, fill="dim gray", width=10)

    def popItems(self,schedule):
        self.w.create_text(270,250, fill="white", font=("helvetica",250),
                           justify="center", text=schedule[0])
        self.w.create_text(765,130, fill="white", font=("helvetica",125),
                           justify="center", text=schedule[1])     
        self.w.create_text(765,375, fill="white", font=("helvetica",125),
                           justify="center", text=schedule[2])


fortyEight=busSchedule()
app = Application()
app.popItems(fortyEight.checkRoute())




