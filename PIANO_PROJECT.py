from tkinter import *
import pygame


class PianoGui:
	def __init__(self, master):
		self.master = master
		master.title("STUDY CHORDS")
		self.Label = Label(master , text="PIANO")
		self.Label.grid(row=0 , columnspan=55)

#ADD IN SOUND
#Octave 1
		def Key1():
			print("C1")
		def Key2():
			print("C#1")
		def Key3():
			print("D#1")
		def Key4():
			print("D1")
		def Key5():
			print("E1")
		def Key6():
			print("F1")
		def Key7():
			print("F#1")
		def Key8():
			print("G1")
		def Key9():
			print("G#1")
		def Key10():
			print("A1")
		def Key11():
			print("A#1")
		def Key12():
			print("B1")
#2nd Octave
		def Key13():
			print("C2")
		def Key14():
			print("C#2")
		def Key15():
			print("D#2")
		def Key16():
			print("D2")
		def Key17():
			print("E2")
		def Key18():
			print("F2")
		def Key19():
			print("F#2")
		def Key20():
			print("G2")
		def Key21():
			print("G#2")
		def Key22():
			print("A2")
		def Key23():
			print("A#2")
		def Key24():
			print("B2")
#3rd Octave
		def Key25():
			print("C3")
		def Key26():
			print("C#3")
		def Key27():
			print("D#3")
		def Key28():
			print("D3")
		def Key29():
			print("E3")
		def Key30():
			print("F3")
		def Key31():
			print("F#3")
		def Key32():
			print("G3")
		def Key33():
			print("G#3")
		def Key34():
			print("A3")
		def Key35():
			print("A#3")
		def Key36():
			print("B3")

#4th Octave
		def Key37():
			print("C4")
		def Key38():
			print("C#4")
		def Key39():
			print("D#4")
		def Key40():
			print("D4")
		def Key41():
			print("E4")
		def Key42():
			print("F4")
		def Key43():
			print("F#4")
		def Key44():
			print("G4")
		def Key45():
			print("G#4")
		def Key46():
			print("A4")
		def Key47():
			print("A#4")
		def Key48():
			print("B4")

#Octave1
		self.C_0_button = Button(master, bg="white",text="C1", height=10 , width=3, command = Key1)
		self.C_0_button.grid(row=5,column=0)

		self.CC_0_button = Button(master ,bg="black" , fg="white",text="C#1" ,height=10 ,width=2, command = Key2)
		self.CC_0_button.grid(row=1,columnspan=2)

		self.DD_0_button = Button(master ,bg="black" , fg="white",text="D#1" ,height=10 ,width=2, command = Key3)
		self.DD_0_button.grid(row=1,columnspan=4)

		self.D_0_button = Button(master, bg="white", text="D1" ,height=10 , width=3, command = Key4)
		self.D_0_button.grid(row=5 , column=1)

		self.E_0_button = Button(master, bg="white", text="E1" ,height=10 , width=3, command = Key5)
		self.E_0_button.grid(row=5 , column=2)

		self.F_0_button = Button(master, bg="white", text="F1" ,height=10 , width=3, command = Key6)
		self.F_0_button.grid(row=5 , column=3)

		self.FF_0_button = Button(master , bg="black", fg="white",text="F#1" ,height=10 ,width=2, command = Key7)
		self.FF_0_button.grid(row=1,column=3 ,columnspan=2)

		self.G_0_button = Button(master, bg="white",text="G1" ,height=10 , width=3, command = Key8)
		self.G_0_button.grid(row=5 , column=4)

		self.GG_0_button = Button(master,bg="black" ,fg="white",text="G#1" ,height=10 ,width=2, command = Key9)
		self.GG_0_button.grid(row=1, column = 4 , columnspan=2)

		self.A_0_button = Button(master, bg="white",text="A1" ,height=10 , width=3, command = Key10)
		self.A_0_button.grid(row=5 , column=5)

		self.AA_0_button = Button(master,bg="black" ,fg="white",text="A#1" ,height=10 ,width=2, command = Key11)
		self.AA_0_button.grid(row=1, column = 5 , columnspan=2)

		self.B_0_button = Button(master, bg="white",text="B1" ,height=10 , width=3, command = Key12)
		self.B_0_button.grid(row=5 , column=6)


#Octave 2
		self.C_1_button = Button(master, bg="white", text="C2", height=10, width=3, command = Key13)

		self.C_1_button.grid(row=5, column=10)

		self.CC_1_button = Button(master, bg="black", fg="white", text="C#2", height=10, width=2, command = Key14)
		self.CC_1_button.grid(row=1, column = 10, columnspan=4)

		self.DD_1_button = Button(master, bg="black", fg="white", text="D#2", height=10, width=2, command =Key15)
		self.DD_1_button.grid(row=1, column = 12, columnspan=4)

		self.D_1_button = Button(master, bg="white", text="D2", height=10, width=3, command =Key16)
		self.D_1_button.grid(row=5, column=12)

		self.E_1_button = Button(master, bg="white", text="E2", height=10, width=3, command =Key17)
		self.E_1_button.grid(row=5, column=14)

		self.F_1_button = Button(master, bg="white", text="F2", height=10, width=3, command =Key18)
		self.F_1_button.grid(row=5, column=16)

		self.FF_1_button = Button(master, bg="black", fg="white", text="F#2", height=10, width=2, command =Key19)
		self.FF_1_button.grid(row=1, column=16, columnspan=4)

		self.G_1_button = Button(master, bg="white", text="G2", height=10, width=3, command =Key20)
		self.G_1_button.grid(row=5, column=18)

		self.GG_1_button = Button(master, bg="black", fg="white", text="G#2", height=10, width=2, command =Key21)
		self.GG_1_button.grid(row=1, column=18, columnspan=4)

		self.A_1_button = Button(master, bg="white", text="A2", height=10, width=3, command =Key22)
		self.A_1_button.grid(row=5, column=20)

		self.AA_1_button = Button(master, bg="black", fg="white", text="A#2", height=10, width=2, command =Key23)
		self.AA_1_button.grid(row=1, column=20, columnspan=4)

		self.B_1_button = Button(master, bg="white", text="B2", height=10, width=3, command =Key24)
		self.B_1_button.grid(row=5, column=22)


#Octave 3
		self.C_2_button = Button(master, bg="white", text="C3", height=10, width=3, command =Key25)

		self.C_2_button.grid(row=5, column=24)

		self.CC_2_button = Button(master, bg="black", fg="white", text="C#3", height=10, width=2, command =Key26)
		self.CC_2_button.grid(row=1, column=24, columnspan=4)

		self.DD_2_button = Button(master, bg="black", fg="white", text="D#3", height=10, width=2, command =Key27)
		self.DD_2_button.grid(row=1, column=26, columnspan=4)

		self.D_2_button = Button(master, bg="white", text="D3", height=10, width=3, command =Key28)
		self.D_2_button.grid(row=5, column=26)

		self.E_2_button = Button(master, bg="white", text="E3", height=10, width=3, command =Key29)
		self.E_2_button.grid(row=5, column=28)

		self.F_2_button = Button(master, bg="white", text="F3", height=10, width=3, command =Key30)
		self.F_2_button.grid(row=5, column=30)

		self.FF_2_button = Button(master, bg="black", fg="white", text="F#3", height=10, width=2, command =Key31)
		self.FF_2_button.grid(row=1, column=30, columnspan=4)

		self.G_2_button = Button(master, bg="white", text="G3", height=10, width=3, command =Key32)
		self.G_2_button.grid(row=5, column=32)

		self.GG_2_button = Button(master, bg="black", fg="white", text="G#3", height=10, width=2, command =Key33)
		self.GG_2_button.grid(row=1, column=32, columnspan=4)

		self.A_2_button = Button(master, bg="white", text="A3", height=10, width=3, command =Key34)
		self.A_2_button.grid(row=5, column=34)

		self.AA_2_button = Button(master, bg="black", fg="white", text="A#3", height=10, width=2, command =Key35)
		self.AA_2_button.grid(row=1, column=34, columnspan=4)

		self.B_2_button = Button(master, bg="white", text="B3", height=10, width=3, command =Key36)
		self.B_2_button.grid(row=5, column=36)


#Octave 4
		self.C_3_button = Button(master, bg="white", text="C4", height=10, width=3, command =Key37)

		self.C_3_button.grid(row=5, column=38)

		self.CC_3_button = Button(master, bg="black", fg="white", text="C#4", height=10, width=2, command =Key38)
		self.CC_3_button.grid(row=1, column=38, columnspan=4)

		self.DD_3_button = Button(master, bg="black", fg="white", text="D#4", height=10, width=2, command =Key39)
		self.DD_3_button.grid(row=1, column=40, columnspan=4)

		self.D_3_button = Button(master, bg="white", text="D4", height=10, width=3, command =Key40)
		self.D_3_button.grid(row=5, column=40)

		self.E_3_button = Button(master, bg="white", text="E4", height=10, width=3, command =Key41)
		self.E_3_button.grid(row=5, column=42)

		self.F_3_button = Button(master, bg="white", text="F4", height=10, width=3, command =Key42)
		self.F_3_button.grid(row=5, column=44)

		self.FF_3_button = Button(master, bg="black", fg="white", text="F#4", height=10, width=2, command =Key43)
		self.FF_3_button.grid(row=1, column=44, columnspan=4)

		self.G_3_button = Button(master, bg="white", text="G4", height=10, width=3, command =Key44)
		self.G_3_button.grid(row=5, column=46)

		self.GG_3_button = Button(master, bg="black", fg="white", text="G#4", height=10, width=2, command =Key45)
		self.GG_3_button.grid(row=1, column=46, columnspan=4)

		self.A_3_button = Button(master, bg="white", text="A4", height=10, width=3, command =Key46)
		self.A_3_button.grid(row=5, column=48)

		self.AA_3_button = Button(master, bg="black", fg="white", text="A#4", height=10, width=2, command =Key47)
		self.AA_3_button.grid(row=1, column=48, columnspan=4)

		self.B_3_button = Button(master, bg="white", text="B4", height=10, width=3, command =Key48)
		self.B_3_button.grid(row=5, column=50)

root = Tk()
my_gui = PianoGui(root)
root.mainloop()




