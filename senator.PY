import tkinter
class senator():
    def __init__(self):
        self.pencerem=tkinter.Tk()
        self.giriş=tkinter.Entry(self.pencerem)
        self.giriş.pack()
        self.düğme=tkinter.Button(self.pencerem,command=self.getir,text="getir")
        self.değişken=tkinter.StringVar()
        self.listbox=tkinter.Listbox(self.pencerem,listvariable=self.değişken)
        self.düğme.pack()
        self.listbox.pack()
        tkinter.mainloop()
    def getir(self):
        self.dosyam=open("senator.txt","r")
        self.liste=[]
        for line in self.dosyam:
            line=line.rstrip()
            line=line.split(",")
            if self.giriş.get()==line[1]:
                self.liste.append(line[0]+" "+line[2])
        self.değişken.set(tuple(self.liste))
        
senator()
            

