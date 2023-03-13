from tkinter import *
from tkinter import ttk
import tkinter.font as font
import main
from tkinter import messagebox
from datetime import datetime

app = Tk()

app.title("Gerrit pipeline")
app.geometry("1800x500")
# app.configure(bg='white')

#Create button function
def b_uppdate_click():
    #Function for b_uppdate
    after_date = time_from.get()
    before_date = time_to.get()
    try:
        datetime.strptime(after_date, "%Y-%m-%d")
        datetime.strptime(before_date, "%Y-%m-%d")
        main.get_code_review(after_date,before_date)
    except ValueError:
        #Wrong input
        messagebox.showinfo("Error", "The date is not in the correct format (YYYY-MM-DD)")

def b_show_click():
    #Function for b_show
    table_result.delete(*table_result.get_children()) #Clear result table
    result = main.process_json_function()
    if result == {}:
            messagebox.showinfo("No results were found", "No results were found")
    else:
        for i in range(len(result["updated"])):
            Owner = result['owner'][i]['_account_id']
            Branch = result["branch"][i]
            Project = result["project"][i]
            LastUpdate = result["updated"][i][:-10]
            Status = result["status"][i]
            ID = result["id"][i]
            data = (Owner, Branch, Project, LastUpdate, Status, ID)
            table_result.insert(parent= '', index = 0, values = data)
    

def b_export_click():
    #Function for b_export
    main.export_pdf()

#Create button
b_uppdate = Button(app, text="Updates", command = b_uppdate_click)
b_uppdate['font'] = font.Font(size=15)
b_uppdate.place(x=20,y=400)

b_show = Button(app, text="Show results", command = b_show_click)
b_show['font'] = font.Font(size=15)
b_show.place(x=10,y=50)

b_export = Button(app, text="Export Plot as PDF", command = b_export_click)
b_export['font'] = font.Font(size=15)
b_export.place(x=700,y=400)


text3 = Label(app, text = "Result:")
text3.place(x=150, y=50)
text3['font'] = font.Font(size=15)

#Create a box that shows results
table_result = ttk.Treeview(app,columns=('Owner', 'Branch', 'Project', 'LastUpdate', 'Status', 'ID'), show ='headings')
table_result.heading('Owner', text="Owner ID")
table_result.heading('Branch', text="Branch")
table_result.heading('Project', text="Project")
table_result.heading('LastUpdate', text="Last Update")
table_result.heading('Status', text="Status")
table_result.heading('ID', text="ID")
table_result.place(x=150, y= 80)
table_result.column("#1", width=80)
table_result.column("#2", width=200)
table_result.column("#3", width=460)
table_result.column("#4", width=150)
table_result.column("#5", width=100)
table_result.column("#6", width=600)

#Time filter box
time_frame = LabelFrame(app, text="Last updated")
time_frame.pack()
time_frame.place(x=190, y=370)

text1 = Label(time_frame, text = "After:")
text1.place(x=10, y=5)
text1['font'] = font.Font(size=13)

text2 = Label(time_frame, text = "Before:")
text2.place(x=140, y=5)
text2['font'] = font.Font(size=13)

title = Label(app, text = "Android Code Reviews")
title.place(x=750, y=5)
title['font'] = font.Font(size=23)

time_from = Entry(time_frame, width=10)
time_from.pack(side=LEFT, padx= 10,pady= 30)
time_from['font'] = font.Font(size=15)
time_from.insert(0, "2023-02-27")

time_to= Entry(time_frame, width=10)
time_to.pack(side=RIGHT, padx= 10,pady= 10)
time_to['font'] = font.Font(size=15)
time_to.insert(0, "2023-02-28")




app.mainloop()