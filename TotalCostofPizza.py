import tkinter
import tkinter.messagebox

'''
Design a creative UI using Python's tkinter module to calculate the total cost of a pizza.

The UI should have (at least) each widget that was covered in class:
- Frames
- Labels
- input box
- buttons
- radio buttons
- check boxes

You can use check boxes for for selecting toppings (each with a different cost)
Radio buttons for the type of crust selected (each with a different cost)
buttons for calculation and quit
The input box can be used to record the name of the person placing the order
Use a message box to display the total cost of the pizza along with the name of the person placing the order

Make sure your design is well laid out and intuitive to the user.
Take account of spacing and packing so that everything is properly aligned and professional looking.
Be creative with font, color, size, etc.

'''
'''
Import tkinter 
Create Class 
'''

class PizzaCost:

    def __init__(self):
        self.main_window = tkinter.Tk()

        '''
        Create box
        '''

        self.main_window.geometry('500x300')
        self.main_window.title('Pizza Cost Calculator')


        '''
        Create Frames (will need 13)
        '''
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)
        self.frame10 = tkinter.Frame(self.main_window)
        self.frame11 = tkinter.Frame(self.main_window)
        self.frame12 = tkinter.Frame(self.main_window)
        self.frame13 = tkinter.Frame(self.main_window)

        # Pack frames 

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()
        self.frame10.pack()
        self.frame11.pack()
        self.frame12.pack()
        self.frame13.pack()

        '''
        Crust (Label & Radio Boxes)
        '''
        self.labelCrust = tkinter.Label(self.frame1, text= 'Select your crust')
        
        self.labelCrust.pack()

        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.frame3, text='thin $10', variable=self.radio_var, value=10)
        self.rb2 = tkinter.Radiobutton(self.frame3, text='regular $5', variable=self.radio_var, value=5)
        self.rb3 = tkinter.Radiobutton(self.frame3, text='stuffed $15', variable=self.radio_var, value=15)

        # Make regular crust the default
        self.rb2.select()

        # Pack the Radio Boxes
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')

        '''
        Toppings (Label & Check Boxes)
        '''
        self.labelToppings = tkinter.Label(self.frame6, text='select your toppings')

        self.labelToppings.pack()

        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()
        self.cb3_var = tkinter.IntVar()
        self.cb4_var = tkinter.IntVar()
        self.cb5_var = tkinter.IntVar()
        self.cb6_var = tkinter.IntVar()
        self.cb7_var = tkinter.IntVar()
        self.cb8_var = tkinter.IntVar()
        self.cb9_var = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.frame7, text='regular sauce +$2',variable=self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.frame7, text='bbq sauce +$4',variable=self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.frame7, text='cheese +$3',variable=self.cb3_var)
        self.cb4 = tkinter.Checkbutton(self.frame8, text='pepperoni +$1',variable=self.cb4_var)
        self.cb5 = tkinter.Checkbutton(self.frame8, text='sausage +$1.50',variable=self.cb5_var)
        self.cb6 = tkinter.Checkbutton(self.frame8, text='ham +$1.77',variable=self.cb6_var)
        self.cb7 = tkinter.Checkbutton(self.frame9, text='bacon +$2.33',variable=self.cb7_var)
        self.cb8 = tkinter.Checkbutton(self.frame9, text='olives +$1.68',variable=self.cb8_var)
        self.cb9 = tkinter.Checkbutton(self.frame9, text='bell pepper +$4.37',variable=self.cb9_var)

        # Pack Check Buttons 
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.cb4.pack(side='left')
        self.cb5.pack(side='left')
        self.cb6.pack(side='left')
        self.cb7.pack(side='left')
        self.cb8.pack(side='left')
        self.cb9.pack(side='left')


        '''
        Customer's Name
        '''
        self.labelName = tkinter.Label(self.frame12, text='Enter your Name')

        self.NameEntry = tkinter.Entry(self.frame12, width=10)

        self.labelName.pack(side='left')
        self.NameEntry.pack() 

        '''
        Quit & Calculate Buttons
        '''
        self.buttonQuit = tkinter.Button(self.main_window, text='Quit', command= self.main_window.destroy)
        self.buttonCalculate = tkinter.Button(self.main_window, text='Calculate', command=self.do_something)

        #Pack Buttons 
        self.buttonQuit.pack(side='left')
        self.buttonCalculate.pack(side='right')

        
        tkinter.mainloop()
    '''
    Do Something
    '''
    def do_something(self):
        customerName = self.NameEntry.get()
        message = "Hi "+customerName+'\n'
        Total_Cost = 0

        Total_Cost += self.radio_var.get()

        if self.cb1_var.get() == 1: 
            Total_Cost += 2
        
        if self.cb2_var.get() == 1: 
            Total_Cost += 4

        if self.cb3_var.get() == 1: 
            Total_Cost += 3

        if self.cb4_var.get() == 1: 
            Total_Cost += 1

        if self.cb5_var.get() == 1: 
            Total_Cost += 1.50

        if self.cb6_var.get() == 1: 
            Total_Cost += 1.77

        if self.cb7_var.get() == 1: 
            Total_Cost += 2.33

        if self.cb8_var.get() == 1: 
            Total_Cost += 1.68

        if self.cb9_var.get() == 1: 
            Total_Cost += 4.37


        tkinter.messagebox.showinfo('Response',str(message) + ' The total cost of your pizza is $' + str(Total_Cost)) 
        
        


Cost_of_Pizza = PizzaCost()
print('Done')