from manimlib.imports import *
from random import *

#manim gambler_ruin.py GamblerRuin -pl

class GamblerRuin(Scene):
    def do_anim(self,p = 0.5):
        title = TextMobject("Gambler ruin visualize").shift( UP*3.5)
        self.add(title)
        ptext = TextMobject("p = {}".format(p)).shift(UP * 3)
        self.add(ptext)
        seed(42)
        height = 0.2
        number_point = 15
        clist=[]
        for i in range(number_point):
            clist.append(Dot().shift(UP*(-i*height)))
        g1 = VGroup(*clist)
        self.add(g1)
        
        
        # hyperparam
        n=2
        k = 2*n+1
        poslist = [k //2] * number_point
        # create text coin
        texts = ["0\$", "25\$", "50\$", "75\$", "100\$"]
        tlist = []
        for i,t in enumerate(texts):
            tlist.append(TextMobject(t).shift(RIGHT*2*(i-k//2) + UP))
        gtext = VGroup(*tlist)
        self.add(gtext)
        while (1): 
            count_zero = 0
            count_k = 0
            newposlist = []
            newclist = []
            for i,position in enumerate(poslist):
                if position != 0 and position != k-1:
                    newpos = random()
                    if newpos > p:
                        newpos = position -1
                    else: 
                        newpos = position +1
                    newposlist.append(newpos)
                    newcolor = WHITE
                    if newpos > position:
                        newcolor = GREEN
                    else:
                        newcolor = RED
                    newclist.append(Dot().shift(RIGHT*2*(newpos - k//2) + UP*(-i*height)).set_fill(newcolor))
                else: 
                    newpos = position
                    newposlist.append(newpos)
                    newclist.append(Dot().shift(RIGHT*2*(newpos - k//2) + UP*(-i*height)))
                    if position == 0:
                        count_zero+=1
                    else:
                        count_k +=1

            g2 = VGroup(*newclist)
            self.clear()
            self.add(title)
            self.add(gtext)
            self.add(ptext)
            self.play(Transform(g1,g2))
            clist = newclist
            poslist  = newposlist
            g1 = g2
            if count_k+count_zero ==  number_point:
                break
        
    def construct(self):
        p = [0.5, 0.8, 0.2]
        for pi in p:
            ptext = TextMobject("p = {}".format(pi))
            self.add(ptext)
            self.wait()
            self.clear()
            self.do_anim(pi)
            self.clear()


   
