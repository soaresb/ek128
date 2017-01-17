from tkinter import *
import random
import math
while True:
	root=Tk()
	w = Canvas(root, width=600, height=600)
	w.pack()
	root.focus_force()
	class Paddle:

		def left(event):
		    w.move(Paddle.p,-25,0)
		def right(event):
			w.move(Paddle.p,25,0)



		def getPosition(event):
			print(w.coords(Paddle.p))
			return w.coords(Paddle.p)
		#sets starting position of paddle, x1,y1 is the top left corner x2,y2 is bottom right
		x1=270
		y1=580
		x2=330
		y2=590
		#creates paddle
		p= w.create_rectangle(x1, y1, x2, y2, fill="green")
		w.bind('<Right>', right)
		w.bind('<Left>', left) 
		w.bind('<Return>',getPosition)
		w.focus_set()

	class Ball:
		score=0
		x1=292.5
		x2=302.5
		y1=292.5
		y2=302.5
		n=0
		b=w.create_oval(x1, y1, x2, y2, fill = 'purple')
		xmove=random.choice([-3,-2.5,2.5,3])
		ymove=random.choice([-3,-2.5,2.5,3])
		# ymove=-1
		# xmove=0
		if ymove==0:
			ymove=1
		if xmove==0:
			xmove=-1
		# def start(event):
		# 	Ball.ballInteractions()
			
		def ballInteractions():
			w.focus_force()
			if sum(Block.blocks.values())==0:
				winText=w.create_text(300,320,text = ('      You Win!\n Your score was: %s')%(Ball.score), font= ('DFKai-SB',20))
			quadrant=0
			w.move(Ball.b,Ball.xmove,Ball.ymove)
			# root.after(10,Ball.ballInteractions)
			ballCoordinates=(w.coords(Ball.b))
			paddleCoordinates=w.coords(Paddle.p)
			ballXCenter=(ballCoordinates[0]+ballCoordinates[2])/2
			ballYCenter=(ballCoordinates[1]+ballCoordinates[3])/2
			if ballCoordinates[2]>600:
				Ball.xmove= -Ball.xmove-.125
			if ballCoordinates[0]<1:
				Ball.xmove= -Ball.xmove+.125
			if ballCoordinates[1]<0:
				Ball.ymove= -Ball.ymove+.125
			if ballCoordinates[3]>600 and ballCoordinates[3]<620:
				w.delete(Ball.b)
				lossText=w.create_text(300,320,text = ('    Game Over\n Your score was: %s\n Press R to restart')%(Ball.score), font= ('DFKai-SB',20))
			if ballXCenter>paddleCoordinates[0] and ballXCenter<paddleCoordinates[2] and ballCoordinates[3]>=paddleCoordinates[1]:
				Ball.ymove= -Ball.ymove-.125
				if math.fabs(ballXCenter - paddleCoordinates[0])<= 3 or math.fabs(ballXCenter - paddleCoordinates[2]) <= 3:
						Ball.xmove= -Ball.xmove-.125

			# if quadrant!=1 and ballXCenter>300 and ballYCenter<140:
			# 	quadrant=1

			# if quadrant!=2 and ballXCenter<300 and ballYCenter<140:
			# 	quadrant=2

			# if quadrant!=3 and ballXCenter<300 and 140<ballYCenter<300:
			# 	quadrant=3



			# if quadrant!=4 and ballXCenter>300 and ballYCenter>140:
			# 	quadrant=4


			for j in Block.blocks:
				if w.coords(Block.blocks[j]) and w.coords(Block.blocks[j])[0]<=ballXCenter<=w.coords(Block.blocks[j])[2] and w.coords(Block.blocks[j])[1]<=ballYCenter<=w.coords(Block.blocks[j])[3]:
					if math.fabs(ballXCenter - w.coords(Block.blocks[j])[0])<= 5 or math.fabs(ballXCenter - w.coords(Block.blocks[j])[2]) <= 5:
						Ball.xmove= -Ball.xmove-.125
					else:
						Ball.ymove= -Ball.ymove-.125
					w.delete(Block.blocks[j])
					Block.blocks[j]=0
					Ball.score=Ball.score+1
					w.itemconfig(3, text=('Score: %s \nPress shift+Q to quit'%Ball.score))
				
			root.after(10,Ball.ballInteractions)
		# w.bind('<Up>', start)
		scoreText=w.create_text(540,560, text=('Score: %s \nPress shift+Q to quit'%score))
	# 
	class Block:
		Colors=['red','blue','green','yellow','orange']
		# x1=270
		# x2=330
		# y1=200
		# y2=220
		x1=0
		x2=60
		y1=0
		y2=20
		# l=w.create_rectangle(x1,y1,x2,y2, fill ='red')
		blocks={}
		for i in range(1,150):
			# blocks[i]= w.create_rectangle(random.randint(1,70),random.randint(1,70),random.randint(1,70),random.randint(1,70), fill ='blue')
			
				
			blocks[i]=w.create_rectangle(x1,y1,x2,y2, fill =random.choice(Colors))
			x1=x1+60
			x2=x2+60
			if x2==660:
				y1=y1+20
				y2=y2+20
				x1=0
				x2=60
			if random.randint(1,100)>60:
				w.delete(blocks[i])

	def restart(event):
		root.destroy()

	def quit(event):
		sys.exit()

	w.bind('<r>',restart)
	w.bind('<Q>',quit)
	root.after(30,Ball.ballInteractions)
	root.mainloop()



# when a new direction for ball use vector to determine which ones it would hit