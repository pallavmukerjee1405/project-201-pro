from tkinter import *
window=Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg="orange")

def calculate_interest():
    p=float(principal.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)

    result_label.destroy()

    output_message=Label(result_frame,text="Interest on Rs."+str(p)+" at "+str(r)+" for "+str(t)+" years is Rs."+str(interest),bg="lightcyan",font=("Calibri",12),width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "teal", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal_label=Label(window,text="Principal=",fg="black",bg="teal",font=("Calibri",12),bd=1)
principal_label.place(x=20, y=90)

principal=Entry(window, text="", bd=2, width=22)
principal.place(x=150, y=92)

rate_label=Label(window,text="Rate=",bg="teal",fg="black",font=("Calibri",12))
rate_label.place(x=20,y=140)

rate=Entry(window,text="",bd=2,width=15)
rate.place(x=150,y=142)

time_label=Label(window,text="Time=",bg="teal",fg="black",font=("Calibri",12))
time_label.place(x=20,y=185)

time=Entry(window,text="",bd=2,width=15)
time.place(x=150,y=187)

calculator_button=Button(window,text="Calculate Interest",command=calculate_interest,fg="black",bg="cyan",bd=4)
calculator_button.place(x=20,y=250)




result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()