#<========== import all the modules here =============> 
from tkinter import* # tkinter module
from PIL import ImageTk,Image # image module
import os # modules to interact with operating system
from pygame import mixer # module to play the music
from tkinter.filedialog import askdirectory # import fuction to open directory on system
mixer.init() #<============= initialize pygame mixer modlule ===========>

def Display_root():
	#<========= making local variable accessable in another scope ==========>
	global root,music_logo,play_logo,pause_logo
	global next_logo,back_logo,display_bg
	#<============== creating window ================>
	root = Tk()
	#<============ seting the size of window =========>
	root.geometry("835x468+335+172")
	#<========== setting title to window ===========>
	root.title("MUSIC PLAYER")
	#<========== setting background color of window =============>
	root.config(bg="white")
	#<================= disabled window to expand more than it setting value ===========>
	root.resizable(width=NO,height=NO)
	#<=============== creating images =============>
	bg = ImageTk.PhotoImage(Image.open("image/bg.jpg"))
	music_logo = ImageTk.PhotoImage(Image.open("image/image2.jpg"))
	play_logo = ImageTk.PhotoImage(Image.open("image/play_logo.png"))
	pause_logo = ImageTk.PhotoImage(Image.open("image/pause_logo.png"))
	next_logo = ImageTk.PhotoImage(Image.open("image/next_logo.png"))
	back_logo = ImageTk.PhotoImage(Image.open("image/back_logo.png"))
	#<============ set image as window background ================>
	display_bg = Label(root,image=bg)
	display_bg.place(x=7,y=0,width=820,height=460)
	#<============= calling display frames here ================>
	Display_frames()
	#<=========== making window to display untill user exut it ================>
	root.mainloop()

#<=========== function to load the music ============>
def LoadMusic_button():
	global list_music,bn
	#< ask user to choose directory of musics ==========>
	direcory = askdirectory()
	#< change directory to current directory ============>
	os.chdir(direcory)
	#< =========  list all the musics in current directory ===============>
	list_music = os.listdir()
	#<========= loop for all musics ==============>
	for item in list_music:
		pos = 0
		#<========== insert it to the variable hold listbox widget ============>
		play_list.insert(pos,item)
		pos += 1
	#<========== it contains: first song position, total number of songs in current directory, and key value to play and unpause the music=========>
	bn = {"next_no":len(list_music)-1,"back_no":0,"unpause":0}
#<============ function to next the music ===================>
def next_music():	
	#<======== change music when the button clicked ===========>
	mixer.music.load(list_music[bn["next_no"]])
	mixer.music.play()
	music_title.configure(text=list_music[bn["next_no"]])
	#<======= if it is last music play, it shouldn't next ============>
	if bn["next_no"] == 0:
		bn["back_no"] = 0
		back_img_bt.configure(state=ACTIVE)
		next_img_bt.configure(state=DISABLED)
	#<========== increased the postion of music ==============>
	bn["next_no"] -= 1
#<============= back button function ============>
def back_music():
	mixer.music.load(list_music[bn["back_no"]])
	mixer.music.play()
	music_title.configure(text=list_music[bn["back_no"]])
	if bn["back_no"] ==  len(list_music)-1:
		bn["next_no"] = len(list_music) -1
		next_img_bt.configure(state=ACTIVE)
		back_img_bt.configure(state=DISABLED)
	bn["back_no"] += 1
#<=========== music play function ============>
def Play_music():
	#<======== get the current selected song in listbox ============>
	if bn["unpause"] == 0:
		mixer.music.load(play_list.get(ACTIVE))
		music_title.configure(text=play_list.get(ACTIVE))
	#<============ play the music get ===========>
		mixer.music.play()
	else:
		mixer.music.unpause()
	bn["unpause"] += 1
#<======= function to change the volume of music =========>
def music_volume(x):	
	#<=========== set the current value of scale wiget to new volume value ===========>
	mixer.music.set_volume(my_scale.get())
#<========== function to pause the music ===========>
def pause_music():
	mixer.init()
	mixer.music.pause()	
def Display_frames():
	#<========= making local variable accessable in another scope ==========>
	global music_title,my_scale,play_list
	global back_img_bt,next_img_bt
	frame = Frame(display_bg,bg="white",)
	frame.place(x=85,y=33,width=650,height=400)
	sub_frame1 = Frame(frame,bg="#7F7F7F",bd=3,relief=GROOVE)
	sub_frame1.place(x=10,y=10,width=440,height=300)
	#<================ small image and title  on sub_frame1 widget ==============>
	image2 = Label(sub_frame1,image=music_logo)
	image2.place(x=6,y=10,width=422,height=250)
	label = Label(sub_frame1,text="MUSIC MP3 PLAYER",bg="white",fg="blue",font=("times new roman",15,"bold"))
	label.place(x=12,y=261,width=410,height=30)

	music_title = Label(frame,bg="white",font=("Verdana",10,"bold"))
	music_title.place(x=12,y=315)

	sub_frame2 = Frame(frame,bg="#7F7F7F",bd=3,relief=GROOVE)
	sub_frame2.place(x=460,y=10, width=184,height=386)
	#<============= songs list frame to hold listbox widget ================>
	music_list_frame = Frame(sub_frame2,bg="white")
	music_list_frame.place(x=3,y=10,width=171,height=365)
	#<================ Vertical and horizontal scrollbars ===============>
	y_scrollbar = Scrollbar(music_list_frame,orient=VERTICAL)
	x_scrollbar = Scrollbar(music_list_frame,orient=HORIZONTAL)
	y_scrollbar.pack(side=RIGHT,fill="y")
	x_scrollbar.pack(side=BOTTOM,fill="x")
	#<================= listbox to hold all the songs list ================>
	play_list = Listbox(music_list_frame,bg="white",font=("Verdana",8,"bold"),selectmode= SINGLE,
				height=365,yscrollcommand=y_scrollbar.set,xscrollcommand=x_scrollbar.set)
	y_scrollbar.configure(command=play_list.yview)
	x_scrollbar.configure(command=play_list.xview)
	play_list.pack(side=LEFT) 
	#<================= Frame to hold all the buttons widget ==================>
	button_frame= Frame(frame,bg="white",bd=4,relief=RIDGE)
	button_frame.place(x=10,y=345,width=440,height=50)
	ld_bt = Button(button_frame,text="Load Songs",fg="white",bg="green",pady=5,font=("Verdana",13,"bold"),command=LoadMusic_button)
	ld_bt.place(x=0,y=0,width=124)

	#<================== all buttons created ===========================>
	back_img_bt = Button(button_frame,image=back_logo,command=back_music)
	back_img_bt.place(x=130,y=0)
	pause_img_bt = Button(button_frame,image=pause_logo,command=pause_music)
	pause_img_bt.place(x=180,y=0)
	play_img_bt = Button(button_frame,image=play_logo,command=Play_music) 
	play_img_bt.place(x=230,y=0)
	next_img_bt = Button(button_frame,image=next_logo,command=next_music)	
	next_img_bt.place(x=280,y=0)
	#<==================  scale to  reduce and increase volume of music ====================>
	my_scale = Scale(button_frame,from_=0.1,to=1,resolution=0.1,orient=HORIZONTAL,bg="white",command=music_volume)

	my_scale.place(x=325,y=0)
print(Display_root())