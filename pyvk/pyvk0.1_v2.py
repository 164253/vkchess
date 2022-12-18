import pygame
from os.path import dirname
from pyvk_core_v2 import pyvkcorecall,getm,getc,getc2
def output():
    screen.blit(disp,(0,0))
    if getc2("c output"):
        y=dist_hi
        p=80 if ischange else 0
        k=-1 if ischange else 1
        for _ in range(9):
            x=dist_wd
            for j in range(9):
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage{}_{}_{}.png".format(m[p]>>12&3,m[p]>>11&1,m[p]>>10&1)).convert(),bdonet),(x,y))
                x+=bdone
                p+=k
            y+=bdone
        z=c>>23&127
        if z^127:screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImagep{}.png".format((m[z]>>13&1)+(m[z]>>11&1))).convert(),bdonet),(dist_wd+z%9*bdone,dist_hi+z//9*bdone))
        z=c>>16&127
        if z^127:screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImagep{}.png".format((m[z]>>13&1)+(m[z]>>11&1))).convert(),bdonet),(dist_wd+z%9*bdone,dist_hi+z//9*bdone))
    else:screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\boardline.png").convert(),(bdone*9,bdone*9)),(dist_wd,dist_hi))
    hbdonet=(bdone//2,bdone//2)
    p=0
    p=80 if ischange else 0
    k=-1 if ischange else 1
    y=dist_hi
    for _ in range(9):
        x=dist_wd
        for _ in range(9):
            b=m[p]>>14^3 if ischange and m[p]>>14 else m[p]>>14
            if m[p]&0x3e0:
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage{}_{}.png".format(m[p]>>5&0x1f,b)).convert_alpha(),hbdonet),(x+bdone//4,y if b==1 else y+bdone//2))
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage{}_{}.png".format(m[p]&0x1f,b)).convert_alpha(),hbdonet),(x+bdone//4,y+bdone//2 if b==1 else y))
            else:screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage{}_{}.png".format(m[p]&0x1f,b)).convert_alpha(),bdonet),(x,y))
            x+=bdone
            p+=k
        y+=bdone
    i=apple
    j=289*ischange
    while i:
        if i&1:screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage-1_1.png").convert_alpha(),hbdonet),(dist_wd+(bdone*(j%17*2+1)>>2),dist_hi+(bdone*(j//17*2+1)>>2)))
        i>>=1
        j=j-1 if ischange else j+1
    pygame.draw.line(screen,(0,0,0),[dist_wd,dist_hi+9*bdone],[dist_wd+9*bdone,dist_hi+9*bdone],linewd)
    pygame.draw.line(screen,(0,0,0),[dist_wd+9*bdone,dist_hi],[dist_wd+9*bdone,dist_hi+9*bdone],linewd)
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\undo.png").convert(),(bdone,bdone)),(int(-1.5*bdone+dist_wd),8*bdone+dist_hi))
    pygame.draw.line(screen,(0,0,0),[int(-0.5*bdone+dist_wd),8*bdone+dist_hi],[int(-0.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(-1.5*bdone+dist_wd),9*bdone+dist_hi],[int(-0.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\change.png").convert(),bdonet),(int(-1.5*bdone+dist_wd),int(6.5*bdone+dist_hi)))
    pygame.draw.line(screen,(0,0,0),[int(-0.5*bdone+dist_wd),int(6.5*bdone+dist_hi)],[int(-0.5*bdone+dist_wd),int(7.5*bdone+dist_hi)],linewd)
    pygame.draw.line(screen,(0,0,0),[int(-1.5*bdone+dist_wd),int(7.5*bdone+dist_hi)],[int(-0.5*bdone+dist_wd),int(7.5*bdone+dist_hi)],linewd)
    screen.blit(first if ischange else second,(int(-1.5*bdone+dist_wd),dist_hi))
    screen.blit(second if ischange else first,(int(9.5*bdone+dist_wd),8*bdone+dist_hi))
    pygame.draw.line(screen,(0,0,0),[int(-0.5*bdone+dist_wd),dist_hi],[int(-0.5*bdone+dist_wd),bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(-1.5*bdone+dist_wd),bdone+dist_hi],[int(-0.5*bdone+dist_wd),bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(10.5*bdone+dist_wd),8*bdone+dist_hi],[int(10.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(9.5*bdone+dist_wd),9*bdone+dist_hi],[int(10.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    pygame.display.update()

pygame.init()
scwd=int(780)
schi=int(780)
bdone=scwd//10 if schi//13>scwd//10 else schi//13
bdonet=(bdone,bdone)
bdwd=bdhi=bdone*9
dist_wd=(scwd-bdwd)//2
dist_hi=(schi-bdhi)//2
linewd=bdone//128 or 1
screen=pygame.display.set_mode((scwd,schi))
pygame.display.set_caption("科摩多龍棋")
dir=dirname(__file__)
icon=pygame.image.load(dir+"\\vkImage1_1.png")
first=pygame.transform.scale(pygame.image.load(dir+"\\first.png").convert(),bdonet)
second=pygame.transform.scale(pygame.image.load(dir+"\\second.png").convert(),bdonet)
pygame.display.set_icon(icon)
disp=pygame.Surface(screen.get_size()).convert()
disp.fill((255,255,255))
screen.blit(disp,(0,0))
pygame.event.set_blocked(pygame.MOUSEMOTION)
m=[
0x8007,0x8005,0x8004,0x8002,0x8001,0x8002,0x8004,0x8005,0x8006,
     0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
     0,0x4008,     0,     0,     0,     0,0x4009,0x4009,     0,
0x4006,0x4005,0x4004,0x4002,0x4001,0x4002,0x4004,0x4005,0x4007,
0x21,0x3fff,0x7f7f,0,0,0,0,0,0,0,0]
'''
m=0
for i,val in enumerate([
0x8007,0x8005,0x8004,0x8002,0x8001,0x8002,0x8004,0x8005,0x8006,
     0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,0x416b,     0,     0,
0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
     0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
0x4006,0x4005,0x4004,0x4002,0x4001,0x4002,0x4004,0x4005,0x4007,
0x21,0x3fff,0x7f7f,0,0,0,0,0,0,0,0]):
    m|=val<<(i<<16)
'''
c=0x3fff7f7f
apple=1<<119|1<<123|1<<131|1<<135|1<<157|1<<165|1<<169
ffox=0
eta=[0]*8
m,c,apple,ffox,eta=pyvkcorecall(m,c,apple,ffox,eta,0,9)
lm=[0]*88
tm=[0]*88
for i in range(88):lm[i]=m[i]
ischange=False
output()
noquit=True
'''
def depri():
    for i in range(9):
        for j in range(9):
            print(lm[i*9+j],end=" ")
        print()
    for i in range(9):
        for j in range(9):
            print(m[i*9+j],end=" ")
        print()
    for i in range(9):
        for j in range(9):
            print(nm[i*9+j],end=" ")
        print()
    print()
'''
while getc2("keep game"):
    if getc("born"):
        if getc("t")^ischange:
            pygame.draw.line(screen,(0,0,0),[dist_wd-int(0.5*bdone),dist_hi-int(0.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi-int(0.5*bdone)],linewd)
            pygame.draw.line(screen,(0,0,0),[dist_wd+int(9.5*bdone),dist_hi-int(1.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi-int(0.5*bdone)],linewd)
            for i in range(1,11):
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage0_0_0.png").convert(),bdonet),(dist_wd+int((9.5-i)*bdone),dist_hi-int(1.5*bdone)))
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage{}_{}.png".format(i,getc("t")+1)).convert_alpha(),bdonet),(dist_wd+int((9.5-i)*bdone),dist_hi-int(1.5*bdone)))
        else:
            pygame.draw.line(screen,(0,0,0),[dist_wd-int(0.5*bdone),dist_hi+int(10.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi+int(10.5*bdone)],linewd)
            pygame.draw.line(screen,(0,0,0),[dist_wd+int(9.5*bdone),dist_hi+int(9.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi+int(10.5*bdone)],linewd)
            for i in range(1,11):
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage0_0_0.png").convert(),bdonet),(dist_wd+int((i-1.5)*bdone),dist_hi+int(9.5*bdone)))
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\vkImage{}_{}.png".format(i,getc("t")+1)).convert_alpha(),bdonet),(dist_wd+int((i-1.5)*bdone),dist_hi+int(9.5*bdone)))
        pygame.display.update()
    event=pygame.event.wait()
    if event.type==pygame.QUIT:
        noquit=False
        pygame.quit()
        break
    elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        if (-1.5*bdone+dist_wd<event.pos[0]<-0.5*bdone+dist_wd) and (8*bdone+dist_hi<event.pos[1]<9*bdone+dist_hi):
            # depri()
            for i in range(88):m[i],lm[i]=lm[i],m[i]
            m,c,apple,ffox,eta=pyvkcorecall(m,c,apple,ffox,-1,m,apple)
            # depri()
            output()
        elif (-1.5*bdone+dist_wd<event.pos[0]<-0.5*bdone+dist_wd) and (6.5*bdone+dist_hi<event.pos[1]<7.5*bdone+dist_hi):
            ischange=not ischange
            output()
        else:
            if getc("born"):
                while getc("born"):
                    if event.type==pygame.QUIT:
                        noquit=False
                        pygame.quit()
                        break
                    elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        if getc("t")^ischange:
                            x=int(event.pos[0]-dist_wd+0.5*bdone)
                            y=int(event.pos[1]-dist_hi+1.5*bdone)
                            if 0<x and x<10*bdone and 0<y and y<bdone:
                                m,c,apple,ffox,eta=pyvkcorecall(m,c,apple,ffox,eta,1,10-int(x//bdone))
                        else:
                            x=int(event.pos[0]-dist_wd+0.5*bdone)
                            y=int(event.pos[1]-dist_hi-9.5*bdone)
                            if 0<x and x<10*bdone and 0<y and y<bdone:
                                m,c,apple,ffox,eta=pyvkcorecall(m,c,apple,ffox,eta,1,1+int(x//bdone))
                    event=pygame.event.wait()
            else:
                for i in range(88):tm[i]=m[i]
                x=event.pos[0]-dist_wd
                y=event.pos[1]-dist_hi
                if x>=0 and x<bdwd and y>=0 and y<bdhi:
                    nm=x//bdone+y//bdone*9
                    if y%bdone<bdone//2:nm|=0x80
                    if getc("t"):nm^=0x80
                    if ischange:
                        nm=80-(nm&0x7f)
                        nm^=0x80
                    m,c,apple,ffox,eta=pyvkcorecall(m,c,apple,ffox,eta,(ffox!=0)<<1,nm)
                if getc2("m change"):
                    for i in range(88):lm[i]=tm[i]
            output()
if noquit:
    output()
    if getc("t"):
        screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\win.png").convert(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi+int(9.5*bdone)))
        screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\lose.png").convert(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi-int(1.5*bdone)))
    else:
        screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\lose.png").convert(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi+int(9.5*bdone)))
        screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\win.png").convert(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi-int(1.5*bdone)))
    pygame.display.update()
    while 1:
        event=pygame.event.wait()
        if event.type==pygame.QUIT:pygame.quit()
