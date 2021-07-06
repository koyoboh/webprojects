from tkinter import *
from tkinter import ttk 
import sqlite3

root =Tk()
root.geometry("550x500")
root.title("Target Heart Rate | Koyoboh Apps")
root.config(background="#2a374b")



'''
#create table
c.execute("""
		CREATE TABLE target_heart_rate(
		name text,
		age integer
		)""")
'''

#create a Frame

frame = LabelFrame (root, text='Target Heart Rate Calculator', font=(20), bg="#a9afb7", fg="#2a374b")
frame.grid(row=0, column=0, ipadx=25, ipady=35, pady=35, padx=35)


#formula to calculate Maximum heart rate
def mhr():
	
	query = 220 - int(age_entry.get())
	query2 = query * 0.5
	query3 = query * 0.7
	n = str(name_entry.get())
	#print("Hello, ", n, " , Your Maximum Heart Rate is: ", query,  str('BMP'))
	#print("50% of your THR is, ", query2, str('BMP') )
	#print("70% of your THR is, ", "{:.2f}".format(query3), str('BMP'), '\n' )

	q1 = "Hello " + n + "," +"\n" + str("Your Maximum Heart Rate is: ") + str(query) + " bpm"
	q2 = "50% of your Target Heart Rate is: " + str(query2) + " bpm"
	q3 = "70% Of your Target Heart Rate is: " + "{:.2f}".format(query3) + " bpm"
	

	result_label = Label(frame, text=q1, bg="#a9afb7", fg="#191919")
	result_label.grid(row=3, column=1, padx=10, pady=10, ipadx=10, sticky=W)
	result_label2 = Label(frame, text=q2)
	result_label2.grid(row=4, column=1, padx=10, pady=10, ipadx=10, sticky=W)
	result_label3 = Label(frame, text=q3)
	result_label3.grid(row=5, column=1, padx=10, pady=10, ipadx=10, sticky=W)


	

	



'''
#delete
def delete():
	db = sqlite3.connect("table_template.db")
	c = db.cursor()
	
	c.execute("DELETE FROM target_heart_rate WHERE oid = " + name_entry.get())
	name_entry.delete(0, END)
	
	ne_label= Label(root, text=ne)
	ne_label.grid(row=7, column=0, columnspan=2, sticky=W)

	db.commit()
	db.close()
'''
	
#save data into the taable_template database
def save():
	db = sqlite3.connect("table_template.db")
	c = db.cursor()
	
	c.execute("INSERT INTO target_heart_rate VALUES (:name, :age)",
			{
			'name': name_entry.get(),
			'age': age_entry.get()
			})

	

	#commit
	db.commit()

	#close
	db.close()
	

#reset entries
def reset():
	db =sqlite3.connect("table_template.db")
	c =db.cursor()
	

	name_entry.delete(0, END)
	age_entry.delete(0, END)
	name_entry.focus()

	db.commit()
	db.close()

#show query
def show():
	db =sqlite3.connect("table_template.db")
	c =db.cursor()
	
	c.execute("SELECT * FROM target_heart_rate ORDER BY name")
	records = c.fetchall()
	sl = ''
	for r in records:
		sl += str(r) + '\n'


	select_label = Label(frame, text=sl)
	select_label.grid(row=9, column=0, columnspan=2, sticky=EW)


	name_entry.delete(0, END)
	age_entry.delete(0, END)
	name_entry.focus()

	db.commit()
	db.close()



	

#entries

name_entry = Entry(frame, width=30, bg="#a9afb7", fg="#191919")
name_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, sticky=EW)
age_entry = Entry(frame, width=30, bg="#a9afb7", fg="#191919")
age_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, sticky=EW)

#labels
name_label = Label(frame, text='Name: ')
name_label.grid(row=0, column=0, padx=10, pady=10, ipadx=10, sticky=EW)
age_label = Label(frame, text='Age: ')
age_label.grid(row=1, column=0, padx=10, pady=10, ipadx=10, sticky=EW)
#buttons
mhr_button = Button(frame, text="Calculate Maximum Heart Rate", command=mhr, bg="#2a374b", fg="#fff")
mhr_button.grid(row=2, column=0, padx=10, pady=10, ipadx=10, sticky=EW)

query_button = Button(frame, text="Save Name/Age", command=save)
query_button.grid(row=3, column=0, padx=10, pady=10, ipadx=10, sticky=EW)


clear_button = Button(frame, text="Reset", command=reset)
clear_button.grid(row=4, column=0, padx=10, pady=10, ipadx=10, sticky=EW)


show_button = Button(frame, text="Show Entry", command=show)
show_button.grid(row=5, column=0, padx=10, pady=10, ipadx=10, sticky=EW)

quit_button = Button(frame, text="Quit App",bg="#2a374b", fg="#fff", command=lambda: root.quit())
quit_button.grid(row=10, column=0, padx=10, pady=10, ipadx=10, sticky=EW)






root.mainloop()
