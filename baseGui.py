from tkinter import *
from tkinter import ttk
import time
import threading
import browserhistory as bh
import win32gui

#TODO:LOCK Options, Counter Display, Email, Grace Period, Ensure time intervals work, Weekend check,

starttime = time.time()
timeLowerDefault = 9
timeUpperDefault = 17
row = 0
secs = 0
trackBoolean = FALSE
lastVisited = ""
websiteList = [{"website":"Facebook", "lower":9, "upper":17, "count": 0},
               {"website":"Gmail" , "lower":9, "upper":17 , "count": 0},
               {"website":"Youtube" , "lower":9, "upper":17 , "count": 0},
               {"website":"Twitter" , "lower":9, "upper":17 , "count": 0}]
base_gui = Tk()


def startTracker(base):
    global trackBoolean
    global starttime
    starttime = time.time()
    trackBoolean = True

    thread = threading.Thread(target=tracker(base))
    thread.start()


def tracker(base):
    global websiteList
    global starttime
    global lastVisited
    global trackBoolean
    global  base_gui
    currenttime = time.time()
    # time.sleep(0.1)
    if currenttime - starttime > 2:
        starttime = currenttime
        # dict_obj = bh.get_browserhistory()
        # dict_obj.keys()
        w = win32gui
        fgWindow = w.GetForegroundWindow()
        data = w.GetWindowText(fgWindow)

        if(data != lastVisited ):
            # print("w")
            # print(w)
            print(data)
            print("Tracker")
            lastVisited = data
            parse = data.split("-")
            if(len(parse) >1):
                for i in range(len(websiteList)):
                    if websiteList[i]["website"] in parse[len(parse) - 2]:
                        print(parse[len(parse) - 2])
                        websiteList[i]["count"] +=1
                        print(websiteList[i]["count"])
    if(trackBoolean):
        base_gui.after(1000,tracker, base)

def stopTracker():
    global  trackBoolean
    trackBoolean = False
    print("Ending Tracking")

def removeWebsiteEntryFrame (newFrame, currentRow):
    print(newFrame)
    print(currentRow)
    # Figure out how to delete row
    newFrame.grid_remove()


def addWebsiteEntryFrame(newFrame, base, websiteNameF, timeSelectLower, timeSelectUpper):
    global websiteList
    item = {
        "website": websiteNameF,
        "lower": timeSelectLower,
        "upper": timeSelectUpper
    }
    websiteList.append(item)
    print(websiteList)
    createWebsiteEntryFrame(newFrame, base, websiteNameF, timeSelectLower, timeSelectUpper)

def createWebsiteEntryFrame (newFrame, base, websiteNameF, timeSelectLower, timeSelectUpper):
    global row
    currentRow = row
    setDefaultWebsiteLabel = Label(newFrame, text=websiteNameF+":", fg="white", font="Verdana 10 bold",
                                bg=applicationBackground).grid(row=row, column=0, padx=40, sticky=W)
    setDefaultTimeLabel2 = Label(newFrame, text='-', fg="white", font="Verdana 10 bold",
                                 bg=applicationBackground).grid(row=row, column=2, )

    timeSelectWeb = ttk.Combobox(newFrame, values=timeListVariable, width=5)
    timeSelectWeb.current(timeSelectLower)
    timeSelectWeb.grid(row=row, column=1, padx=10)
    timeSelectWeb2 = ttk.Combobox(newFrame, values=timeListVariable, width=5)
    timeSelectWeb2.current(timeSelectUpper)
    timeSelectWeb2.grid(row=row, column=3, padx=10)
    addButton = Button(newFrame,
                       command=lambda: removeWebsiteEntryFrame(newFrame, currentRow),
                       activebackground=applicationBackground, image=loadimage, border=0, bg=applicationBackground,
                       width=15, height=15)
    # addButton.grid(row=row, column=4, padx=10)

    row = row + 1

def setValue(value):
    print(value)




applicationName = "Watcher"
applicationBackground = "#373d57"
print(applicationName)
# root
base_gui.geometry("600x600")
base_gui.configure(background=applicationBackground)


# Canvas Init
base_gui.title(applicationName)
mainLogo = Canvas(base_gui, width=375, height=75, borderwidth=5, relief="ridge")
mainLogo.pack(pady=15)
mainLogo.create_text(200, 40, fill="darkblue",font="Verdana 30 bold", text=applicationName)

# Frame for Email Entry
frameEmails = Frame(base_gui, width=400, height=100, bg=applicationBackground)
frameEmails.pack()

# Frame email fields
userLabel = Label(frameEmails, text='User Email', fg="white",font="Verdana 10 bold", bg=applicationBackground).grid(row=0, column=0)
refereeLabel = Label(frameEmails, text='Referee Email', fg="white",font="Verdana 10 bold", bg=applicationBackground).grid(row=1, column=0)
userEntry = Entry(frameEmails).grid(row=0, column=1)
refereeEntry = Entry(frameEmails).grid(row=1, column=1)

print(userEntry)

# Frame to set default time
frameTimeSet = Frame(base_gui, width=400, height=150, bg=applicationBackground)
frameTimeSet.pack(pady= 10)
timeListVariable = ["12 am", "1 am", "2 am", "3 am", "4 am", "5 am", "6 am", "7 am", "8 am", "9 am", "10 am", "11 am", "12 pm",
                    "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm", "10 pm", "11 pm", ]

setDefaultTimeLabel = Label(frameTimeSet, text='Default Time Window', fg="white",font="Verdana 10 bold", bg=applicationBackground).grid(row=0, column=0)
setDefaultTimeLabel2 = Label(frameTimeSet, text='-', fg="white",font="Verdana 10 bold", bg=applicationBackground).grid(row=0, column=2)

timeSelect = ttk.Combobox(frameTimeSet, values=timeListVariable, width=5)
timeSelect.current(timeLowerDefault)
timeSelect.grid(row=0,column=1, padx=10)

timeSelect2 = ttk.Combobox(frameTimeSet, values=timeListVariable, width=5)
timeSelect2.current(timeUpperDefault)
timeSelect2.grid(row=0,column=3, padx=10)

# Frame to display monitored websites
# websiteList = ['Facebook', 'Gmail', 'Youtube', 'Twitter']
middleFrame = Frame(base_gui, width=400, height=150, bg=applicationBackground)
middleFrame.pack();
websiteFrame = Frame(middleFrame, width=400, height=150, bg=applicationBackground)
websiteFrame.pack(fill=BOTH, )


addWebsiteOptionFrame = Frame(middleFrame, width=400, height=100, bg=applicationBackground, borderwidth=1,relief="groove")
addWebsiteOptionFrame.pack(side=BOTTOM, pady= 10)


addLabel = Label(Label(addWebsiteOptionFrame, text="Add Another Website:", fg="white", font="Verdana 10 bold",
                       bg=applicationBackground).grid(row=0, column=0, padx=10, sticky=W))
addEntry = Entry(addWebsiteOptionFrame)
addEntry.grid(row=1, column=0,  padx=40, sticky=W)
addTimeSelect = ttk.Combobox(addWebsiteOptionFrame, values=timeListVariable, width=5)
addTimeSelect.current(timeLowerDefault)
addTimeSelect.grid(row=1,column=1, padx=10)

setDefaultTimeLabel2 = Label(addWebsiteOptionFrame, text='-', fg="white",font="Verdana 10 bold",
                             bg=applicationBackground).grid(row=1, column=2)

addTimeSelect2 = ttk.Combobox(addWebsiteOptionFrame, values=timeListVariable, width=5)
addTimeSelect2.current(timeUpperDefault)
addTimeSelect2.grid(row=1,column=3, padx=10)
loadimage = PhotoImage(file="resources/+button.png")

addButton = Button(addWebsiteOptionFrame, command=lambda : addWebsiteEntryFrame(websiteFrame, base_gui, addEntry.get(), addTimeSelect.current(), addTimeSelect2.current()),
                   activebackground= applicationBackground, image=loadimage, border=0, bg=applicationBackground,  width = 15, height= 15)
addButton.grid(row=1, column=4, padx=10)
col = 0
while col < 4:
    websiteFrame.columnconfigure(col, weight=1)
    addWebsiteOptionFrame.columnconfigure(col, weight=1)
    col = col + 1
for name in websiteList:
    createWebsiteEntryFrame(websiteFrame, base_gui, name["website"], timeSelect.current(), timeSelect2.current())

# bottomFrame = Frame(base_gui, bg=applicationBackground)
# bottomFrame.pack(side=BOTTOM)
stopButton = Button(base_gui, command=lambda : stopTracker(),
                   activebackground= applicationBackground, text="stop", border=0, bg=applicationBackground, fg ="white", font="Verdana 20 bold")
stopButton.pack(side=BOTTOM, pady=20)
submitButton = Button(base_gui, command=lambda : startTracker(base_gui),
                   activebackground= applicationBackground, text="start", border=0, bg=applicationBackground, fg ="white", font="Verdana 20 bold")
submitButton.pack(side=BOTTOM, pady=20)

base_gui.mainloop()


# Frame for Websites Selection
# Consists of Website Name # of max visits and timeFrame




#
# # Frame Container
# frameTest = tk.Frame(base_gui, width=375, height=115, bg="yellow")
# frameTest.pack()
#
# bottomframe = tk.Frame(base_gui,  bg="blue")
# bottomframe.pack(side=tk.BOTTOM)
#
#
# # Button Formatting
# buttonTest = tk.Button(bottomframe, command=setValue(), text="TestValue")
# buttonTest.pack()
#
# # Radio Button Formatting
# checkButtonTest = tk.Checkbutton(bottomframe, command=setValue(), text="Check")
# checkButtonTest.pack()
#
# # Text Entry Field
# labelTest = tk.Label(frameTest, text='FieldName')
# entryTest = tk.Entry(frameTest)
#
# labelTest.pack()
# entryTest.pack()
#









