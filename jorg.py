# Ryan Jorgensen
# Tower's of Hanoi game

from Tkinter import *


class rj_hanoi(Frame):
    def __init__(self, master=None):
        # initialize frame
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Jorgensen")
        self.make_stuffs()
        
    def make_stuffs(self):
    
        self.canvas = Canvas(root, width=1100, height=500)
        background = PhotoImage(file='bg.gif')
        self.canvas.create_image(510,260,image=background)
        background.image = background
        self.canvas.pack()

        #Create drawable canvas

        disk1 = PhotoImage(file='d1.gif')
        self.canvas.create_image(210,430,image=disk1)
        disk1.image = disk1
        
        disk2 = PhotoImage(file='d2.gif')
        self.canvas.create_image(210,405,image=disk2)
        disk2.image = disk2
        
        disk3 = PhotoImage(file='d3.gif')
        self.canvas.create_image(210,380,image=disk3)
        disk3.image = disk3
        '''
        disk4 = PhotoImage(file='d4.gif')
        self.canvas.create_image(210,355,image=disk4)
        disk4.image = disk4
        
        disk5 = PhotoImage(file='d5.gif')
        self.canvas.create_image(210,330,image=disk5)
        disk5.image = disk5

        disk6 = PhotoImage(file='d6.gif')
        self.canvas.create_image(210,305,image=disk6)
        disk6.image = disk6

        disk7 = PhotoImage(file='d7.gif')
        self.canvas.create_image(210,280,image=disk7)
        disk7.image = disk7

        disk8 = PhotoImage(file='d8.gif')
        self.canvas.create_image(210,255,image=disk8)
        disk8.image = disk8
        
        reset = Button(self.canvas, text="End Game", command=self.reset)
        reset_window = self.canvas.create_window(468, 80, anchor='nw',window=reset)
        '''
        p1 = Button(self.canvas, text="Step 1", command=play_game)
        p1_window = self.canvas.create_window(165, 110, anchor='nw', window=p1,
                                              tags='p1')
        '''
        p2 = Button(self.canvas, text="Step 2", command=self.play_game2)
        p2_window = self.canvas.create_window(235, 110, anchor='nw', window=p2,
                                              tags='p2')
        p3 = Button(self.canvas, text="Step 3", command=self.play_game3)
        p3_window = self.canvas.create_window(305, 110, anchor='nw', window=p3,
                                              tags='p3')
        p4 = Button(self.canvas, text="Step 4", command=self.play_game4)
        p4_window = self.canvas.create_window(375, 110, anchor='nw', window=p4,
                                              tags='p4')
        p5 = Button(self.canvas, text="Step 5", command=self.play_game5)
        p5_window = self.canvas.create_window(445, 110, anchor='nw', window=p5,
                                              tags='p5')
        p6 = Button(self.canvas, text="Step 6", command=self.play_game6)
        p6_window = self.canvas.create_window(515, 110, anchor='nw', window=p6,
                                              tags='p6')
        p7 = Button(self.canvas, text="Step 7", command=self.play_game7)
        p7_window = self.canvas.create_window(585, 110, anchor='nw', window=p7,
                                              tags='p7')
        p8 = Button(self.canvas, text="Step 8", command=self.play_game8)
        p8_window = self.canvas.create_window(655, 110, anchor='nw', window=p8,
                                              tags='p8')
        p9 = Button(self.canvas, text="Step 9", command=self.play_game9)
        p9_window = self.canvas.create_window(725, 110, anchor='nw', window=p9,
                                              tags='p9')
        p10 = Button(self.canvas, text="Step 10", command=self.play_game10)
        p10_window = self.canvas.create_window(795, 110, anchor='nw', window=p10,
                                              tags='p10')
        Finish = Button(self.canvas, text="Finish Him!", command=self.play_game11)
        Finish_window = self.canvas.create_window(462,140,anchor='nw',window=Finish)
        #inst = bg.create_text(510, 100, text='Choose a starting peg')
        '''
        self.canvas.pack()
def play_game():
    root.canvas.move(4,300,50)
    '''
    def play_game2(self):
        self.canvas.move(3,600,25)
    def play_game3(self):
        self.canvas.move(4,300,-30)
    def play_game4(self):
        self.canvas.move(2,300,0)
    def play_game5(self):
        self.canvas.move(4,-300,0)
        self.canvas.move(3,0,0)
    def play_game6(self):
        self.canvas.move(3,-600,0)
    def play_game7(self):
        self.canvas.move(4,-300,0)
    def play_game8(self):
        self.canvas.move(2,300,0)
    def play_game9(self):
        self.canvas.move(4,300,30)
    def play_game10(self):
        self.canvas.move(3,600,-30)
    def play_game11(self):
        self.canvas.move(4,300,-60)
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
