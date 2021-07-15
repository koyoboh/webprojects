from tkinter import *
from tkinter import ttk 
import sqlite3


root=Tk()
root.geometry('500x500')
#root.resizable(False,False)
root.title("Your Profile")
root.config(background="#355c7d")
'''
c.execute("""
	CREATE TABLE bmi(
	name text,
	weight real,
	height real
	)""")

'''




global w
global h 
global n


#entry name:
n=Entry(root, width=100, borderwidth=12, )
n.pack(pady=20)
n.insert(0, "What is your name? : ")
n.focus()


#entry weight
w=Entry(root, width=100, borderwidth=12, )
w.pack(pady=20)
w.insert(0, "Enter Your Weight In Kg: ")
w.focus()


#entry height
h=Entry(root, width=100, borderwidth=12, )
h.pack(pady=20)
h.insert(0, "Enter Your Height In Meters: ")


#frame
frame = LabelFrame(root, text="BMI Calculator", padx=10, pady=10)
frame.pack(pady=5, padx=5)

#func
def bmi():
	db = sqlite3.connect("Profile.db")
	c = db.cursor()
	try:
		getN = str(n.get())
		getW = float(w.get())
		getH = float(h.get())
		calBmi = getW / (getH*getH)
		result = round(calBmi)
		n.focus()
	except ValueError:
		
	  
		w.insert(0, "*Wrong Input ")
		h.insert(0, "*Wrong Input ")
		n.insert(0, "*Wrong Input ")


		
	
	if calBmi < 18.5:
		label=Label(frame, text=f"You are Underweight with a BMI of {result}").pack(pady=10)
	elif calBmi >25:
		label=Label(frame, text=f"You are Overweight! with a BMI of {result}").pack(pady=10)
	else:
		label=Label(frame, text= f"You are Healthy! with a BMI of  {result}").pack(pady=10)
	label =Label(frame, text=f"Thank you, {getN}").pack(pady=10)






	db.commit()
	db.close()




def delete():
	n.delete(0)
	h.delete(0)
	w.delete(0)

def reset():

	n.delete(0, END)
	w.delete(0, END)
	h.delete(0, END)
	
	w.insert(0, "Please Enter Weight In Kgs: ")
	h.insert(0, "Please Enter Height In Meters: ")
	n.insert(0, "Please Enter Your Name Again: ")

	db = sqlite3.connect("Profile.db")
	c = db.cursor()
	try:
		c.execute("DELETE FROM bmi WHERE oid = 1")
		answer.config(text="**Record Deleted**")
	except ValueError:
		answer.config(text="Not Deleted")


	db.commit()
	db.close()

	n.focus()
	


def save():
	db = sqlite3.connect("Profile.db")
	c = db.cursor()
	c.execute("INSERT INTO bmi VALUES(:name, :weight ,:height)",
					{
					'name': n.get(),
					'weight':w.get(),
					'height':h.get()
					})

	c.execute("SELECT * ,oid  FROM bmi ORDER BY oid DESC LIMIT 1")
	showD=''


	show_data = c.fetchall()
	for s in show_data:
		showD = str(s) + "\t"


	data_label = Label(frame, text=showD, pady=5, padx=5)
	data_label.pack(pady=10, expand=True, fill='x')

	n.delete(0, END)
	w.delete(0, END)
	h.delete(0, END)

	
	db.commit()
	db.close()

	#s = e.get()
	#e.insert(0, str(v) + 'Enter Name: ')
	#e.delete(0, END)
	
	




#forBim



#button
b1= Button(frame, text="Calculate BMI ", padx=30, pady=20, bg="#e84a5f", fg="#f2f2f2" ,command=bmi)
b2= Button(frame, text="Delete ",padx=30, pady=20, command=delete)
b3= Button (frame, text="Reset ",padx=30, pady=20, command=reset)
b4= Button(frame, text="Save BMI Results ", padx=30, pady=20,command=save)
b5= Button(frame, text="Exit App ", padx=30, pady=20,command=lambda: root.quit())
#packs
b1.pack(pady=10, expand=True, fill='x', side=LEFT)
b2.pack(pady=10,expand=True, fill='x', side=LEFT)
b3.pack(pady=10,expand=True, fill='x', side=LEFT)
b4.pack(pady=10,expand=True, fill='x', side=LEFT)
b5.pack(pady=10,expand=True, fill='x', side=LEFT)


#label
f = Label(frame, text="Your Profile", pady=20, padx=30)
f.pack(pady=20)

#answer label
answer = Label(frame, text="")
answer.pack(pady=20)




root.mainloop()

