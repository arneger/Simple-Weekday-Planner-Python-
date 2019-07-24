from tkinter import *
import json

#Dictionary that's used to save the json object for the program
weekdays = {"monday": "",
            "tuesday": "",
            "wednesday": "",
            "thursday": "",
            "friday": "",
            "saturday": "",
            "sunday": ""}

#Function that clears the text entries and loads the string information from the json file
#into the text entries.
def gather():
    monday_text.delete(0.0, END)
    tuesday_text.delete(0.0, END)
    wednesday_text.delete(0.0, END)
    thursday_text.delete(0.0, END)
    friday_text.delete(0.0, END)
    saturday_text.delete(0.0, END)
    sunday_text.delete(0.0, END)
    plan_saved = json.load(open("my_plan.json", "r"))
    for key, value in plan_saved.items():
        weekdays[key] = value
    mon = weekdays["monday"]
    tue = weekdays["tuesday"]
    wed = weekdays["wednesday"]
    thu = weekdays["thursday"]
    fri = weekdays["friday"]
    sat = weekdays["saturday"]
    sun = weekdays["sunday"]
    monday_text.insert(END, mon)
    tuesday_text.insert(END, tue)
    wednesday_text.insert(END, wed)
    thursday_text.insert(END, thu)
    friday_text.insert(END, fri)
    saturday_text.insert(END, sat)
    sunday_text.insert(END, sun)

#Function that saves the information from the text entries and saves it to the json file
def sav():
    mon = monday_text.get("1.0", "end-1c")
    tue = tuesday_text.get("1.0", "end-1c")
    wed = wednesday_text.get("1.0", "end-1c")
    thu = thursday_text.get("1.0", "end-1c")
    fri = friday_text.get("1.0", "end-1c")
    sat = saturday_text.get("1.0", "end-1c")
    sun = sunday_text.get("1.0", "end-1c")
    weekdays["monday"] = mon
    weekdays["tuesday"] = tue
    weekdays["wednesday"] = wed
    weekdays["thursday"] = thu
    weekdays["friday"] = fri
    weekdays["saturday"] = sat
    weekdays["sunday"] = sun
    with open("my_plan.json", "w") as file:
        file.write(json.dumps(weekdays))

window = Tk()
window.title("Week Planner")
C = Canvas(bg="blue", height=250, width=300)
filename = PhotoImage(file = "house.gif")
background_label = Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Top header
Label (window, text="Week Planner", bg="white", fg="black", font="none 24 bold") .grid(row=0, column=2, sticky=W)

#The below is weekday headers and Text entry boxes
Label (window, text="Monday", bg="white", fg="black", font="none 16") .grid(row=1, column=0)
monday_text = Text(window, width=80, height=6, wrap=WORD, background='azure', fg="black")
monday_text.grid(row=1, column=1, columnspan=2, sticky=W)

Label (window, text="Tuesday", bg="white", fg="black", font="none 16") .grid(row=2, column=0)
tuesday_text = Text(window, width=80, height=6, wrap=WORD, background='alice blue')
tuesday_text.grid(row=2, column=1, columnspan=2, sticky=W)

Label (window, text="Wednesday", bg="white", fg="black", font="none 16") .grid(row=3, column=0)
wednesday_text = Text(window, width=80, height=6, wrap=WORD, background='azure')
wednesday_text.grid(row=3, column=1, columnspan=2, sticky=W)

Label (window, text="Thursday", bg="white", fg="black", font="none 16") .grid(row=4, column=0)
thursday_text = Text(window, width=80, height=6, wrap=WORD, background='alice blue')
thursday_text.grid(row=4, column=1, columnspan=2, sticky=W)

Label (window, text="Friday", bg="white", fg="black", font="none 16") .grid(row=5, column=0)
friday_text = Text(window, width=80, height=6, wrap=WORD, background='azure')
friday_text.grid(row=5, column=1, columnspan=2, sticky=W)

Label (window, text="Saturday", bg="white", fg="black", font="none 16") .grid(row=6, column=0)
saturday_text = Text(window, width=80, height=6, wrap=WORD, background='alice blue')
saturday_text.grid(row=6, column=1, columnspan=2, sticky=W)

Label (window, text="Sunday", bg="white", fg="black", font="none 16") .grid(row=7, column=0)
sunday_text = Text(window, width=80, height=6, wrap=WORD, background='azure')
sunday_text.grid(row=7, column=1, columnspan=2, sticky=W)

#Save button
Button(window, text="Save plan", width=10, bg="lightblue3", fg="black",command=sav) .grid(row=9, column=0)
#Load button
Button(window, text="Load plan", width=10, bg="lightblue3", fg="black",command=gather) .grid(row=0, column=0)

window.mainloop()
