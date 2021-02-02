import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


class Data():
    def __init__(self, data):  
        self.data = int(data)
        split = len(data)//2
        self.code = data[:split]
        self.address = data[split:]

class CPU:
    """The Entire CPU"""
    def __init__(self, master):
        #variables for math and calculations
        self.memory = []

        self.reg_a = "00000000"
        self.reg_b = "00000000"
        self.reg_c = "0000"

        self.alu_1 = "00000000"
        self.alu_2 = "00000000"
        self.alu_out = "00000000"

        self.o = 0
        self.z = 0
        self.n = 0

        self.clock = 0
        self.address_reg = 0

        #variables tell it what base to use
        self.base = 2
        self.length = 8
        self.bool_2 = True

        #setting up tkinter window
        self.master = master
        self.master.geometry('360x460')
        self.master.title("CPU")

        #register frame
        self.registers = tk.LabelFrame(self.master, text="Registers")
        self.registers.place(x=15, y=0)
        self.reg_a_label = tk.Label(self.registers, text ="Reg A:")
        self.reg_a_label.grid(column=0, row=1)
        self.reg_a_value = tk.Label(self.registers, text ="00000000")
        self.reg_a_value.grid(column=1, row=1)
        self.reg_b_label = tk.Label(self.registers, text ="  Reg B:")
        self.reg_b_label.grid(column=2, row=1)
        self.reg_b_value = tk.Label(self.registers, text ="00000000")
        self.reg_b_value.grid(column=3, row=1)
        self.reg_c_label= tk.Label(self.registers, text ="   Reg C:")
        self.reg_c_label.grid(column=4, row=1)
        self.reg_c_value = tk.Label(self.registers, text ="0000")
        self.reg_c_value.grid(column=5, row=1)

        #alu frame
        self.alu = tk.LabelFrame(self.master, text="ALU")
        self.alu.place(x=30, y=50)
        self.alu_1_label = tk.Label(self.alu, text="Input: ")
        self.alu_1_label.grid(column=0, row=0)
        self.alu_1_value = tk.Label(self.alu, text="00000000")
        self.alu_1_value.grid(column=1, row=0)
        self.alu_2_label = tk.Label(self.alu, text="Input: ")
        self.alu_2_label.grid(column=0, row=1)
        self.alu_2_value = tk.Label(self.alu, text="00000000")
        self.alu_2_value.grid(column=1, row=1)
        self.alu_out_label = tk.Label(self.alu, text="Output: ")
        self.alu_out_label.grid(column=0, row=2)
        self.alu_out_value = tk.Label(self.alu, text="00000000")
        self.alu_out_value.grid(column=1, row=2)

        #tk.StringVar
        self.mem_1_var = tk.StringVar()
        self.mem_2_var = tk.StringVar()
        self.mem_3_var = tk.StringVar()
        self.mem_4_var = tk.StringVar()
        self.mem_5_var = tk.StringVar()
        self.mem_6_var = tk.StringVar()
        self.mem_7_var = tk.StringVar()
        self.mem_8_var = tk.StringVar()
        self.mem_9_var = tk.StringVar()
        self.mem_10_var = tk.StringVar()
        self.mem_11_var = tk.StringVar()
        self.mem_12_var = tk.StringVar()
        self.mem_13_var = tk.StringVar()
        self.mem_14_var = tk.StringVar()
        self.mem_15_var = tk.StringVar()
        self.mem_16_var = tk.StringVar()

        #memory frame
        self.mem = tk.LabelFrame(self.master, text="Memory")
        self.mem.place(x=180, y=50)
        self.mem_1 = tk.Entry(self.mem,width=10, textvariable = self.mem_1_var)
        self.mem_1.grid(column=1, row=0)
        self.mem_2 = tk.Entry(self.mem,width=10, textvariable = self.mem_2_var)
        self.mem_2.grid(column=1, row=1)
        self.mem_3 = tk.Entry(self.mem,width=10, textvariable = self.mem_3_var)
        self.mem_3.grid(column=1, row=2)
        self.mem_4 = tk.Entry(self.mem,width=10, textvariable = self.mem_4_var)
        self.mem_4.grid(column=1, row=3)
        self.mem_5 = tk.Entry(self.mem,width=10, textvariable = self.mem_5_var)
        self.mem_5.grid(column=1, row=4)
        self.mem_6 = tk.Entry(self.mem,width=10, textvariable = self.mem_6_var)
        self.mem_6.grid(column=1, row=5)
        self.mem_7 = tk.Entry(self.mem,width=10, textvariable = self.mem_7_var)
        self.mem_7.grid(column=1, row=6)
        self.mem_8 = tk.Entry(self.mem,width=10, textvariable = self.mem_8_var)
        self.mem_8.grid(column=1, row=7)
        self.mem_9 = tk.Entry(self.mem,width=10, textvariable = self.mem_9_var)
        self.mem_9.grid(column=1, row=8)
        self.mem_10 = tk.Entry(self.mem,width=10, textvariable = self.mem_10_var)
        self.mem_10.grid(column=1, row=9)
        self.mem_11 = tk.Entry(self.mem,width=10, textvariable = self.mem_11_var)
        self.mem_11.grid(column=1, row=10)
        self.mem_12 = tk.Entry(self.mem,width=10, textvariable = self.mem_12_var)
        self.mem_12.grid(column=1, row=11)
        self.mem_13 = tk.Entry(self.mem,width=10, textvariable = self.mem_13_var)
        self.mem_13.grid(column=1, row=12)
        self.mem_14 = tk.Entry(self.mem,width=10, textvariable = self.mem_14_var)
        self.mem_14.grid(column=1, row=13)
        self.mem_15 = tk.Entry(self.mem,width=10, textvariable = self.mem_15_var)
        self.mem_15.grid(column=1, row=14)
        self.mem_16 = tk.Entry(self.mem,width=10, textvariable = self.mem_16_var)
        self.mem_16.grid(column=1, row=15)
        self.addr_1 = tk.Label(self.mem, text="0000:")
        self.addr_1.grid(column=0, row=0)
        self.addr_2 = tk.Label(self.mem, text="0001:")
        self.addr_2.grid(column=0, row=1)
        self.addr_3 = tk.Label(self.mem, text="0010:")
        self.addr_3.grid(column=0, row=2)
        self.addr_4 = tk.Label(self.mem, text="0011:")
        self.addr_4.grid(column=0, row=3)
        self.addr_5 = tk.Label(self.mem, text="0100:")
        self.addr_5.grid(column=0, row=4)
        self.addr_6 = tk.Label(self.mem, text="0101:")
        self.addr_6.grid(column=0, row=5)
        self.addr_7 = tk.Label(self.mem, text="0110:")
        self.addr_7.grid(column=0, row=6)
        self.addr_8 = tk.Label(self.mem, text="0111:")
        self.addr_8.grid(column=0, row=7)
        self.addr_9 = tk.Label(self.mem, text="1000:")
        self.addr_9.grid(column=0, row=8)
        self.addr_10 = tk.Label(self.mem, text="1001:")
        self.addr_10.grid(column=0, row=9)
        self.addr_11 = tk.Label(self.mem, text="1010:")
        self.addr_11.grid(column=0, row=10)
        self.addr_12 = tk.Label(self.mem, text="1011:")
        self.addr_12.grid(column=0, row=11)
        self.addr_13 = tk.Label(self.mem, text="1100:")
        self.addr_13.grid(column=0, row=12)
        self.addr_14 = tk.Label(self.mem, text="1101:")
        self.addr_14.grid(column=0, row=13)
        self.addr_15 = tk.Label(self.mem, text="1110:")
        self.addr_15.grid(column=0, row=14)
        self.addr_16 = tk.Label(self.mem, text="1111:")
        self.addr_16.grid(column=0, row=15)

        #control frame
        self.control = tk.LabelFrame(self.master, text="Control")
        self.control.place(x=30, y=140)
        self.instruction_label = tk.Label(self.control, text="Code: ")
        self.instruction_label.grid(column=0, row=0)
        self.instruction = tk.Label(self.control, text="")
        self.instruction.grid(column=1, row=0)
        self.address_label = tk.Label(self.control, text="Address: ")
        self.address_label.grid(column=0, row=1)
        self.address = tk.Label(self.control, text="0000")
        self.address.grid(column=1, row=1)
        self.clock_label = tk.Label(self.control, text="Clock: ")
        self.clock_label.grid(column=0, row=2)
        self.clock_value = tk.Label(self.control, text="0")
        self.clock_value.grid(column=1, row=2)
        self.o_label = tk.Label(self.control, text="O: ")
        self.o_label.grid(column=0, row=3)
        self.o_value = tk.Label(self.control, text="0")
        self.o_value.grid(column=1, row=3)
        self.z_label = tk.Label(self.control, text="Z: ")
        self.z_label.grid(column=0, row=4)
        self.z_value = tk.Label(self.control, text="0")
        self.z_value.grid(column=1, row=4)
        self.n_label = tk.Label(self.control, text="N: ")
        self.n_label.grid(column=0, row=5)
        self.n_value = tk.Label(self.control, text="0")
        self.n_value.grid(column=1, row=5)

        #frame for button
        self.commands = tk.Frame(self.master)
        self.commands.place(x=30, y=290)
        self.main_button = tk.Button(self.commands, text="Get Memory", command=self.get_memory)
        self.main_button.pack()

        #taskbar menu thing
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open...", command=self.open_file)

        self.base_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Base", menu=self.base_menu)
        self.base_menu.add_command(label="Base 2 (Binary)", command=self.set_base_2)
        self.base_menu.add_command(label="Base 16 (Hexadecimal)", command=self.set_base_16)

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Commands", command=self.help)
        self.help_menu.add_command(label="About...", command=self.about)

    def check_number(self, code):
        try: #checks if number is either binary or hexadecimal depending on what self.base is set to
            code = int(code, self.base)
            return True
        except ValueError: #if not then returns false
            return False

    def set_base_2(self): #changes variables and memory addresses to binary values
        self.base = 2
        self.length = 8
        self.bool_2 = True
        self.addr_1.configure(text="0000:")
        self.addr_2.configure(text="0001:")
        self.addr_3.configure(text="0010:")
        self.addr_4.configure(text="0011:")
        self.addr_5.configure(text="0100:")
        self.addr_6.configure(text="0101:")
        self.addr_7.configure(text="0110:")
        self.addr_8.configure(text="0111:")
        self.addr_9.configure(text="1000:")
        self.addr_10.configure(text="1001:")
        self.addr_11.configure(text="1010:")
        self.addr_12.configure(text="1011:")
        self.addr_13.configure(text="1100:")
        self.addr_14.configure(text="1101:")
        self.addr_15.configure(text="1110:")
        self.addr_16.configure(text="1111:")

    def set_base_16(self): #changes variables and memory addresses to hexadecimal values
        self.base = 16
        self.length = 2
        self.bool_2 = False
        self.addr_1.configure(text="0:")
        self.addr_2.configure(text="1:")
        self.addr_3.configure(text="2:")
        self.addr_4.configure(text="3:")
        self.addr_5.configure(text="4:")
        self.addr_6.configure(text="5:")
        self.addr_7.configure(text="6:")
        self.addr_8.configure(text="7:")
        self.addr_9.configure(text="8:")
        self.addr_10.configure(text="9:")
        self.addr_11.configure(text="A:")
        self.addr_12.configure(text="B:")
        self.addr_13.configure(text="C:")
        self.addr_14.configure(text="D:")
        self.addr_15.configure(text="E:")
        self.addr_16.configure(text="F:")

    def get_code(self,code): #finds corresponding function for binary or hexadecimal code
        op_code = {
        1: self.loadA, #A = VALUE IN MEMORY LOCATION
        2: self.loadB, #B = VALUE IN MEMORY LOCATION
        3: self.addBA, #A = A + B
        4: self.subBA, #A = A - B
        5: self.stoA, #STORE A INTO MEMORY NUMBER
        6: self.AB, #Z=1, IF AB=0 : 
        7: self.AplusB, #Z=1, IF  : B=0
        8: self.AxorB, #Z=1, IF AxorB=0
        9: self.reset, #O,N,Z = 0
        10: self.juiz, #JUMP TO ADRESS # IF Z=0
        11: self.setC, #REG C = VALUE
        12: self.incC, #C = C + 1
        13: self.decC, #C = C - 1
        14: self.jump, #JUMP TO ADDRESS #
        15: self.halt #STOP PROGRAM
        }
        code = op_code.get(code)
        return code

    def open_file(self): #lets user get memory from a txt file
        self.memory = [] #resets memory (in case user wants to open another file after the first one)
        file_name = askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")), title = "Choose a file.")
        try:
            info = open(file_name).read().splitlines()
        except:
            return
        if len(info) > 16: #makes sure file is 16 lines
            messagebox.showerror("Error", "File must be no more than 16 lines.")
            return
        for i in info:
            if i == "":
                continue
            #make sure data is usable
            elif len(i) != self.length:
                messagebox.showerror("Error", "Error with data.")
                return
            elif not self.check_number(i):
                messagebox.showerror("Error", "Error with data.")
                return
        variables = [
        self.mem_1_var, 
        self.mem_2_var, 
        self.mem_3_var, 
        self.mem_4_var, 
        self.mem_5_var, 
        self.mem_6_var, 
        self.mem_7_var, 
        self.mem_8_var, 
        self.mem_9_var, 
        self.mem_10_var, 
        self.mem_11_var, 
        self.mem_12_var, 
        self.mem_13_var, 
        self.mem_14_var, 
        self.mem_15_var, 
        self.mem_16_var
        ]
        y=0 #to set the row
        for i in info:
            if self.bool_2:
                if i =="":
                    i = "00000000"
            else:
                if i =="":
                    i = "00"
            #make label for each object
            #mem_from_file = tk.Label(self.mem, text=i)
            #mem_from_file.grid(column=1, row=y)
            variables[y].set(i)
            y +=1
            #add to memory object list
            i = Data(i)
            self.memory.append(i)
        #add extra items if list is less than 16 
        for i in range(16-len(info)):
            if self.bool_2:
                self.memory.append(Data('00000000'))
            else:
                self.memory.append(Data('00'))
        #set button to do next step
        self.main_button.configure(text="Next Step", command=self.main)
        try:
            self.menu.delete("Base") 
        except:
            pass

    def about(self): #defines the about page
        window = tk.Toplevel()
        window.title("About")
        text = tk.Message(window, text="Hello, Fernando made this.\nPlease give me a lot of XP and @T and a very good grade.")
        text.pack()

        dismiss = tk.Button(window, text="Dismiss", command=window.destroy)
        dismiss.pack()

    def help(self): #defines the help page
        window = tk.Toplevel()
        window.title("Help")
        text = tk.Message(window, text="""0001 / 1 : (loadA), A = VALUE IN MEMORY LOCATION
            \n0010 / 2 : (loadB), B = VALUE IN MEMORY LOCATION
            \n0011 / 3 : (addBA), A = A + B
            \n0100 / 4 : (subBA), A = A - B
            \n0101 / 5 : (stoA), STORE A INTO MEMORY NUMBER
            \n0110 / 6 : (AB), Z=1, IF AB=0
            \n0111 / 7 : (AplusB), Z=1, IF A+B=0
            \n1000 / 8 : (AxorB), Z=1, IF AxorB=0
            \n1001 / 9 : (reset), O,N,Z = 0
            \n1010 / A : (juiz), JUMP TO ADRESS # IF Z=0
            \n1011 / B : (setC), REG C = VALUE
            \n1100 / C : (incC), C = C + 1
            \n1101 / D : (decC), C = C - 1
            \n1110 / E : (jump), JUMP TO ADDRESS #
            \n1111 / F : (halt), STOP PROGRAM""")
        text.pack()

        dismiss = tk.Button(window, text="Dismiss", command=window.destroy)
        dismiss.pack()

    def get_memory(self): #gets memory from input boxes
        mem_get = [
        self.mem_1.get(), 
        self.mem_2.get(), 
        self.mem_3.get(), 
        self.mem_4.get(), 
        self.mem_5.get(), 
        self.mem_6.get(), 
        self.mem_7.get(), 
        self.mem_8.get(), 
        self.mem_9.get(), 
        self.mem_10.get(), 
        self.mem_11.get(), 
        self.mem_12.get(), 
        self.mem_13.get(), 
        self.mem_14.get(), 
        self.mem_15.get(), 
        self.mem_16.get()
        ]

        for i in mem_get:
            if self.bool_2:
                if i =="":
                    i = "00000000"
            else:
                if i =="":
                    i = "00"

            if len(i) != self.length:
                messagebox.showerror("Error", "Error with inputs.")
                return
            elif not self.check_number(i):
                messagebox.showerror("Error", "Error with inputs.")
                return

            i = Data(i)
            self.memory.append(i)
        self.main_button.configure(text="Next Step", command=self.main)
        self.menu.delete("Base") 

    def main(self):
        #find the binary code or if past line 16 do nothing
        try:
            code = self.memory[self.address_reg].code
        except IndexError:
            self.address_reg = 0
            self.main()
            return
        #finds corresponding function for binary or hexadecimal code
        code = int(code, self.base)
        code = self.get_code(code)
        #blank lines or 00.. will be skipped
        try:
            code()
        except TypeError:
            pass
        self.control_out()
        self.address_reg += 1

    def control_out(self):
        codes = {
        0: 'NONE',
        1: 'LOAD_A',
        2: 'LOAD_B',
        3: 'ADD BA',
        4: 'SUB BA',
        5: 'STO_A',
        6: 'AB',
        7: 'A+B',
        8: 'AxorB',
        9: 'RESET',
        10: 'JUIZ',
        11: 'SET C',
        12: 'INC C',
        13: 'DEC C',
        14: 'JUMP',
        15: 'HALT'
        }

        code = codes.get(int(self.memory[self.address_reg].code, self.base))
        #change the text to correspond with inputs, flags, etc.
        self.instruction.configure(text=code)
        if self.bool_2:
            self.address.configure(text=f"{'{0:04b}'.format(self.address_reg)}")
        else:
            self.address.configure(text=f"{'{0:01x}'.format(self.address_reg)}")
        self.clock_value.configure(text=self.clock)

        self.reg_a_value.configure(text=self.reg_a)
        self.reg_b_value.configure(text=self.reg_b)
        self.reg_c_value.configure(text=self.reg_c)

        self.alu_1_value.configure(text=self.alu_1)
        self.alu_2_value.configure(text=self.alu_2)
        self.alu_out_value.configure(text=self.alu_out)

        self.o_value.configure(text=self.o)
        self.z_value.configure(text=self.z)
        self.n_value.configure(text=self.n)

    def loadA(self):
        #takes the address indicated (e.g. 0001[0000])
        location = self.memory[self.address_reg].address
        #changes the address to decimal (so it can be used as a location in a list)
        information = int(location, self.base)
        #takes data from address found above(e.g. 0000) from the memory list and puts it in Register A
        self.reg_a = self.memory[information].data
        self.clock += 1

    def loadB(self):
        #same thing as loadA but in one line
        self.reg_b = self.memory[int(self.memory[self.address_reg].address, self.base)].data
        self.clock += 1

    def addBA(self):
        self.alu_1 = int(self.reg_a, self.base)
        self.alu_2 = int(self.reg_b, self.base)
        self.alu_out = self.alu_1 + self.alu_2

        if self.bool_2:
            self.alu_1 = '{0:08b}'.format(self.alu_1)
            self.alu_2 = '{0:08b}'.format(self.alu_2)
        else:
            self.alu_1 = '{0:02x}'.format(self.alu_1)
            self.alu_2 = '{0:02x}'.format(self.alu_2)

        if self.alu_out >= 127:
            self.alu_out = 0
            self.o = 1
        if self.bool_2:
            self.alu_out = '{0:08b}'.format(self.alu_out)
        else:
            self.alu_out = '{0:02x}'.format(self.alu_out)
        self.reg_a = self.alu_out
        self.clock += 1

    def subBA(self):
        self.alu_1 = int(self.reg_a, self.base)
        self.alu_2 = int(self.reg_b, self.base)
        self.alu_out = self.alu_1 - self.alu_2

        if self.bool_2:
            self.alu_1 = '{0:08b}'.format(self.alu_1)
            self.alu_2 = '{0:08b}'.format(self.alu_2)
        else:
            self.alu_1 = '{0:02x}'.format(self.alu_1)
            self.alu_2 = '{0:02x}'.format(self.alu_2)

        if self.alu_out >= 127: #256 is the biggest number possible
            self.alu_out = 0
            self.o = 1
        elif self.alu_out < -128: #-128 is the smallest number possible
            self.alu_out = 0
            self.o = 1
            self.n = 1
        elif self.alu_out < 0:
            self.n = 1
            #converts to twos compliment
            self.alu_out *= -1 #sets to positive so that converting to binary wont mess up
            #inverts the number in binary
            self.alu_out = '{0:08b}'.format(self.alu_out)
            new_num = []
            for i in self.alu_out:
                if not(int(i)):
                    new_num.append('1')
                else:
                    new_num.append('0')
            self.alu_out = ''.join(new_num)
            #adds 1 to the number
            self.alu_out = int(self.alu_out, 2) + 1

        #set negative int to binary or hexadecimal
        if self.bool_2:
            self.alu_out = '{0:08b}'.format(self.alu_out)
        else:
            self.alu_out = '{0:02x}'.format(self.alu_out)

        self.reg_a = self.alu_out
        self.clock += 1

    def stoA(self): #stores info at Register A to given address
        self.memory[int(self.memory[self.address_reg].address, self.base)] = Data(self.reg_a)
        y = int(self.memory[self.address_reg].address, self.base)
        stored = tk.Label(self.mem, text=self.reg_a)
        stored.grid(column=1, row=y)
        self.clock += 1

    def AB(self): #if A and B = 0, sets Z = 1
        self.alu_1 = int(self.reg_a, self.base)
        self.alu_2 = int(self.reg_b, self.base)
        if (self.alu_1&self.alu_2) == 0:
            self.z = 1
        self.clock += 1

    def AplusB(self): #if A or B = 0, sets Z = 1
        self.alu_1 = int(self.reg_a, self.base)
        self.alu_2 = int(self.reg_b, self.base)
        if (self.alu_1|self.alu_2) == 0:
            self.z = 1
        self.clock += 1

    def AxorB(self): #if A xor B = 0, sets Z = 1
        self.alu_1 = int(self.reg_a, self.base)
        self.alu_2 = int(self.reg_b, self.base)

        if (self.alu_1^self.alu_2) == 0:
            self.z = 1
        self.clock += 1

    def reset(self): #resets flags
        self.o = 0
        self.z = 0
        self.n = 0
        self.clock += 1

    def juiz(self): #jumps to address if Z = 0
        if self.z == 0:
            jump = int(self.memory[self.address_reg].address)
            remain = jump - self.address_reg
            self.address_reg += remain
        self.clock += 1

    def setC(self): #sets C to the value beside the instruction (1011 XXXX)
        self.reg_c = self.memory[self.address_reg].address

        self.clock += 1

    def incC(self): #increases C by 1
        c = int(self.reg_c, self.base)
        c +=1

        if self.bool_2:
            c = '{0:04b}'.format(c)
        else:
            c = '{0:02x}'.format(c)

        self.reg_c = c
        self.clock += 1

    def decC(self): #decreases C by 1
        c = int(self.reg_c, self.base)
        c -= 1
        if self.bool_2:
            c = '{0:04b}'.format(c)
        else:
            c = '{0:02x}'.format(c)

        self.reg_c = c
        self.clock += 1

    def jump(self): #jumps to address
        jump = int(self.memory[self.address_reg].address)
        remain = jump - self.address_reg
        self.address_reg += remain
        self.clock += 1

    def halt(self): #stops
        self.main_button.configure(text="Done!",command=self.halt)


###main###
ROOT = tk.Tk()
GUI = CPU(ROOT)
ROOT.mainloop()
