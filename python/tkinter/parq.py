from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import showinfo
import sqlite3



root = Tk()
root.geometry=("400x600")
root.title('PAR Q Form')
root.config(background="#aab2b7")

#create frame
frame = LabelFrame(root, text="PAR Q Form", bg="#808c93", font=(20), fg="#fff")
frame.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10)


#create or connect to db profile

def submit():
	db =sqlite3.connect("Profile")

	#create cursor

	c = db.cursor() 
	


	c.execute(" INSERT INTO PAR_Q VALUES(:q1,:q2,:q3,:q4,:q5,:q6)",
			{
			'q1': q1.get(),
			'q2': q2.get(),
			'q3': q3.get(),
			'q4': q4.get(),
			'q5': q5.get(),
			'q6': q6.get()

			})

	c.execute("SELECT oid,* FROM PAR_Q ORDER BY oid DESC LIMIT 1")
	records = c.fetchone()
	#print(record)

	#create submit label
	paqr = ''
	thanks = ''

	#create yes button function
	def ybs1():
		yes_entry1.delete(0, END)
	def ybs2():
		yes_entry2.delete(0, END)
	def ybs3():
		yes_entry3.delete(0, END)
	def ybs4():
		yes_entry4.delete(0, END)
	def ybs5():
		yes_entry5.delete(0, END)
	def ybs6():
		yes_entry6.delete(0, END)
		
	
	

	#for loop
	for r in records:
		paqr += str(r) +"\t"
		if q1.get() == 'Yes':
			yes_entry1 = Entry(frame, width=100)
			yes_entry1.grid(row=7, column=1)

			#create label
			yes_label1 = Label(frame, text="You ansered YES to Question 1, Please provide more details: ", bg="#808c93", fg="#e9ebed")
			yes_label1.grid(row=8, column=1, padx=10, pady=10, sticky=W, columnspan=2)

			#create yes button
			yes_button_submit1 = Button(frame, text="Save records", bg="#e9ebed", fg="red")
			yes_button_submit1.grid(row=8, column=0, sticky=EW)



		if q2.get() == 'Yes':
			yes_entry2 = Entry(frame, width=100)
			yes_entry2.grid(row=9, column=1)

			#create label
			yes_label2 = Label(frame, text="You ansered YES to Question 2, Please provide more details: ", bg="#808c93", fg="#e9ebed")
			yes_label2.grid(row=10, column=1, padx=10, pady=10, sticky=W, columnspan=2)

			#create yes button
			yes_button_submit2 = Button(frame, text="Save records",command=ybs2, bg="#e9ebed", fg="red" )
			yes_button_submit2.grid(row=10, column=0, sticky=EW)



		if q3.get() == 'Yes':
			yes_entry3 = Entry(frame, width=100)
			yes_entry3.grid(row=11, column=1)

			#create label
			yes_label3 = Label(frame, text="You ansered YES to Question 3, Please list medications: ", bg="#808c93", fg="#e9ebed")
			yes_label3.grid(row=12, column=1, padx=10, pady=10, sticky=W, columnspan=2)

			#create yes button
			yes_button_submit3 = Button(frame, text="Save records",command=ybs3, bg="#e9ebed", fg="red")
			yes_button_submit3.grid(row=12, column=0, sticky=EW)

		if q4.get() == 'Yes':
			yes_entry4 = Entry(frame, width=100)
			yes_entry4.grid(row=13, column=1)

			#create label
			yes_label4 = Label(frame, text="You ansered YES to Question 4, Please provide more details: ",  bg="#808c93", fg="#e9ebed")
			yes_label4.grid(row=14, column=1, padx=10, pady=10, sticky=W, columnspan=2)

			#create yes button
			yes_button_submit4 = Button(frame, text="Save records",command=ybs4, bg="#e9ebed", fg="red")
			yes_button_submit4.grid(row=14, column=0, sticky=EW)

		if q5.get() == 'Yes':
			yes_entry5 = Entry(frame, width=100)
			yes_entry5.grid(row=15, column=1)

			#create label
			yes_label5 = Label(frame, text="You ansered YES to Question 5, Please state trimester?: ", bg="#808c93", fg="#e9ebed")
			yes_label5.grid(row=16, column=1, padx=10, pady=10, sticky=W, columnspan=2)

			#create yes button
			yes_button_submit5 = Button(frame, text="Save records",command=ybs5, bg="#e9ebed", fg="red")
			yes_button_submit5.grid(row=16, column=0, sticky=EW)

		if q6.get() == 'Yes':
			yes_entry6 = Entry(frame, width=100)
			yes_entry6.grid(row=17, column=1)

			#create label
			yes_label6 = Label(frame, text="You ansered YES to Question 6, Please provide more details: ", bg="#808c93", fg="#e9ebed")
			yes_label6.grid(row=18, column=1, padx=10, pady=10, sticky=W, columnspan=2)

			#create yes button
			yes_button_submit6 = Button(frame, text="Save records",command=ybs6,  bg="#e9ebed", fg="red",)
			yes_button_submit6.grid(row=18, column=0, sticky=EW)
		else:
			thanks ='Thank you!'
			




	submit_label =Label(frame, text=paqr,  bg="#808c93", fg="#fff")
	submit_label.grid(padx=10, pady=10)

	submit_label2 =Label(frame, text=thanks, bg="#808c93", fg="#fff")
	submit_label2.grid(padx=10, pady=10)


	#commit
	db.commit()

	#close
	db.close()

	q1.delete(0, END)
	q2.delete(0, END)
	q3.delete(0, END)
	q4.delete(0, END)
	q5.delete(0, END)
	q6.delete(0, END)
	q1.focus()

	#insert questions
	#q1.insert(0, q1.get())

	



'''
#create table
c.execute("""CREATE TABLE PAR_Q(
		q1 text,
		q2 text,
		q3 text,
		q4 text,
		q5 text,
		q6 text
		)""")
'''




#create questionnaire
q1 = Entry(frame, width=5)
q1.grid(row=0, column=1, padx=10, pady=10)

q2 = Entry(frame, width=5)
q2.grid(row=1, column=1, padx=10, pady=10)

q3 = Entry(frame, width=5)
q3.grid(row=2, column=1, padx=10, pady=10)

q4 = Entry(frame, width=5)
q4.grid(row=3, column=1, padx=10, pady=10)

q5 = Entry(frame, width=5)
q5.grid(row=4, column=1, padx=10, pady=10)

q6 = Entry(frame, width=5)
q6.grid(row=5, column=1, padx=10, pady=10)



#create label
q1_label = Label(frame, text="1: Has your doctor diagnosed you with a heart disease? YES/NO", bg="#808c93", fg="#e9ebed", font=(12))
q1_label.grid(row=0, column=0, sticky=W)

q2_label = Label(frame, text="2: Do you ever faint or have dizzy spells? YES/NO", bg="#808c93", fg="#e9ebed", font=(12))
q2_label.grid(row=1, column=0, sticky=W)

q3_label = Label(frame, text="3: Do you take any medications? YES/NO", bg="#808c93", fg="#e9ebed", font=(12))
q3_label.grid(row=2, column=0, sticky=W)

q4_label = Label(frame, text="4: Do you suffer from any bone, muscle or joint pains? YES/NO", bg="#808c93", fg="#e9ebed", font=(12))
q4_label.grid(row=3, column=0, sticky=W)

q5_label = Label(frame, text="5: Are you pregnant or have you given birth in the last 6 months? YES/NO", bg="#808c93", fg="#e9ebed", font=(12))
q5_label.grid(row=4, column=0, sticky=W)

q6_label = Label(frame, text="6: Do you know any reason you shouldn't participate in physical exercise? YES/NO", bg="#808c93", fg="#e9ebed", font=(12))
q6_label.grid(row=5, column=0, sticky=W)


submit_button = Button(frame, text="Submit", command=submit, bg="#808c93", fg="#e9ebed", font=(12))
submit_button.grid(row=6, column=0, sticky=EW)

#create reset
q_button = Button(frame, text="Quit App", command=lambda: root.quit(), bg="#fff", fg="#808c93", font=(12))
q_button.grid(row=19, column=0, sticky=EW)



root.mainloop()