from tkinter import *
aken=Tk()
aken.geometry("1000x1000")
aken.title("Tunniplaan TARpv21")
p=["Esmaspäev","Tesipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,10,2):
	Ep=Label(aken,text=p[j],relief="groove",font="Arial",height=6).grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
	j+=1


for i in range(11):
	tn="t"+str(i)
	tn=Label(aken,text=i,relief="groove",font="Arial",width=8,height=2).grid(row=0,column=i+1,sticky=N+S+W+E)

ml=Button(aken,text="Multimeedia",relief="groove",font="Arial",width=4,height=1,bg="#424983").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
pr=Button(aken,text="Programmeerimise \nalused",relief="groove",font="Arial",width=4,height=1,bg="#1ebbd7").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
ml=Button(aken,text="Multimeedia",relief="groove",font="Arial",width=4,height=1,bg="#424983").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
pr=Button(aken,text="Programmeerimise \nalused",relief="groove",font="Arial",width=4,height=1,bg="#1ebbd7").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
ru=Button(aken,text="Rühma\njuhataja \ntund",relief="groove",font="Arial",width=4,height=1,bg="#1ebbd7").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)

en1=Button(aken,text="Inglise Keel_1",relief="groove",font="Arial",width=4,height=1,bg="#f8ac6a").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
en2=Button(aken,text="Inglise Keel_2",relief="groove",font="Arial",width=4,height=1,bg="#8e7cc3").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
op=Button(aken,text="Operatsioonisüstee\n mide alused",relief="groove",font="Arial",width=4,height=1,bg="#5743bb").grid(row=3,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
kh=Button(aken,text="Kehaline Kasvatus",relief="groove",font="Arial 11",width=4,height=1,bg="#ff8ab3").grid(row=3,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
est2=Button(aken,text="Eesti Keel\n_2",relief="groove",font="Arial 11",width=4,height=1,bg="#cbd9db").grid(row=4,column=9,sticky=N+S+W+E)
est1=Button(aken,text="Eesti Keel\n_1",relief="groove",font="Arial 11",width=4,height=1,bg="#5743bb").grid(row=3,column=9,sticky=N+S+W+E)
geo=Button(aken,text="Ajalugu \n inim\ngeograafia",relief="groove",font="Arial 11",width=4,height=1,bg="#e69138").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)

pr=Button(aken,text="Programmeerimise \nalused",relief="groove",font="Arial",width=4,height=1,bg="#1ebbd7").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
ml=Button(aken,text="Multimeedia",relief="groove",font="Arial",width=4,height=1,bg="#424983").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
ml=Button(aken,text="Multimeedia",relief="groove",font="Arial",width=4,height=1,bg="#424983").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
pr=Button(aken,text="Programmeerimise \nalused",relief="groove",font="Arial",width=4,height=1,bg="#1ebbd7").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
kn=Button(aken,text="Kunstiained",relief="groove",font="Arial",width=4,height=1,bg="#ff8ab3").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

ad=Button(aken,text="Andme\nbaasisüsteemide \n alused",relief="groove",font="Arial",width=4,height=1,bg="#ff5791").grid(row=7,column=2,columnspan=2,rowspan=2,sticky=N+S+W+E)
ad=Button(aken,text="Andme\nbaasisüsteemide \n alused",relief="groove",font="Arial",width=4,height=1,bg="#ff5791").grid(row=7,column=4,columnspan=3,rowspan=2,sticky=N+S+W+E)
geo=Button(aken,text="Ajalugu \n inim\ngeograafia",relief="groove",font="Arial 11",width=4,height=1,bg="#e69138").grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
est2=Button(aken,text="Eesti Keel\n_2",relief="groove",font="Arial 11",width=4,height=1,bg="#cbd9db").grid(row=7,column=8,sticky=N+S+W+E)
est1=Button(aken,text="Eesti Keel\n_1",relief="groove",font="Arial 11",width=4,height=1,bg="#5743bb").grid(row=8,column=8,sticky=N+S+W+E)

rus=Button(aken,text="Keel ja kirjandus",relief="groove",font="Arial 11",width=4,height=1,bg="#949639").grid(row=9,column=3,columnspan=2,rowspan=2,sticky=N+S+W+E)
mat=Button(aken,text="Matemaatika",relief="groove",font="Arial 11",width=4,height=1,bg="#ff8e9a").grid(row=9,column=6,columnspan=2,rowspan=2,sticky=N+S+W+E)
suht=Button(aken,text="Suhtlemine ja \n klienditeenidus",relief="groove",font="Arial 11",width=4,height=1,bg="#5743bb").grid(row=9,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
geo=Button(aken,text="Ajalugu \n inim\ngeograafia",relief="groove",font="Arial 11",width=4,height=1,bg="#e69138").grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)







aken.mainloop()



