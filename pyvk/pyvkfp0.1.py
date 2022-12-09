def getmap(map,pos,type):return map>>(pos<<4)>>{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10,"have chess":0}[type]&{"b":3,"me":3,"p":1,"e":1,"up":0x1f,"down":0x1f,"c":0xf,"have chess":0x3ff}[type]
def setmap(map,pos,type,value):return map&{"b":0x3fff,"me":0xcfff,"p":0xf7ff,"e":0xfbff,"up":0xfc1f,"down":0xffe0,"c":0xc3ff}[type]<<(pos<<4)|value<<{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10}[type]<<(pos<<4)
def getflags(flags,type):return flags>>{"t":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0}[type]&{"t":1,"zu":0x7f,"zd":7,"mouseup":1,"mouse":7,"tagup":1,"tag":7}[type]
def setflags(flags,type,value):return flags&{"t":0x3fffffff,"zu":0x407fffff,"zd":0x7f80ffff,"mouseup":0x7fff7fff,"mouse":0x7fff80ff,"tagup":0x7fffff7f,"tag":0x7fffff80,"mouse,up":0x7fff00ff,"tag,up":0x7fffff00}[type]|value<<{"t":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0,"mouse,up":8,"tag,up":0}[type]
def geteta(eta,pos):return eta>>(pos<<3)&0xff
def seteta(eta,pos,value):return eta^geteta(eta,pos)|value<<(pos<<3)
def getapple(apple,pos):return apple>>pos&1
def setapple(apple,pos,value):return apple^(getapple(apple,pos)^value)<<pos
def vkclick(call_type,*args):return {-1:undo,0:first_click,1:second_click,2:born}[call_type](*args)

def undo(map,apple,pre_map,pre_apple):#return call_type(always0),map,eta(always0),flags(always0x3fff7f7f),apple
    #此處傳入pre_map,pre_apple再傳回看似無意義
    #但未來會改為傳入map和一步棋譜(pre_move) 解析後再回傳
    #為了統一化undo操作才這樣寫
    map=pre_map
    apple=pre_apple
    return 0,map,0,0x3fff7f7f,apple

def first_click(map,apple,pos):#return call_type(always1),map,eta,flags,apple
    flags=setflags(setflags(flags,"mouse,up",pos),"tag,up",pos)
    if not getmap(map,pos,"up"):flags=setflags(flags,"mouseup",0)
    for i in range(81):map=setmap(map,i,"c",0)
    return 1,select_chess(map,flags,getmap(map,pos&0x7f,"up"if pos&0x80 else"down"))

def select_chess(map,flags,who):
    eta=0
    t=getflags(flags,"t")
    s=getflags(flags,"mouse")
    if who==16:
        for stop,x,flags_type in ((-1,-9,"zu"),(81,9,"zd")):
            for i in range(s+x,stop,x):
                if getmap(map,i,"b")==2-t: #敵人
                    if foot_turtle(i,s):setflags(flags,flags_type,i)
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
        for stop,x,epa in (((lambda x:x>=0)+l[1]),((lambda x:x<81)+l[6]),((lambda x:(x+1)%9)+l[3]),((lambda x:x%9)+l[4]))
            j,i=1,s+x
            while stop(i):
                ap,i=is_apple(apple,i+x,i),i+x
                if ap!=8:
                    j=7 if p else 5
                    seteta(eta,epa,1<<ap)
                if getmap(map,i-x,"have chess"):break
            while i>=0:j,i=move(i,i+9,epa|j<<2&0x18),i+x
    elif who==17:for i in range(81):if getmap(map,i,"have chess")==t+1 and s!=i:setmap(map,i,"me",1)
    elif who==19:
        for x,epa in l[1:4:2]+l[4:7:2]:
            i,j=s,1
            while j&1:j,i=move(i+x,i,epa|j<<2&0x18),i+x
    return map,eta,flags,apple

def foot_turtle():pass

def move_limit(end,start):pass

def move(map,flags,eta,end,start,epa): #e=evolution p=ispoison a=whichEta #return &1keep &2p &4e
    mou=getflags(flags,"mouse")
    if move_limit(end,start):
        if getmap(map,end,"b")==2-getflags(flags,"t") #敵人 #吃人無論如何都是return 0
            if foot_turtle(end,mou):
                ap=is_apple(apple,end,start)
                setmap(map,end,"me",2)
                if epa&16 or ap!=8: #為什麼是8見is_apple()
                    setmap(map,end,"e",1)
                    seteta(eta,epa&7,1<<ap) #eta[a]加入第ap個銅錢草
                    if epa&8 or not getflags(flags,"mouseUp") and getmap(map,mou,"up"):
                        setmap(map,end,"p",1)
                        return 6
                    return 4
        elif not getmap(map,end,"have chess") or not getmap(map,end,"up") and (getflags(flags,"mouseUp") or getmap(map,mou,"up")):
            ap=is_apple(apple,end,start)
            setmap(map,end,"me",1)
            if epa&16 or ap!=8:
                setmap(map,end,"e",1)
                seteta(eta,epa&7,1<<ap) #eta[a]加入第ap個銅錢草
                if epa&8 or not getflags(flags,"mouseUp") and getmap(map,mou,"up"):
                    setmap(map,end,"p",1)
                    return 6|(not getmap(map,end,"down"))
                return 4|(not getmap(map,end,"down"))
            return not getmap(map,end,"down")
    return 0 #所有沒return,要中斷迴圈都來這

def is_apple(apple,end,start):
    d={27:0,29:1,33:2,35:3,38:5,42:6,44:7}.get(min(start,end),8) #8表不同排,後面ap!=8即此意
    return d if start%9!=end%9 && getapple(apple,d) else 8

def second_click():pass

def born():pass
