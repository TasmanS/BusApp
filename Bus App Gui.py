import urllib.request
import xml.etree.ElementTree as ET
import tkinter as tk

def checkRoute(bus, stop, direction):

   
    z=urllib.request.urlopen("http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token=1c4f133b-4036-4b61-a5ce-e3b24b651047&stopcode=14443")
    data=z.read()
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


class busSchedule(dict):
    def __init__(self):
        dict.__init__(self)
        self.schedule=(checkRoute(48,"Douglass and 24th","to Mission"))
        self.bus="48"
        self.stop="Douglass and 24th"
        self.direction="to Mission"



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

        self.busstopid=tk.Label(master)
        self.bustopid.pack()
    

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "\n 48 Bus Schedule\n \n (click to update)\n"
        self.hi_there["command"] = self.updateRoute
        

        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
                   
        
        self.QUIT.pack(side="bottom")

    def updateRoute(self):
            fortyEight=busSchedule()
            print("\n" + fortyEight.bus + " bus" + " at " + fortyEight.stop + " going " + fortyEight.direction)
            for item in fortyEight.schedule:
                print(item)
            

fortyEight={}
root = tk.Tk()
app = Application(master=root)
app.master.title("Bus App")
app.mainloop()
