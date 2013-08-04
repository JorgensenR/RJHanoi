# Ryan Jorgensen
# Tower's of Hanoi game

from Tkinter import *


class rj_hanoi(Frame):
    def __init__(self, master=None):
        # initialize frame
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Pickles of Hanoi")
        self.make_bg()
        self.make_stuffs()
        
    
    def make_bg(self):
        self.canvas = Canvas(root, width=1100, height=500)
        background = PhotoImage(file='imgs/bg.gif')
        self.canvas.create_image(510,260,image=background)
        background.image = background
        self.canvas.pack()

        #Create drawable canvas
    def make_stuffs(self):
        disk1 = PhotoImage(file='imgs/d1.gif')
        self.canvas.create_image(210,430,image=disk1)
        disk1.image = disk1
        
        disk2 = PhotoImage(file='imgs/d2.gif')
        self.canvas.create_image(210,405,image=disk2)
        disk2.image = disk2
        
        disk3 = PhotoImage(file='imgs/d3.gif')
        self.canvas.create_image(210,380,image=disk3)
        disk3.image = disk3
        

        p1 = Button(self.canvas, text="Step 1", command=self.play_game)
        p1_window = self.canvas.create_window(165, 110, anchor='nw', window=p1,
                                              tags='p1')

        self.canvas.pack()
        
    def play_game(self):
        self.canvas.move(4,300,50)
    '''
    def play_game2(self):
        self.canvas.move(3,600,25)
    
    def play_game3(self):
        self.canvas.move(4,300,-30)

    def reset(self):
        root.destroy() 
    '''  
# create the root window
root = Tk()

# modify the window

root.geometry("1100x500")


# kick off the window's event-loop
app = rj_hanoi(root)
root.mainloop()
