import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import math
'''
some gui lib
'''
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

'''
the function you want to plot
'''
def func(x):
    y = 5 * math.sin(2 * math.pi * 1 * x)
    z = 3 * math.pi * math.exp(y)
    return z


class Func_plot:
    '''
    Programming a data visualization tool
    in plot function:
        range is a vector -- (x_min,x_max) default value (-10,10) 
    '''
    def __init__(self,func,range=(0,0.01)):
        self.func = func
        self.range = range

    def plot(self):
        x_min = self.range[0]
        x_max = self.range[1]
        x = np.linspace(x_min,x_max,int((x_max - x_min)*100))
        y = [ self.func(m) for m in x ]
        return x,y


class Func_GUI(Func_plot):

    def __init__(self,master):
        Func_plot.__init__(self,func)
        self.master = master
        master.title("Function Visualization GUI")
        self.frame1 = tk.Frame(master, width=200, height=100, bg="white")
        self.frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame2 = tk.Frame(master, width=100, bg="white")
        self.frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.label = tk.Label(master=self.frame1,text ='please enter file name :')
        self.label.pack()
        self.entry = tk.Entry(master=self.frame1)
        self.entry.pack()
        self.button01 = tk.Button(master = self.frame2,text='Start',width = 10,height = 2,bg='white',fg='black',command=self.start)
        self.button01.pack()
        self.button02 = tk.Button(master = self.frame2,text='Stop',width = 10,height = 2,bg='white',fg='black',command=self.stop)
        self.button02.pack()
        self.button1 = tk.Button(master = self.frame2,text='Zoom in',width = 10,height = 2,bg='white',fg='black',command=self.zoomin)
        self.button1.pack()
        self.button2 = tk.Button(master = self.frame2,text='Zoom out',width = 10,height = 2,bg='white',fg='black',command=self.zoomout)
        self.button2.pack()
        self.button3 = tk.Button(master = self.frame2,text='Save',width = 10,height = 2,bg='white',fg='black',command=self.save)
        self.button3.pack()
        
        '''
        plot function graph
        '''
        self.figure1 = plt.Figure(figsize=(6,5), dpi=100)
        self.a = self.figure1.add_subplot(111)
        self.x,self.y = self.plot()
        self.a.plot(self.x,self.y)
        self.bar1 = FigureCanvasTkAgg(self.figure1, self.frame1)
        self.bar1.get_tk_widget().pack()
        self.after_id = None
        self.running = False
        self.setlen = 5
        self.master.after(10, self.run)


    def draw(self):  
            self.a.clear()
            self.x,self.y = self.plot()
            self.a.plot(self.x,self.y)
            self.a.set_xlabel('Time (s)')
            self.a.set_ylabel('Signal (unit)')
            self.bar1.draw()


    def run(self):
        if self.running:
            if self.range[1] - self.range[0] < self.setlen:
                self.range = (self.range[0],self.range[1]+0.1)
            else:
                self.range = (self.range[0]+0.1,self.range[1]+0.1)
            self.draw()
        self.master.after(10,self.run)


    def start(self):
        self.running = True


    def stop(self):
        self.running = False
        

    
    def zoomin(self):
        d = (self.range[1] - self.range[0])
        self.range = (self.range[0] + d/2 ,self.range[1])
        self.setlen = self.range[1] - self.range[0]
        self.draw()


    def zoomout(self):
        d = self.range[1] - self.range[0]
        if self.range[0] - d/2 <= 0:
            self.range =(0, self.range[1])
        else:
            self.range = (self.range[0] - d/2, self.range[1])
        self.setlen = self.range[1] - self.range[0]
        self.draw()
    

    def save(self):
        self.figure1.savefig('signal.png')
        '''
        '''


root = tk.Tk()
plot_gui = Func_GUI(root)
root.mainloop()






