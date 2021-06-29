import turtle
import random

ms = turtle.Screen()
ms.setup(430,630,500,10)
ms.bgcolor('gray')
ms.title('2048小游戏')
ms.tracer(0)
ms.register_shape('bg.gif')       #注册图片
ms.register_shape('title.gif')
ms.register_shape('score.gif')
ms.register_shape('top_score.gif')
ms.register_shape('2.gif')
ms.register_shape('4.gif')
ms.register_shape('8.gif')
ms.register_shape('16.gif')
ms.register_shape('32.gif')
ms.register_shape('64.gif')
ms.register_shape('128.gif')
ms.register_shape('256.gif')
ms.register_shape('512.gif')
ms.register_shape('1024.gif')
ms.register_shape('2048.gif')
ms.tracer(0)

class Block(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def grow(self):                              #随机产生一个2,4
        num = random.choice([2, 2, 4, 2, 4])
        self.shape(f'{num}.gif')
        a = random.choice(allpos)
        self.goto(a)
        allpos.remove(a)
        block_list.append(self)
        ms.update()

    def go_top(self):                      # 向上
        self.go(-50, -150,-250,0,100,True)

    def go_down(self):                     # 向下
        self.go(-150,-50,50,0,-100,True)

    def go_left(self):                      # 向左
        self.go(-50, 50, 150,-100,0,False)

    def go_right(self):                      # 向右
        self.go(50, -50, -150,100,0,False)

    def go(self,a,b,c,px,py,bool):                  #去移动操作的格子
        global move_time,z_bool,score,top_score     #全局变量
        move_time = 0
        block1,block2,block3 = [],[],[]
        if bool is True:                    #用boll去判断是否去移动格子
            for i in  block_list:
                if i.ycor() == a:            #ycor y坐标,移动y
                    block1.append(i)
                if i.ycor() == b:
                    block2.append(i)
                if i.ycor() == c:
                    block3.append(i)
        else:
            for i in  block_list:
                if i.xcor() == a:            #ycor y坐标,移动x
                    block1.append(i)
                if i.xcor() == b:
                    block2.append(i)
                if i.xcor() == c:
                    block3.append(i)
        for j in block1:
            j.move(j.xcor()+px,j.ycor()+py)
        for j in block2:
            for k in range(2):
                j.move(j.xcor()+px,j.ycor()+py)
        for j in block3:
            for  k in range(3):
                j.move(j.xcor()+px,j.ycor()+py)
        if move_time != 0:
            new_block = Block()
            new_block.grow()
        for i in block_list:
            if i.shape() == '2048.gif' and z_bool:
                winlose.show_text('达成2048,按回车继续游戏')
                z_bool = False
        if judge() is False:
            winlose.show_text('游戏结束，重新开始请按空格键')
        bc_score.show_score(score)
        bc_top_score.show_top_score(top_score)


    def move(self,gox,goy):  # 数字移动
        global  move_time,score,top_score       #全局变量
        if (gox, goy) in allpos:             #判断,如果这个方块里面有数字则不产生
            allpos.append(self.pos())
            self.goto(gox,goy)
            allpos.remove(self.pos())
            move_time += 1
        else:
            for i in block_list:
                if i.pos() == (gox,goy) and i.shape() == self.shape():
                    allpos.append(self.pos())
                    self.goto(gox,goy)
                    self.ht()
                    block_list.remove(self)
                    z = int(i.shape()[0:-4])         #把后面四位切掉,合成
                    i.shape(f'{2*z}.gif')
                    move_time += 1
                    score = score + z

        if score > top_score:           #判断如果当前分数大于最高分数，就去代替
            top_score = score

class Background(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def show_text(self):                #画出格子
        self.color('white', 'white')
        self.goto(-215, 120)
        self.begin_fill()
        self.pd()
        self.goto(215, 120)
        self.goto(215, 110)
        self.goto(-215, 110)
        self.end_fill()
        self.penup()
        self.shape('title.gif')
        self.goto(-125, 210)
        self.stamp()
        self.shape('score.gif')
        self.goto(125, 245)
        self.stamp()
        self.shape('top_score.gif')
        self.goto(125, 170)
        self.stamp()

    def show_back(self):
        for i in allpos:
            self.shape('bg.gif')
            self.goto(i)
            self.stamp()

    def show_score(self,score):
        self.write('white')
        self.goto(125, 210)
        self.clear()
        self.write(f'{score}', align='center', font=('Arial', 20, 'bold'))

    def show_top_score(self,top_score):
        self.goto(125, 135)
        self.clear()
        self.write(f'{top_score}', align='center', font=('Arial', 20, 'bold'))

class Winlose(turtle.Turtle):    #输赢，出现2048就去判断赢
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")

    def show_text(self, text):
        self.write(f'{text}', align='center', font=("黑体", 20, "bold"))

def judge():
    judge_a = 0
    if allpos == []:
        for i in block_list:
            for j in block_list:
                if i.shape() == j.shape() and i.distance(j) == 100:
                    judge_a +=1
        if judge_a == 0:
            return  True
        else:
            return  False
    else:
        return True

def init():
    global z_bool,block_list,allpos,score
    z_bool =True
    allpos = [(-150, 50), (-50, 50), (50, 50), (150, 50),
              (-150, -50), (-50, -50), (50, -50), (150, -50),
              (-150, -150), (-50, -150), (50, -150), (150, -150),
              (-150, -250), (-50, -250), (50, -250), (150, -250)]
    for i in block_list:
        i.clear()
        i.ht()
    winlose.clear()
    block_list = []
    block = Block()
    block.grow()
    score = 0



allpos = [(-150, 50), (-50, 50), (50, 50), (150, 50),               #格子的数值
              (-150, -50), (-50, -50), (50, -50), (150, -50),
              (-150, -150), (-50, -150), (50, -150), (150, -150),
              (-150, -250), (-50, -250), (50, -250), (150, -250)]

move_time = 0 #数值为0
back = Background()
back.show_text()
back.show_back()
block_list = []
block = Block()
block.grow()
winlose = Winlose()
z_bool = True
score = 0                       #当前分数0
top_score = 0                   #最高分数0
bc_score = Background()
bc_top_score = Background()
bc_score.show_score(score)
bc_top_score.show_top_score(top_score)



ms.listen()
ms.onkey(block.go_top,'Up')
ms.onkey(block.go_down,'Down')
ms.onkey(block.go_left,'Left')
ms.onkey(block.go_right,'Right')
ms.onkey(winlose.clear,'Return')
ms.onkey(init,'space')

ms.mainloop()