#12/18 0.1
'''未完成
先手青蛙南七北六 後手青蛙北七南二 先手青蛙西四進化會吃到第一個銅錢草 原理不明 以後再改
select_chess一堆迴圈可縮短
增加糧食危機
增加鳳梨
讓move j(epa) 從世上消失
'''
'''definition of structs and functions
struct sMap{b:2,me:2,p:1,e:1,up:5,down:5}m[86]
struct control{t:1,born:1,zu:7,zd:7,mouse:8,tag:8}c
'''
getm=lambda pos,type:m[pos]>>{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10,"have chess":0}[type]&{"b":3,"me":3,"p":1,"e":1,"up":0x1f,"down":0x1f,"c":0xf,"have chess":0x3ff}[type]
# getm=lambda pos,type:m>>(pos<<4)>>{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10,"have chess":0}[type]&{"b":3,"me":3,"p":1,"e":1,"up":0x1f,"down":0x1f,"c":0xf,"have chess":0x3ff}[type]
def setm(pos,type,value):
    global m
    m[pos]=m[pos]&{"b":0x3fff,"me":0xcfff,"p":0xf7ff,"e":0xfbff,"up":0xfc1f,"down":0xffe0,"c":0xc3ff}[type]|value<<{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10}[type]
    # m=m&{"b":0x3fff,"me":0xcfff,"p":0xf7ff,"e":0xfbff,"up":0xfc1f,"down":0xffe0,"c":0xc3ff}[type]<<(pos<<4)|value<<{"b":14,"me":12,"p":11,"e":10,"up":5,"down":0,"c":10}[type]<<(pos<<4)
getc=lambda type:c>>{"t":31,"born":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0,"mouse,up":8,"tag,up":0}[type]&{"t":1,"born":1,"zu":0x7f,"zd":0x7f,"mouseup":1,"mouse":0x7f,"tagup":1,"tag":0x7f,"mouse,up":0xff,"tag,up":0xff}[type]
# getc=lambda type:c>>{"t":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0}[type]&{"t":1,"zu":0x7f,"zd":0x7f,"mouseup":1,"mouse":0x7f,"tagup":1,"tag":0x7f}[type]
def setc(type,value):
    global c
    c=c&{"t":0x7fffffff,"born":0xbfffffff,"zu":0xc07fffff,"zd":0xff80ffff,"mouseup":0xffff7fff,"mouse":0xffff80ff,"tagup":0xffffff7f,"tag":0xffffff80,"mouse,up":0xffff00ff,"tag,up":0xffffff00}[type]|value<<{"t":31,"born":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0,"mouse,up":8,"tag,up":0}[type]
    # c=c&{"t":0x3fffffff,"zu":0x407fffff,"zd":0x7f80ffff,"mouseup":0x7fff7fff,"mouse":0x7fff80ff,"tagup":0x7fffff7f,"tag":0x7fffff80,"mouse,up":0x7fff00ff,"tag,up":0x7fffff00}[type]|value<<{"t":30,"zu":23,"zd":16,"mouseup":15,"mouse":8,"tagup":7,"tag":0,"mouse,up":8,"tag,up":0}[type]
getc2=lambda type:c2>>{"m change":2,"c output":1,"keep game":0}[type]&1
def setc2(type,value):
    global c2
    c2=c2&{"m change":0x3,"c output":0x5,"keep game":0x6}[type]|value<<{"m change":2,"c output":1,"keep game":0}[type]
# return{0x2000 ismchange,l:8,&16 t(c>>31),&8 t(when bo),&4 bo,&2 co,&1 keep game}
geteta=lambda pos:eta[pos]&0xff
# geteta=lambda pos:eta>>(pos<<3)&0xff
def seteta(pos,value):
    global eta
    eta[pos]=eta[pos]^geteta(pos)|value
getapple=lambda pos:apple>>pos&1
# getapple=lambda pos:apple>>2*pos&3
def setapple(pos,value):
    global apple
    apple^=getapple(pos)^value<<pos
    # apple=(apple^getapple(pos)<<2*pos)|value<<2*pos
m=0
c=0
c2=0
eta=[0]*8
apple=0
ffox=0
#*(m+81) dll return{0x20 ismchange,0x10 t(c>>31),&8 t(when bo),&4 bo,&2 co,&1 keep game}
#*(m+82){c:高16}
#*(m+83){c:低16}
#*(m+84~91){eta:0~7}
def reset():
    for i in range(8):seteta(i,0)
    for i in range(81):setm(i,"c",0)
    for type,value in (("zu",0x7f),("zd",0x7f)):setc(type,value)

def move_limit(end,start):
    pos,dcol,scol=end-start,(end-start)%9,start%9 #dcol=差值(delta)column,scol=start column
    return (not dcol==8 or scol) and (not dcol==1 or scol!=8) and (pos>=-1 or start>8) and (pos<=1 or start<72)

def foot_turtle(end,start):
    end_up=getm(end,"up" if getm(end,"up") else "down")
    start_up=getm(start,"up" if getm(start,"up") else "down")
    if start_up<4:return 1 #if(start_up==1 or start_up==2 or start_up==3)return 1
    if end_up!=13:return end_up!=15 or not (end-start)%9 #if(w沒大腳怪)[w鱷龜]
    #w大腳怪
    if start_up!=13:return 0
    return end_up!=15 or not (end-start)%9 #if(s沒大腳怪)[w鱷龜]

def poison_frog(end,start):
    end_up=getm(end,"up" if getm(end,"up") else "down")
    if end_up!=18:return 0 #w沒箭毒蛙
    #w箭毒蛙
    start_up=getm(start,"up" if getm(start,"up") else "down")
    if start_up!=15:return start_up!=13 #if(s無鱷龜)return if(s大腳怪)=1 else  0
    return not (end-start)%9 #s鱷龜 if(同直行)=1 else=0

ap_pos=lambda x:x//9*34+(x%9<<1)

def move(end,start,epa): #e=evolution p=ispoison a=whichEta #return &1keep &2p &4e
    global m,c,eta
    mou=getc("mouse")
    if move_limit(end,start):
        if getm(end,"b")==2-getc("t"): #敵人 #吃人無論如何都是return 0
            if foot_turtle(end,mou):
                ap=ap_pos(end)+ap_pos(start)>>1
                setm(end,"me",2)
                if epa&16 or apple>>ap&1:
                    setm(end,"e",1)
                    seteta(epa&7,1<<ap) #eta[a]加入第ap個銅錢草
                    if epa&8 or not getc("mouseup") and getm(mou,"up"):
                        setm(end,"p",1)
                        return 6
                    return 4
        elif not getm(end,"have chess") or not getm(end,"up") and (getc("mouseup") or not getm(mou,"up")):
            ap=ap_pos(end)+ap_pos(start)>>1
            setm(end,"me",1)
            if epa&16 or apple>>ap&1:
                setm(end,"e",1)
                seteta(epa&7,1<<ap) #eta[a]加入第ap個銅錢草
                if epa&8 or not getc("mouseup") and getm(mou,"up"):
                    setm(end,"p",1)
                    return 6|(not getm(end,"down"))
                return 4|(not getm(end,"down"))
            return not getm(end,"down")
    return 0 #所有沒return,要中斷迴圈都來這

def which_eta(who,t): #who=移動者,t=移動量
    if who!=7:
        if t<0:
            if t%10:return 1
            elif t%9:return 2
            elif t%8:return 3
            else:return 0
        else:
            if t%10:return 6
            elif t%9:return 5
            elif t%8:return 4
            else:return 7
    if getc("t"):return 5 if t%9!=1 else 7
    return 2 if t%9!=1 else 0

def select_chess(who):
    global m,eta,c
    t=getc("t")
    s=getc("mouse")
    if who==16:
        for stop,x,flags_type in ((-1,-9,"zu"),(81,9,"zd")):
            for i in range(s+x,stop,x):
                if getm(i,"b")==2-t: #敵人
                    if foot_turtle(i,s):setc(flags_type,i)
                    break
    l=((-10,0),(-9,1),(-8,2),(-1,3),(1,4),(8,5),(9,6),(10,7))
    r=(((0,8),),((0,3),(5,8)),((0,1),(2,6),(7,8)),((6,7) if t else (1,2),),((0,1),(2,3),(5,6),(7,8)))
    if who==6:
        if t:
            for k in range(8,11):
                i=s
                j=1
                while j&1:
                    j=move(i+k,i,k-3|j<<2&0x18) #所有loop mo都是先&在|
                    i+=k
        else:
            for k in range(8,11):
                i=s
                j=1
                while j&1:
                    j=move(i-k,i,10-k|j<<2&0x18) #所有loop mo都是先&在|
                    i-=k
    elif who==7:
        if t:
            for k in [0,2]:
                i=s+8+k
                j=move(s+8+k,s,5+k)
                while j&1:
                    j=move(i+9,i,5+k|j<<2&0x18) #所有loop mo都是先&在|
                    i+=9
        else:
            for k in [0,2]:
                i=s-10+k
                j=move(s-10+k,s,2-k)
                while j&1:
                    j=move(i-9,i,2-k|j<<2&0x18) #所有loop mo都是先&在|
                    i-=9
    elif who==8:
        move(s-9,s,1)
        move(s+9,s,6)
        for k in [0,1]:
            i=s
            j=1
            while j&1:
                j=move(i+1 if k else i-1,i,3+k|j<<2&0x18)
                i+=1 if k else -1
    elif who==9 or who==18:
        p=m[s]&0x3e0 and ~c&0x8000 #will p
        i=s-9
        j=1
        while i>=0:
            ap=ap_pos(i+9)+ap_pos(i)>>1
            if apple>>ap&1:
                j=7 if p else 5
                eta[1]|=1<<ap
            if m[i]:
                i-=9
                break
            i-=9
        while i>=0:
            j=move(i,i+9,1|j<<2&0x18)
            i-=9
        i=s+9
        j=1
        while i<81:
            ap=ap_pos(i-9)+ap_pos(i)>>1
            if apple>>ap&1:
                j=7 if p else 5
                eta[6]|=1<<ap
            if m[i]:
                i+=9
                break
            i+=9
        while i<81:
            j=move(i,i-9,6|j<<2&0x18)
            i+=9
        i=s-1
        j=1
        while (i+1)%9:
            ap=ap_pos(i+1)+ap_pos(i)>>1
            if apple>>ap&1:
                j=7 if p else 5
                eta[3]|=1<<ap
            if m[i]:
                i-=1
                break
            i-=1
        while (i+1)%9:
            j=move(i,i+1,3|j<<2&0x18)
            i-=1
        i=s+1
        j=1
        while i%9:
            ap=ap_pos(i-1)+ap_pos(i)>>1
            if apple>>ap&1:
                j=7 if p else 5
                eta[4]|=1<<ap
            if m[i]:
                i+=1
                break
            i+=1
        while i%9:
            j=move(i,i-1,4|j<<2&0x18)
            i+=1
    elif who==17:
        for i in range(81):
            if m[i]>>14==t+1 and s!=i:m[i]|=0x1000
    elif who==19:
        for k1,k2 in [[-9,1],[-1,3],[1,4],[9,6]]:
            i=s
            j=1
            while j&1:
                j=move(i+k1,i,k2|j<<2&0x18)
                i+=k1
    else:
        if who==10:who=4
        elif who==11:who=5
        elif 12<who<17:who=1
        for ir in r[who-1]:
            for x,epa in l[ir[0]:ir[1]]:move(s+x,s,epa)

def first_click():
    if not getm(getc("mouse"),"up"):setc("mouseup",0)
    reset()
    select_chess(getm(getc("mouse"),"up" if getc("mouseup") else "down"))

def whale(start):
    p=0 #八格遍歷,只能窮舉
    for i in range(8):
        th=start+(-10,-9,-8,-1,1,8,9,10)[i]
        tu=getm(th,"up" if getm(th,"up") else "down")
        if move_limit(start,th) and getm(th,"b")==2-getc("t") and tu!=13 and (tu!=15 or i==1 or i==6):
            if tu==18:p=1 #自己頭上必鯨魚
            setm(th,"up",0)
            setm(th,"down",0)
    return p

def to_penguin():
    for i in range(72,81):
        if getm(i,"b")==2:
            up=getm(i,"up")
            down=getm(i,"down")
            if up and (up==6 or up==7 or up==4 or up==10):setm(i,"up",19) #頭up只是拿來加速短路
            if down==6 or down==7 or down==4 or down==10:setm(i,"down",19)
    for i in range(9):
        if getm(i,"b")==1:
            up=getm(i,"up")
            down=getm(i,"down")
            if up and (up==6 or up==7 or up==4 or up==10):setm(i,"up",19) #頭up只是拿來加速短路
            if down==6 or down==7 or down==4 or down==10:setm(i,"down",19)

def how_many_kmdl(turn):
    turn+=1
    for i in range(81):
        if getm(i,"b")==turn and (getm(i,"up")==1 or getm(i,"down")==1):return 1
    return 0

def second_click():
    global eta,apple
    end=getc("mouse")
    start=getc("tag")
    tu=getm(start,"up" if getm(start,"up") else "down")
    td=getm(start,"up" if getc("tagup") else "down")
    t=getc("t")
    if tu==14 or tu==5 and getm(end,"e"):setm(end,"p",whale(end))
    if td==17: #鬣蜥
        temp=(getm(end,"up"),getm(end,"down"))
        setm(end,"up",getm(start,"up"))
        setm(end,"down",getm(start,"down"))
        setm(start,"up",temp[0])
        setm(start,"down",temp[1])
        if getm(start,"up" if getm(start,"up") else "down")==14: #whale
            if whale(start):
                setm(start,"up",0)
                setm(start,"down",0)
        to_penguin() #to pen
    else:
        if getm(end,"e"):apple^=eta[which_eta(td,end-start)]&apple&((1<<1+ap_pos(max(start,end)))-1^(1<<1+ap_pos(min(start,end)))-1) #apple_del
        if getm(end,"me")==2: #吃
            if poison_frog(end,start):
                setm(end,"b",0)
                setm(end,"up",0)
                setm(end,"down",0)
            else:
                setm(end,"b",t+1)
                setm(end,"down",td)
                if getm(start,"up") and not getc("tagup"):setm(end,"up",tu)
        elif getm(end,"b"):setm(end,"up",tu)
        else:
            setm(end,"b",t+1)
            setm(end,"down",td)
            if getm(start,"up") and not getc("tagup"):setm(end,"up",tu)
        if getm(end,"e") and 1<tu<11:setm(end,"up" if getm(end,"up") else "down",tu+9)
        setm(start,"up",0)
        if not getc("tagup"):
            setm(start,"b",0)
            setm(start,"down",0)
        if getm(end,"p"):
            setm(end,"b",0)
            setm(end,"up",0)
            setm(end,"down",0)
        to_penguin()
        if tu==1 and (getm(end,"me")==2 or getm(end,"e")):
            if t: #if(後手)
                if getm(4,"b")!=1 and not getm(4,"up"):setc("born",1)
            elif getm(76,"b")!=2 and not getm(76,"up"):setc("born",1)

def shot_poison():
    end=getc("mouse")
    start=getc("tag")
    if getm(start,"up")==14:
        if whale(end):
            setm(start,"b",0)
            setm(start,"up",0)
            setm(start,"down",0)
    kmdlborn=1
    if poison_frog(end,start):
            setm(start,"b",0)
            setm(start,"up",0)
            setm(start,"down",0)
    if foot_turtle(end,start):
            setm(end,"b",0)
            setm(end,"up",0)
            setm(end,"down",0)
    #born待改
    if kmdlborn:
        if getc("t"):
            if not getm(4,"b")==1 and not getm(4,"up"):setc("born",1)
        elif not getm(76,"b")==2 and not getm(76,"up"):setc("born",1)

def ffox_calculate():
    global ffox
    for i in range(81):ffox|=((getm(i,"up")==11 and getm(i,"b")==2-getc("t"))<<1|(getm(i,"down")==11 and getm(i,"b")==2-getc("t")))<<(i<<1)

'''
call_type
-1 undo
0 click(nm)
1 born()
'''
def pyvkcorecall(pm,pc,papple,pffox,peta,call_type,*args):
    global m,c,eta,apple,ffox
    m=pm
    c=pc
    apple=papple
    ffox=pffox
    eta=peta
    {-1:undo,0:click,1:born,2:ffox_click}[call_type](*args)
    return m,c,apple,ffox,eta

def ffox_click(nm):
    global ffox,m,c
    c=c&0xffff00ff|nm<<8 #mou=nm&0xff
    if ffox&1<<(((c>>8&0x7f)<<1)+(c>>15&1)) and c&0x7f==127 and m[c>>8&0x7f]>>14==(c>>31)+1:#if(ffox[mou]&&(tag==127(|255))&&m[mou]==t)first_click()
        if not m[c>>8&0x7f]&0x3e0:c&=0xffff7fff #if(m[mouse].up空)mouseUp=0
        reset()
        if m[c>>8&0x7f]>>(not not c&0x8000)*5&0x1f==11: #原理同[end_up],[start_up]
            s=c>>8&0x7f #s=mouse
            move(s-10,s,0)
            move(s-8,s,2)
            move(s+8,s,5)
            move(s+10,s,7)
            c=c^(c&0xff)|(c>>8&0xff) #tag(Up)=mouse(Up)
        setc2("c output",1)
    else:
        if m[c>>8&0x7f]&0x3c00: #if(c[])second_click()
            ffox^=(1<<(c>>7&1))<<((c&0x7f)<<1)
            save_ffox_up=not c&0x80 and m[c&0x7f]&0x3e0==352 and ffox>>(((c&0x7f)<<1)+1)&1
            second_click()
            if save_ffox_up and m[c>>8&0x7f]&0x3e0==352:ffox^=(2<<((c&0x7f)<<1))|(1<<((c>>8&0x7f)<<1)+1)
            reset()
            if not ffox:
                c^=0x80000000
            if not (how_many_kmdl(c>>31) and how_many_kmdl(not c>>31)):setc2("keep game",getc("born") and not how_many_kmdl(not getc("t")))
            c=c&0xffff0000|0x7f7f
            setc2("m change",1)
        else:
            reset()
            c=c&0xffff0000|0x7f7f

def born(nm):
    t=getc("t")
    home=4 if t else 76
    setm(home,"up" if getm(home,"have chess") else "down",nm)
    setm(home,"b",t+1)
    setc("born",0)
    if not how_many_kmdl(t):setc2("keep game",0)
    setc2("m change",1)
    setc("t",getc("t")^1)

def click(nm):
    setc("mouse,up",nm)
    if getc("tag")==127 and getm(getc("mouse"),"b")==getc("t")+1:
        first_click()
        setc("tag,up",getc("mouse,up"))
        setc2("c output",1)
    else:
        setc2("keep game",1)
        if getc("mouse")!=127 and (getc("mouse")==getc("zu") or getc("mouse")==getc("zd")) and (getc("mouseup") or not getm(getc("mouse"),"c")):
            shot_poison()
            reset()
            setc("t",getc("t")^1)
            if not (how_many_kmdl(getc("t")) and how_many_kmdl(not getc("t"))):setc2("keep game",getc("born") and not how_many_kmdl(not getc("t")))
            setc("tag",127)
            setc2("m change",1)
            ffox_calculate()
            if ffox:
                setc("t",getc("t")^1)
        elif getm(getc("mouse"),"c"):
            second_click()
            reset()
            if not getc("born"):setc("t",getc("t")^1)
            if not (how_many_kmdl(getc("t")) and how_many_kmdl(not getc("t"))):setc2("keep game",getc("born") and not how_many_kmdl(not getc("t")))
            setc("mouse",127)
            setc("tag",127)
            setc2("m change",1)
            ffox_calculate()
            if ffox:setc("t",getc("t")^1)
        else:
            reset()
            setc("mouse",127)
            setc("tag",127)

def undo(pm,papple):
    global m,ffox,apple
    m=pm
    ffox=0
    apple=papple
    reset()
    setc2("c output",0)
