import tkinter as tk
import random
from PIL import ImageTk,Image

def placep1(): player_1.place(x=player_pos[0]-9,y=player_pos[1]-9)
def placep2(): player_2.place(x=player_pos[2]+16,y=player_pos[3]-9)
def placep3(): player_3.place(x=player_pos[4]-9,y=player_pos[5]+17)
def placep4(): player_4.place(x=player_pos[6]+16,y=player_pos[7]+17)

def code(x):
    
    pass

def decode(x,y):
    pass

def get_choice(value):
    global no_players
    no_players=value

def move(ct):
    # 1 50,30
    pass
    
def roll_dices():
    global Dices,count,player_turn,player_pos
    r = random.randint(1, 6)
    b2 = tk.Button(root, image=Dices[r-1],height=65,width=65)
    b2.place(x=852,y=152)
    count+=r
    
    if(r!=6):
    #    print((player_turn % int(no_players) +1)," ",count)
        move(count)
        
        cur_player = int(player_turn % int(no_players))*2
        x,y=player_pos[cur_player],player_pos[cur_player+1]
        z=int(((x+40)/80) + 10*(9-(y-40)/80)) + count
        print(z)
        
        #check
        if(ar[z]!=-1): z=ar[z]
        
        if(z<100):
            player_pos[cur_player]=(z%10)*80 -40
            player_pos[cur_player+1]=(9-int(z/10))*80 +40
            if(player_pos[0]<0):
                player_pos[cur_player+1]+=80
                player_pos[cur_player]=760
            if((player_turn % int(no_players) +1)==1): placep1()
            if((player_turn % int(no_players) +1)==2): placep2()
            if((player_turn % int(no_players) +1)==3): placep3()
            if((player_turn % int(no_players) +1)==4): placep4()
        if(z==100):
            win.place(x=930, y=95)
            print("win")
            
        player_turn+=1
        count=0
        
        # Player turn button
        if((player_turn % int(no_players) +1)==1):
            if(int(no_players)==2): p2_turn.place(x=-100, y=-100)
            if(int(no_players)==3): p3_turn.place(x=-100, y=-100)
            if(int(no_players)==4): p4_turn.place(x=-100, y=-100)
            p1_turn.place(x=850, y=95)
        if((player_turn % int(no_players) +1)==2):
            p1_turn.place(x=-100, y=-100)
            p2_turn.place(x=850, y=95)
        if((player_turn % int(no_players) +1)==3):
            p2_turn.place(x=-100, y=-100)
            p3_turn.place(x=850, y=95)
        if((player_turn % int(no_players) +1)==4):
            p3_turn.place(x=-100, y=-100)
            p4_turn.place(x=850, y=95)
    
    
def StartGame():
    print("2nd ",no_players)
    if(no_players == "Players"):
        pass
    else:
        w.place(x=-100, y=-100)
        startGame.place(x=-200, y=-200)
        placep1()
        if(int(no_players)>=2): placep2()
        if(int(no_players)>=3): placep3()
        if(int(no_players)==4): placep4()
        
        #Player Turn
        p1_turn.place(x=850, y=95)
        #Screen
        dice_screen = tk.Canvas(root,width=70,height=70)
        dice_screen.create_rectangle(70,70,70,70, fill='white', outline='black')
        dice_screen.place(x=850,y=150)
        #Button
        diceRoll = tk.Button(F1, text="  Roll  ",background='white',command=roll_dices, font=("Helvetica"))
        diceRoll.place(x=850, y=240)
        #Exits
        exit_button = tk.Button(F1, text="Exit",background='white', font=("Helvetica"),command=root.destroy)
        exit_button.place(x=850, y=700)
    
root = tk.Tk()
root.geometry("1000x800")
root.title("Snake and Ladder")

F1=tk.Frame(root,width=1000,height=800,relief='raised',bg="brown")
F1.place(x=0,y=0)

#set Board
img1 = ImageTk.PhotoImage(Image.open("Img.jpg"))
Lab=tk.Label(F1,image=img1)
Lab.place(x=0,y=0)

#player 1 coin
p1_turn = tk.Button(F1, text="Player 1",background='white',command=roll_dices, font=("Helvetica"))
player_1= tk.Canvas(root,width=20,height=20)
player_1.create_oval(1,1,22,22,fill="blue")
player_1.place(x=-100,y=-100)

#player 2 coin
p2_turn = tk.Button(F1, text="Player 2",background='white',command=roll_dices, font=("Helvetica"))
player_2= tk.Canvas(root,width=20,height=20)
player_2.create_oval(1,1,22,22,fill="red")
player_2.place(x=-100,y=-100)

#player 4 coin
p3_turn = tk.Button(F1, text="Player 3",background='white',command=roll_dices, font=("Helvetica"))
player_4= tk.Canvas(root,width=20,height=20)
player_4.create_oval(1,1,22,22,fill="green")
player_4.place(x=-100,y=-100)

#player 3 coin
p4_turn = tk.Button(F1, text="Player 4",background='white',command=roll_dices, font=("Helvetica"))
player_3= tk.Canvas(root,width=20,height=20)
player_3.create_oval(1,1,22,22,fill="yellow")
player_3.place(x=-100,y=-100)

# data variables
no_players="Players"
count=0
player_turn=0
player_pos=[40,760,40,760,40,760,40,760]
z=int(((40+40)/80) + 10*(9-(760-40)/80))
print("st ",z)
#    1  2  3  4  5  6  7  8  9  0
ar=[ 0,-1,-1,-1,-1,-1,27,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,-1,70,
    -1,-1,-1,-1, 5,-1,-1,-1,-1,-1, #2
    -1,-1,-1, 1,-1,55,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,19,-1,-1,-1, #4
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,95,-1,52,-1,-1,98,-1,-1, #6
    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,57,-1,-1,-1,
    61,-1,-1,-1,-1,-1,-1,-1,69,-1,]
win = tk.Button(F1, text="Won",background='white',command=roll_dices, font=("Helvetica"))


# dices img
Dices=[]
names=["d1.jpg","d2.jpg","d3.jpg","d4.jpg","d5.jpg","d6.jpg"]
for i in names:
    dice_img = Image.open(i)
    dice_img.resize((40,40))
    dice_img = ImageTk.PhotoImage(dice_img)
    Dices.append(dice_img)
 
# drop menu
OPTIONS = ["Players", "2", "3", "4"]
variable = tk.StringVar()
variable.set(OPTIONS[0]) # default value
w = tk.OptionMenu(F1,variable, *OPTIONS,command= get_choice)
no_players=variable.get()
w.pack()
w.place(x=850, y=225)
w.config(font=('calibri',(10)),bg='white',width=5)

#Start Game
startGame = tk.Button(F1, text="Start", background='white', font=("Helvetica"),command =  StartGame)
startGame.place(x=850, y=400)




root.mainloop()
