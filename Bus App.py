import urllib.request
import xml.etree.ElementTree as ET
import tkinter as tk
import time


class busSchedule():
    def __init__(self):
        self.schedule=[]

    def checkRoute(self):

        self.schedule=[]
       
        z=urllib.request.urlopen("http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token=1c4f133b-4036-4b61-a5ce-e3b24b651047&stopcode=14443")
        try: data=z.read()
        except:
            return ["-","-","-"]
        
        f=open("rt22.xml", "wb")
        f.write(data)
        f.close()

        doc=ET.parse("rt22.xml")
        stopschedule=doc.getroot()

        for entry in stopschedule.iter("DepartureTime"):
            self.schedule+=[entry.text]
            
        while len(self.schedule)<3:
            self.schedule+=["-"]
        
        print(self.schedule)
        return(self.schedule)



class Application():
    def __init__(self):
        self.w = tk.Canvas(width=1000, height=500)
        self.w.pack()
        self.w.create_rectangle(25,15,535,485, fill="dim gray", width=10)
        self.w.create_rectangle(555,15,975,240, fill="dim gray", width=10)
        self.w.create_rectangle(555,260,975,485, fill="dim gray", width=10)


    def popItems(self,schedule):
        self.t1=self.w.create_text(275,250, fill="white", font=("helvetica",250),
                           justify="center", text=schedule[0])
        self.t2=self.w.create_text(770,130, fill="white", font=("helvetica",125),
                           justify="center", text=schedule[1])     
        self.t3=self.w.create_text(770,375, fill="white", font=("helvetica",125),
                           justify="center", text=schedule[2])


    def updateItems(self,busobject):
        latestRoute=busobject.checkRoute()
        self.w.itemconfig(self.t1,text=latestRoute[0])
        self.w.itemconfig(self.t2,text=latestRoute[1])
        self.w.itemconfig(self.t3,text=latestRoute[2])
        self.w.update()
        time.sleep(1)
        self.updateItems(busobject)
        


fortyEight=busSchedule()
app = Application()
app.popItems(fortyEight.checkRoute())
app.updateItems(fortyEight)









