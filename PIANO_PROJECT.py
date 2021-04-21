from tkinter import *
import pygame.midi

init = 0

class PianoGui:
	def colorchange(self, button):
		self.master.after(200, lambda: button.config(background="green"))
		self.master.after(400, lambda: button.config(background="white"))
	def __init__(self, master):
		global init
		self.master = master
		master.title("STUDY CHORDS")
		self.Label = Label(master , borderwidth=1, relief="raised", text="PIANO")
		self.Label.grid(row=0 , columnspan=55)
		if init == 0:
			pygame.init()
			pygame.midi.init()
			print("initialized")
			input_id = pygame.midi.get_default_input_id()
			print(pygame.midi.get_device_info(input_id))
			self.midi_input = pygame.midi.Input(input_id)
			init = 1









#Octave1
		self.C_0_button = Label(master, bg="white",borderwidth=1, relief="raised", text="C1", height=10 , width=3)
		self.C_0_button.grid(row=5,column=0)

		self.CC_0_button = Label(master ,bg="black" , fg="white",borderwidth=1, relief="raised", text="C#1" ,height=10 ,width=2)
		self.CC_0_button.grid(row=1,columnspan=2)

		self.DD_0_button = Label(master ,bg="black" , fg="white",borderwidth=1, relief="raised", text="D#1" ,height=10 ,width=2)
		self.DD_0_button.grid(row=1,columnspan=4)

		self.D_0_button = Label(master, bg="white", borderwidth=1, relief="raised", text="D1" ,height=10 , width=3)
		self.D_0_button.grid(row=5 , column=1)

		self.E_0_button = Label(master, bg="white", borderwidth=1, relief="raised", text="E1" ,height=10 , width=3)
		self.E_0_button.grid(row=5 , column=2)

		self.F_0_button = Label(master, bg="white", borderwidth=1, relief="raised", text="F1" ,height=10 , width=3)
		self.F_0_button.grid(row=5 , column=3)

		self.FF_0_button = Label(master , bg="black", fg="white",borderwidth=1, relief="raised", text="F#1" ,height=10 ,width=2)#, command = Key7)
		self.FF_0_button.grid(row=1,column=3 ,columnspan=2)

		self.G_0_button = Label(master, bg="white",borderwidth=1, relief="raised", text="G1" ,height=10 , width=3)#, command = Key8)
		self.G_0_button.grid(row=5 , column=4)

		self.GG_0_button = Label(master,bg="black" ,fg="white",borderwidth=1, relief="raised", text="G#1" ,height=10 ,width=2)#, command = Key9)
		self.GG_0_button.grid(row=1, column = 4 , columnspan=2)

		self.A_0_button = Label(master, bg="white",borderwidth=1, relief="raised", text="A1" ,height=10 , width=3)#, command = Key10)
		self.A_0_button.grid(row=5 , column=5)

		self.AA_0_button = Label(master,bg="black" ,fg="white",borderwidth=1, relief="raised", text="A#1" ,height=10 ,width=2)#, command = Key11)
		self.AA_0_button.grid(row=1, column = 5 , columnspan=2)

		self.B_0_button = Label(master, bg="white",borderwidth=1, relief="raised", text="B1" ,height=10 , width=3)#, command = Key12)
		self.B_0_button.grid(row=5 , column=6)


#Octave 2
		self.C_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="C2", height=10, width=3)#, command = Key13)

		self.C_1_button.grid(row=5, column=10)

		self.CC_1_button = Label(master, bg="black", fg="white", borderwidth=1, relief="raised", text="C#2", height=10, width=2)#, command = Key14)
		self.CC_1_button.grid(row=1, column = 10, columnspan=4)

		self.DD_1_button = Label(master, bg="black", fg="white", borderwidth=1, relief="raised", text="D#2", height=10, width=2)#,15)
		self.DD_1_button.grid(row=1, column = 12, columnspan=4)

		self.D_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="D2", height=10, width=3)#,16)
		self.D_1_button.grid(row=5, column=12)

		self.E_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="E2", height=10, width=3)#,17)
		self.E_1_button.grid(row=5, column=14)

		self.F_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="F2", height=10, width=3)#,18)
		self.F_1_button.grid(row=5, column=16)

		self.FF_1_button = Label(master, bg="black", fg="white", borderwidth=1, relief="raised", text="F#2", height=10, width=2)#,19)
		self.FF_1_button.grid(row=1, column=16, columnspan=4)

		self.G_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="G2", height=10, width=3)#,20)
		self.G_1_button.grid(row=5, column=18)

		self.GG_1_button = Label(master, bg="black", fg="white", borderwidth=1, relief="raised", text="G#2", height=10, width=2)#,21)
		self.GG_1_button.grid(row=1, column=18, columnspan=4)

		self.A_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="A2", height=10, width=3)#,22)
		self.A_1_button.grid(row=5, column=20)

		self.AA_1_button = Label(master, bg="black", fg="white", borderwidth=1, relief="raised", text="A#2", height=10, width=2)#,23)
		self.AA_1_button.grid(row=1, column=20, columnspan=4)

		self.B_1_button = Label(master, bg="white", borderwidth=1, relief="raised", text="B2", height=10, width=3)#,24)
		self.B_1_button.grid(row=5, column=22)


def change_background(label, color):
	bg = label.cget("background")
	label.configure(background=color)
	label.after(100, lambda color=bg: label.configure(background=color))


def read_midi_event(Piano, midi_input, count, notes, Piano_Dict, root):


	# end the program if you've already played all the notes
	if count >= len(notes):
		root.quit()
		root.destroy()
		return
	key = 0


	# Poll the midi keyboard and read a midi event. Save the event to <midi_note>.
	going = True
	count_temp = 0
	while going:
		if midi_input.poll():
			midi_events = midi_input.read(10)
			print("HERE: {}".format(midi_events))
			print("full midi_events:" + str(midi_events))
			key = midi_events[0][0][1]
			print(key)
			key_button = Piano_Dict.get(int(key))
			count_temp += 1
		if count_temp >= 2:
			going = False



	# if/else state to compare correct key with <midi_note>

	print(count)
	if key == 0:  # make sure the piano key is valid
		#print("Key invalid")
		root.after(0, lambda: read_midi_event(Piano, midi_input, count, notes, Piano_Dict, root))
	elif key == (notes[count]):
		root.after(0, change_background(key_button, "green"))
		count += 1
		root.after(150, lambda: read_midi_event(Piano, midi_input, count, notes, Piano_Dict, root))
	else:
		root.after(0, change_background(key_button, "red"))
		count += 1
		root.after(150, lambda: read_midi_event(Piano, midi_input, count, notes, Piano_Dict, root))


def get_midi_event(midi_input):
	if midi_input.poll():
		midi_events = midi_input.read(10)
		key = midi_events[0][1]
		key_button = Piano_Dict.get(key)
		if key == key_button:
			self.colorchange(key_button)


		#compare key to truth value and if matches key button turn green and if doesn't key turns red





def pianomain():
	root = Tk()
	#building gui
	my_gui = PianoGui(root)
	#Mapping Midi Keys to Gui keys
	notes = [48, 49, 50, 51, 52, 53, 54, 55]
	count = 0
	Piano_Dict = {48: my_gui.C_0_button, 49: my_gui.CC_0_button, 50: my_gui.D_0_button, 51: my_gui.DD_0_button, 52: my_gui.E_0_button, 53: my_gui.F_0_button, 54: my_gui.FF_0_button, 55: my_gui.G_0_button, 56: my_gui.GG_0_button, 57: my_gui.A_0_button, 58: my_gui.AA_0_button, 59: my_gui.B_0_button, 60: my_gui.C_1_button, 61: my_gui.CC_1_button,
				  62: my_gui.D_1_button, 63: my_gui.DD_1_button,
				  64: my_gui.E_1_button, 65: my_gui.F_1_button,
				  66: my_gui.FF_1_button, 67: my_gui.G_1_button,
				  68: my_gui.GG_1_button, 69: my_gui.A_1_button,
				  70: my_gui.AA_1_button, 71: my_gui.B_1_button,}
	# pygame.init()
	# pygame.midi.init()
	# input_id = pygame.midi.get_default_input_id()
	# midi_input = pygame.midi.Input(input_id)
	root.after(100, lambda: read_midi_event(my_gui, my_gui.midi_input, count, notes, Piano_Dict, root))
	root.mainloop()





