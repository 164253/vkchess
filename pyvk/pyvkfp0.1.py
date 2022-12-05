def getmap(map,pos,type):return map>>(pos<<4)>>{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10,"have chess":0}[type]&{"b":3,"me":3,"p":1,"e":1,"up":0x1f,"down":0x1f,"c":0xf,"have chess":0x3ff}[type]
def setmap(map,pos,type,value):return map&{"b":0x3fff,"me":0xcfff,"p":0xf7ff,"e":0xfbff,"up":0xfc1f,"down":0xffe0,"c":0xc3ff}[type]<<(pos<<4)|value<<{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10}[type]<<(pos<<4)
def getflags(flags,type):return flags>>{"t":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0}[type]&{"t":1,"zu":0x7f,"zd":7,"mouseup":1,"mouse":7,"tagup":1,"tag":7}[type]
def setflags(flags,type,value):return flags&{"t":0x3fffffff,"zu":0x407fffff,"zd":0x7f80ffff,"mouseup":0x7fff7fff,"mouse":0x7fff80ff,"tagup":0x7fffff7f,"tag":0x7fffff80}[type]|value<<{"t":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0}[type]
def vkclick(call_type,*args):return {-1:undo,0:first_click,1:second_click,2:born}[call_type](*args)

def undo(map,apple,pre_map,pre_apple):#return call_type(always0),map,flags(always0x3fff7f7f),apple
    #此處傳入pre_map,pre_apple再傳回看似無意義
    #但未來會改為傳入map和一步棋譜(pre_move) 解析後再回傳
    #為了統一化undo操作才這樣寫
    map=pre_map
    apple=pre_apple
    return 0,map,0x3fff7f7f,apple

def first_click(map,apple,pos):#return call_type(always1),map,flags,apple
    flags=0x3fff0000|pos<<8
    if not getmap(map,pos,"up"):flags=setflags(flags,"mouseup",0)
    for i in range(81):map=setmap(map,i,"c",0)
    select_chess(map,[0]*8,flags,getmap(map,pos&0x7f,"up"if pos&0x80 else"down"))
    flags|=pos
    return 1,map,flags,apple

def select_chess(map,eta,flags,who):
    t=getflags(flags,"t")
    s=getflags(flags,"mouse")
    if who==16:
        for i in range(s-9,-1,-9):
            if getmap(map,i,"b")==2-t: #敵人
                if foot_turtle(i,s):setflags(flags,"zu",i)
                break
        for i in range(s+9,81,9):
            if getmap(map,i,"b")==2-t: #敵人
                if foot_turtle(i,s):setflags(flags,"zd",i)
                break
    l=((-10,0),(-9,1),(-8,2),(-1,3),(1,4),(8,5),(9,6),(10,7))
    if who==1 or who==2 or who==13 or who==14 or who==15 or who==16:
        if who!=2:for x,epa in l[3:5]:move(s+x,s,epa)
        for x,epa in l[0:3]+l[5:8]:move(s+x,s,epa)
    elif who==3:for x,epa in l[0]+l[2:6]+l[7]:move(s+x,s,epa)
    elif who==4 or who==10:move(s+9,s,6) if t else move(s-9,s,1)
    elif who==5:for x,epa in l[1]+l[3:5]+l[6]:move(s+x,s,epa)
    elif who==6:
        for x,epa in (l[0:3] if t else l[5:8]):
            i,j=s,1
            while j&1:j,i=move(i+x,i,epa|j<<2&0x18),i+x #所有loop mo都是先&在|
    elif who==7:
        for x,epa in (l[:3:2] if t else l[5::2])
            j,i=move(s+x,s,epa),s+x
            while j&1:j,i=move(i+9 if t else i-9,i,epa|j<<2&0x18),(i+9 if t else i-9) #所有loop mo都是先&在|
    elif who==8:
        for x,epa in l[1]+l[6]:move(s+x,s,epa)
        for x,epa in l[3:5]:
            i,j=s,1
            while j&1:j,i=move(i+x,i,epa|j<<2&0x18),i+x
    elif who==9 or who==18:
        p=getmap(map,s,"up") and not getflags(flags,"mouseup") #will p
        i=s-9
        j=1
        while i>=0:
            ap=is_apple(i+9,i)
            if ap!=8:
                j=7 if p else 5
                eta[1]|=1<<ap
            if getmap(map,i,"have chess"):
                i-=9
                break
            i-=9
        while i>=0:
            j=move(i,i+9,1|j<<2&0x18)
            i-=9
        i=s+9
        j=1
        while i<81:
            ap=is_apple(i-9,i)
            if ap!=8:
                j=7 if p else 5
                eta[6]|=1<<ap
            if getmap(map,i,"have chess"):
                i+=9
                break
            i+=9
        while i<81:
            j=move(i,i-9,6|j<<2&0x18)
            i+=9
        i=s-1
        j=1
        while (i+1)%9:
            ap=is_apple(i+1,i)
            if ap!=8:
                j=7 if p else 5
                eta[3]|=1<<ap
            if getmap(map,i,"have chess"):
                i-=1
                break
            i-=1
        while (i+1)%9:
            j=move(i,i+1,3|j<<2&0x18)
            i-=1
        i=s+1
        j=1
        while i%9:
            ap=is_apple(i-1,i)
            if ap!=8:
                j=7 if p else 5
                eta[4]|=1<<ap
            if getmap(map,i,"have chess"):
                i+=1
                break
            i+=1
        while i%9:
            j=move(i,i-1,4|j<<2&0x18)
            i+=1
    elif who==17:
        for i in range(81):
            if getmap(map,i,"have chess")>>14==t+1 and s!=i:getmap(map,i,"have chess")|=0x1000
    elif who==19:
        for k1,k2 in [[-9,1],[-1,3],[1,4],[9,6]]:
            i=s
            j=1
            while j&1:
                j=move(i+k1,i,k2|j<<2&0x18)
                i+=k1

def foot_turtle():pass

def move():pass

def is_apple():pass

def second_click():pass

def born():pass
