#11/7 0.1
'''未完成'''
'''definition of structs and functions
struct sMap{b:2,me:2,p:1,e:1,up:5,down:5}m[86]
struct control{t:1,kmdlborn:1,zu:7,zd:7,mouse:8,tag:8}c #kmdlborn用不到了,sad
/*註解略寫  #請使用ctrl+f自行搜尋
[t差] t=目的地差值
[end_up] whereUp=where(兩高用.up,一高用.down)
[start_up] selfUp=self(兩高用.up,一高用.down)
[w鱷龜] if(w無鱷龜)=1 elif同直行=1 else 0
'''
m=0
c=0
l=0
eta=[0]*8
#*(m+81) dll return{0x2000 ismchange,l:8,&16 t(c>>31),&8 t(when bo),&4 bo,&2 co,&1 keep game}
#*(m+82){c:高16}
#*(m+83){c:低16}
#*(m+84~87){eta:0~7}
def reset():
    global eta,m,c
    eta=[0]*8 #eta清空
    for i in range(81):m[i]&=0xc3ff #m[0~81].c清空
    c|=0x3fff0000 #c重置

def move_limit(end,start): #無規律只能窮舉
    return {-10:start%9 and start>8,
     -9:start>8, #非最上橫排
     -8:start%9!=8 and start>8,
     -1:start%9, #非最左橫排
     1:start%9!=8, #非最右橫排
     8:start%9 and start<72,
     9:start<72, #非最下橫排
     10:start%9!=8 and start<72
    }[end-start]
    #剩的自己排列組合

def foot_turtle(end,start):
    global m
    end_up=m[end]>>(not not m[end]&0x3e0)*5&0x1f
    start_up=m[start]>>(not not m[start]&0x3e0)*5&0x1f
    if start_up<4:return 1 #if(start_up==1 or start_up==2 or start_up==3)return 1
    if end_up!=13:return end_up!=15 or not (end-start)%9 #if(w沒大腳怪)[w鱷龜]
    #w大腳怪
    if start_up!=13:return 0
    return end_up!=15 or not (end-start)%9 #if(s沒大腳怪)[w鱷龜]

def poison_frog(end,start):
    global m
    end_up=m[end]>>(not not m[end]&0x3e0)*5&0x1f #[end_up]
    if end_up!=18:return 0 #w沒箭毒蛙
    #w箭毒蛙
    start_up=m[start]>>(not not m[start]&0x3e0)*5&0x1f #[start_up]
    if start_up!=15:return start_up!=13 #if(s無鱷龜)return if(s大腳怪)=1 else  0
    return not (end-start)%9 #s鱷龜 if(同直行)=1 else=0

def is_apple(end,start):
    global l
    if start%9!=end%9:return 8
    else:
        d={27:0,29:1,33:2,35:3,38:5,42:6,44:7}.get(min(start,end),8) #8表不同排,後面ap!=8即此意
        return d if 1<<d&l else 8

def move(end,start,epa): #e=evolution p=ispoison a=whichEta #return &1keep &2p &4e
    global m,c,eta
    mou=c>>8&0x7f
    if move_limit(end,start):
        if m[end]>>14 == 2-(c>>31): #敵人 #吃人無論如何都是return 0
            if foot_turtle(end,mou):
                ap=is_apple(end,start)
                m[end]|=0x2000 #m[end].me=2
                if epa&16 or ap!=8: #見ia()
                    m[end]|=0x400 #m[end].e=1
                    eta[epa&7]|=1<<ap #eta[a]加入第ap個銅錢草
                    if epa&8 or ~c&0x8000 and m[mou]&0x3e0: #if(p or (!mouseUp and m[mou].up))m[end].p=1
                        m[end]|=0x800
                        return 6
                    return 4
        elif not m[end] or not m[end]&0x3e0 and (c&0x8000 or not m[mou]&0x3e0): #m[end]空 or (m[end].up空 and (mouseUp or m[mou].up空))
            ap=is_apple(end,start)
            m[end]|=0x1000 #m[end].me=1
            if epa&16 or ap!=8:
                m[end]|=0x400
                eta[epa&7]|=1<<ap
                if epa&8 or ~c&0x8000 and m[mou]&0x3e0:
                    m[end]|=0x800
                    return 6|(not m[end]&0x1f)
                return 4|(not m[end]&0x1f)
            return not m[end]&0x1f
    return 0 #所有沒return,要中斷迴圈都來這

def which_eta(down,t): #down=移動者,t=移動量
    if down!=7:
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
    if c>>31:return 5 if t%9!=1 else 7
    return 2 if t%9!=1 else 0

def switch_dict(down):
    global m,eta,c
    t=c>>31 #t=turn
    s=c>>8&0x7f #s=mouse
    if down==16:
        for i in range(s-9,-1,-9):
            if m[i]>>14==2-t: #敵人
                if foot_turtle(i,s):c=c&0xc07fffff|i<<23
                break
        for i in range(s+9,81,9):
            if m[i]>>14==2-t: #敵人
                if foot_turtle(i,s):c=c&0xff80ffff|i<<16
                break
    if down==1 or down==2 or down==13 or down==14 or down==15 or down==16:
        if down!=2:
            move(s-1,s,3)
            move(s+1,s,4)
        move(s-10,s,0)
        move(s-9,s,1)
        move(s-8,s,2)
        move(s+8,s,5)
        move(s+9,s,6)
        move(s+10,s,7)
    elif down==3:
        move(s-10,s,0)
        move(s-8,s,2)
        move(s-1,s,3)
        move(s+1,s,4)
        move(s+8,s,5)
        move(s+10,s,7)
    elif down==4 or down==10:move(s+9,s,6) if t else move(s-9,s,1)
    elif down==5:
        move(s-9,s,1)
        move(s-1,s,3)
        move(s+1,s,4)
        move(s+9,s,6)
    elif down==6:
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
    elif down==7:
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
    elif down==8:
        move(s-9,s,1)
        move(s+9,s,6)
        for k in [0,1]:
            i=s
            j=1
            while j&1:
                j=move(i+1 if k else i-1,i,3+k|j<<2&0x18)
                i+=1 if k else -1
    elif down==9 or down==18:
        p=m[s]&0x3e0 and ~c&0x8000 #will p
        i=s-9
        j=1
        while i>=0:
            ap=is_apple(i+9,i)
            if ap!=8:
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
            ap=is_apple(i-9,i)
            if ap!=8:
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
            ap=is_apple(i+1,i)
            if ap!=8:
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
            ap=is_apple(i-1,i)
            if ap!=8:
                j=7 if p else 5
                eta[4]|=1<<ap
            if m[i]:
                i+=1
                break
            i+=1
        while i%9:
            j=move(i,i-1,4|j<<2&0x18)
            i+=1
    elif down==17:
        for i in range(81):
            if m[i]>>14==t+1 and s!=i:m[i]|=0x1000
    elif down==19:
        for k1,k2 in [[-9,1],[-1,3],[1,4],[9,6]]:
            i=s
            j=1
            while j&1:
                j=move(i+k1,i,k2|j<<2&0x18)
                i+=k1

def first_set():
    global c,m
    if not m[c>>8&0x7f]&0x3e0:c&=0xffff7fff #if(m[mouse].up空)mouseUp=0
    reset()
    switch_dict(m[c>>8&0x7f]>>(not not c&0x8000)*5&0x1f) #原理同[end_up],[start_up]
    c=c^(c&0xff)|(c>>8&0xff) #tag(Up)=mouse(Up)

def whale(start):
    global m
    p=0 #八格遍歷,只能窮舉
    for i in range(8):
        th=start+[-10,-9,-8,-1,1,8,9,10][i]
        tu=m[th]>>(not not m[th]&0x3e0)*5&0x1f
        if move_limit(start,th) and m[th]>>14==2-(c>>31) and tu!=13 and (tu!=15 or i==1 or i==6):
            if tu==18:p=1 #自己頭上必鯨魚
            m[th]=0
    return p

def to_penguin():
    global m
    for i in range(72,81):
        if m[i]&0x8000: #b==2
            up=m[i]>>5&0x1f
            down=m[i]&0x1f
            if up and (up==6 or up==7 or up==4 or up==10):m[i]=m[i]&0xfc1f|0x260 #頭up只是拿來加速短路
            if down==6 or down==7 or down==4 or down==10:m[i]=m[i]&0xffe0|0x13
    for i in range(9):
        if m[i]&0x4000: #b==1
            up=m[i]>>5&0x1f
            down=m[i]&0x1f
            if up and (up==6 or up==7 or up==4 or up==10):m[i]=m[i]&0xfc1f|0x260 #頭up只是拿來加速短路
            if down==6 or down==7 or down==4 or down==10:m[i]=m[i]&0xffe0|0x13

def how_many_kmdl(turn):
    global m
    for i in range(81):
        if (m[i]>>14)-1==turn and (m[i]&0x1f==1 or m[i]&0x3e0==32):return 1
    return 0

def apple_del(e,s): #e=end,s=start
    if e>s:e,s=s,e #w恆小
    return (e<=27 and s>=36)|(e<=29 and s>=38)<<1|(e<=33 and s>=42)<<2|(e<=35 and s>=44)<<3|(e<=38 and s>=47)<<5|(e<=42 and s>=51)<<6|(e<=44 and s>=53)<<7

def second_set():
    global m,c,eta,l
    end=c>>8&0x7f
    start=c&0x7f
    tu=m[start]>>(not not m[start]&0x3e0)*5&0x1f
    td=m[start]>>(not not c&0x80)*5&0x1f
    t=c>>31
    if tu==14 or tu==5 and m[end]&0x400:m[end]|=0x800 if whale(end) else 0 #if(tu鯨魚 or (tu鯰魚 and m[end].e)whale
    if td==17: #鬣蜥
        m[start],m[end]=m[end],m[start] #換
        if m[start]>>(not not m[start]&0x3e0)*5&0x1f==14: #whale
            if whale(start):m[start]=0
        to_penguin() #to pen
    else:
        if m[end]&0x400:l^=eta[which_eta(td,end-start)]&apple_del(end,start) #appleDel
        if m[end]&0x2000: #吃
            if poison_frog(end,start):m[end]&=0x3c00 #wb=end_up=wd=0
            else:
                m[end]=(m[end]&0x3c00)|td|(t+1<<14) #wb=t+1,wd=td,end_up=0
                if m[start]&0x3e0 and ~c&0x80:m[end]|=tu<<5 #if(tu and !tagUp)end_up=tu
        elif m[end]>>14:m[end]|=tu<<5 #if(wb)end_up=tu
        else:
            m[end]|=td|(t+1<<14) #wd=td,wb=tb
            if m[start]&0x3e0 and ~c&0x80:m[end]|=tu<<5 #if(start_up and !tagUp)end_up=tu
        if m[end]&0x400 and tu!=1 and tu!=2 and tu!=3 and tu<11:m[end]+=9<<(not not m[end]&0x3e0)*5 #if((m[end].e)&&(tu!=1)&&(tu!=2)&&(tu!=3)&&未進化)m[end].down=tu+9 #進化
        m[start]&=0xfc1f #start_up=0
        if ~c&0x80:m[start]&=0x3fe0 #if(!tagUp)sd=sb=0
        if m[end]&0x800:m[end]&=0x3c00 #if(m[end].p)end_up=wd=wb=0
        to_penguin()
        if tu==1 and m[end]&0x2400: #if(tu=1 and (m[end].me=2 or m[end].e))
            if t: #if(後手)
                if (not m[4]&0x4000) and (not m[4]&0x3e0):m[81]|=4|c>>31<<3 #if(*(m+4).b!=1 and *(m+4).up空)born()
            elif (not m[76]&0x8000) and (not m[76]&0x3e0):m[81]|=4|c>>31<<3 #elif(*(m+76).b!=2 and *(m+76).up空)born()

def shot_poison():
    global m,c
    end=c>>8&0x7f
    start=c&0x7f
    if m[start]>>5&0x1f==14:
        if whale(end):m[start]=0
    c|=(m[start]>>5&0x1f==1)<<30
    if poison_frog(end,start):m[start]&=0x3c00
    if foot_turtle(end,start):m[end]&=0x3c00
    if c&0x40000000:
        if c&0x80000000:
            if (not m[4]&0x4000) and (not m[4]&0x3e0):m[81]|=4|c>>31<<3 #if(後手)if(*(m+4).b!=1 and *(m+4).up空)born()
        elif (not m[76]&0x8000) and (not m[76]&0x3e0):m[81]|=4|c>>31<<3 #if(後手)if(*(m+4).b!=1 and *(m+4).up空)born()
    c&=0xbfffffff

def pyvkcoreclick(p,nm):
    global m,c,eta,l
    m=p
    c=m[82]<<16|m[83]
    l=m[81]>>5&0xff
    for i in range(4):
        eta[i<<1]=m[84+i]>>8&0xff
        eta[(i<<1)+1]=m[84+i]&0xff
    if m[81]&4:
        home=4 if m[81]&8 else 76
        m[home]|=nm<<(not not m[home])*5|(0x8000 if m[81]&8 else 0x4000)
        m[81]&=0x1ff3
        if not how_many_kmdl(m[81]>>3&1):m[81]&=0x1ffe
        m[81]|=0x2000
    else:
        c=c&0xffff00ff|nm<<8 #mou=nm&0xff
        if c&0x7f==127 and m[c>>8&0x7f]>>14==(c>>31)+1:#if((tag==127(|255))&&m[mou]==t)
            first_set() #first_set()
            m[81]|=2 #co()
        else:
            m[81]=m[81]&16|1
            if (c>>8&0x7f!=127 and ((c>>8&0x7f==c>>23&0x7f) or (c>>8&0x7f==c>>16&0x7f))) and (c&0x8000^c>>16&0x8000 or not m[c>>8&0x7f]&0x3c00): #if((mou!=127 and ((mou==zu) or (mou==zd)))  and  (mouUp or !m[mou].mepe))
                shot_poison()
                reset()
                c^=0x80000000
                m[81]^=16
                if not (how_many_kmdl(c>>31) and how_many_kmdl(not c>>31)):m[81]=(m[81]&30)|(m[81]>>2 and not how_many_kmdl(not c>>31))
                c=c&0xffffff00|0x7f
                m[81]|=0x2000
            elif m[c>>8&0x7f]&0x3c00: #if(c[])second_set()
                second_set()
                reset()
                c^=0x80000000
                m[81]^=16
                if not (how_many_kmdl(c>>31) and how_many_kmdl(not c>>31)):m[81]=(m[81]&30)|(m[81]>>2 and not how_many_kmdl(not c>>31))
                c=c&0xffff0000|0x7f7f
                m[81]|=0x2000
            else:
                reset()
                c=c&0xffff0000|0x7f7f
            m[81]=m[81]&0x201f|l<<5
    m[82]=c>>16&0xffff
    m[83]=c&0xffff
    for i in range(4):m[84+i]=eta[i<<1]<<8|eta[(i<<1)+1]
    # return m
def pyvkcoreundo(p):
    global m
    m=p
    reset()
    m[81]&=0x1ffd
    m[83]=m[83]&0xff00|0x7f7f
'''
struct control{t:1,kmdlborn:1,zu:7,zd:7,mouse:8,tag:8}c #kmdlborn用不到了,sad
'''
#*(m+81) dll return{0x2000 ismchange,l:8,&16 t(c>>31),&8 t(when bo),&4 bo,&2 co,&1 keep game}
#*(m+82){c:高16}
#*(m+83){c:低16}
