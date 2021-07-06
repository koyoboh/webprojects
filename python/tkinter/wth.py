from tkinter import *
from tkinter import ttk 
import sqlite3

root =Tk()
root.geometry('750x650')
root.title("Waist To Hip Ratio Calculator | Koyoboh Apps")
#root.resizable(False,False)
root.config(background="#2c404c")


'''
c.execute("""
		CREATE TABLE waist_to_hip(
		gender,
		waist_m,
		hip_m
		)""")
'''

#creat Frame

frame = LabelFrame (root, text='Waist To Hip Ratio Calculator', font=(20), bg="#2c404c", fg="#fff")
frame.grid(row=0, column=0, ipadx=10, ipady=10, pady=10, padx=10)

def cal():

	db = sqlite3.connect("table_template.db")
	c = db.cursor()
	try:
		ge =str(gender_entry.get())
		we = float(waist_entry.get())
		he = float(hip_entry.get())
		answer1.config(text="Valid Input")
	except ValueError:
		answer1.config(text="***Please enter the right input")

	ge =str(gender_entry.get())
	we = float(waist_entry.get())
	he = float(hip_entry.get())
	formula = we/he

	r = "Your Waist to Hip ratio is: " +"{:.2f}".format(formula)
	r2 = "Gender: " + ge
	r3 = "According to the World Health Organization (WHO), a healthy WHR is:" +"\n" +"0.9 or less in men" +"\n" +"0.85 or less for women"
		
		
		
	
	'''
		WHR 'Waist to Hip Ratio' is measurement that can be used to observe your health status. \t
		WHR measures the ratio of your waist circumference to your hip circumference \t
		and indicates how much bodyfat is stored on your waist, hips, and buttocks.\t
	'''

		 
	
	
	


	

	results = Label(frame, text=r)
	results.grid(row=5, column=0, pady=10, sticky=EW)
	results = Label(frame, text=r2)
	results.grid(row=6, column=0, pady=10, sticky=EW)
	results = Label(frame, text=r3)
	results.grid(row=7, column=0, pady=10, sticky=EW)
	E


	
	
	c.execute("INSERT INTO waist_to_hip VALUES(:gender,:waist,:hip)",
			{
			'gender':gender_entry.get(),
			'waist':waist_entry.get(),
			'hip':hip_entry.get()
			})


	
	db.commit()
	db.close()
	

#query show records
def show():
	db = sqlite3.connect("table_template.db")
	c = db.cursor()
	show_records =''
	c.execute("SELECT * , oid FROM waist_to_hip ORDER BY oid DESC LIMIT 1")
	get_records = c.fetchall()
	for gr in get_records:
		show_records += str(gr) + "\n"

	show_label = Label(root, text=show_records, bg="#2c404c", fg="#fff")
	show_label.grid(row=9, column=0, pady=10)

	gender_entry.delete(0, END)
	waist_entry.delete(0, END)
	hip_entry.delete(0, END)
	gender_entry.focus()

	db.commit()
	db.close()

#create entries

gender_entry=Entry(frame, width=30)
gender_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, sticky=EW)
waist_entry=Entry(frame, width=30)
waist_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, sticky=EW)
hip_entry=Entry(frame, width=30)
hip_entry.grid(row=2, column=1, padx=10, pady=10, ipadx=10, sticky=EW)

#create label
gender_label = Label(frame, text="Gender: ", bg="#2c404c", fg="#fff")
gender_label.grid(row=0, column=0, pady=10, padx=10, sticky=W)
waist_label = Label(frame, text="Waist Measurement in cm: ", bg="#2c404c", fg="#fff")
waist_label.grid(row=1, column=0, pady=10, padx=10, sticky=W)
hip_label = Label(frame, text="Hip Measurement in cm: ", bg="#2c404c", fg="#fff")
hip_label.grid(row=2, column=0, pady=10, padx=10, sticky=W)

#create formula button

cal_button = Button(frame, text="Calculate Ratio", command=cal, bg="#2c404c", fg="#fff")
cal_button.grid(row=3, column=0, ipadx=10, padx=10, pady=10, sticky='EW')

#show records
show_button = Button(frame, text="Show Records", command=show, bg="#2c404c", fg="#fff")
show_button.grid(row=8, column=0, ipadx=10, padx=10, pady=10, sticky='EW')

#quit records
quit_button = Button(frame, text="Quit App", command=lambda: root.quit(), bg="#6b0000", fg="#fff")
quit_button.grid(row=10, column=0, ipadx=10, padx=10, pady=10, sticky='EW')

answer1 = Label (frame, text="", bg="#2c404c", fg="#fff")
answer1.grid(row=4, column=0, ipadx=10, padx=10, pady=10, sticky=EW)




root.mainloop()