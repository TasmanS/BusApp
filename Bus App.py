import urllib.request
import xml.etree.ElementTree as ET
import tkinter as tk

class busSchedule(dict):
    def __init__(self):
        dict.__init__(self)
        self.schedule=("bus","Douglass and 24th","To Mission")

        def checkRoute(bus, stop, direction):

       
            z=urllib.request.urlopen("http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token=1c4f133b-4036-4b61-a5ce-e3b24b651047&stopcode=14443")
            try: data=z.read()
            except:
                ["no bus", "no bus", "no bus"]
            f=open("rt22.xml", "wb")
            f.write(data)
            f.close()
            schedule=[]
            doc=ET.parse("rt22.xml")
            stopschedule=doc.getroot()
            key={1:"first",2:"second",3:"third"}
            counter=1
    
            for entry in stopschedule.iter("DepartureTime"):
                schedule+=[(key[counter] + " bus in " + entry.text + "m")]
                counter+=1
            if len(schedule)==0:
                return ["no bus", "no bus", "no bus"]
            return(schedule)



class Application():
    def __init__(self, master):
        self.master = tk.Tk()
        self.w = tk.Canvas(self.master, width=1000, height=500)
        self.w.pack()
        self.w.create_rectangle(0, 0, 700, 200, fill="black", width=10)
        self.w.create_rectangle(100, 200, 1000, 400, fill="red", width=10)
        self.w.create_rectangle(800, 400, 500,0, fill="blue", width=10)



        self.master.update()


##    def createWidgets(self):
##        self.hi_there = tk.Button(self)
##        self.hi_there["text"] = "\n Bus Schedule\n \n (click to update me)\n"
##        self.hi_there["command"] = self.say_hi
##        self.hi_there.pack(side="top")
##
##        self.QUIT = tk.Button(self, text="QUIT", fg="red",
##                                            command=root.destroy)
##        self.QUIT.pack(side="bottom")
##
##    def say_hi(self):
##        for item in fortyEight.schedule:
##            print(item)

fortyEight={}
fortyEight=busSchedule()
root=tk.Frame
app = Application(root)



