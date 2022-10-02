#6/18 0.9.15 可以正常使用
#將軍判定有對方能生的可能 check先註解
#等連線
import pygame
from sys import exit
from os.path import dirname
# global m b c t tag tagUp mouse mouseUp keeploop eta1~8 zu zd froghas ischange lm lb lc
t = 1
mouse = -1
mouseUp = False
tag = -1
tagUp = False
m=[
7,0,5,0,4,0,3,0,1,0,2,0,4,0,5,0,6,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,9,0,0,0,0,0,0,0,0,0,0,0,8,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
-1,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,-1,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,-1,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,8,0,0,0,0,0,0,0,0,0,0,0,9,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
6,0,5,0,4,0,2,0,1,0,3,0,4,0,5,0,7]
c = [0] * 289
b = [0] * 289
for i in range(289):
    if m[i]:
        if i < 144:
            b[i] = 2
        else:
            b[i] = 1
ischange = False
lt=t
lm=[i for i in m]
lb=[i for i in b]
 
def each_reset():
    global c,zu,zd,eta1,eta2,eta3,eta4,eta5,eta6,eta7,eta8#,eta
    #eta=[[]]
    eta1=[]
    eta2=[]
    eta3=[]
    eta4=[]
    eta5=[]
    eta6=[]
    eta7=[]
    eta8=[]
    c = [0] * 289
    zu = zd = -1
 
def second_reset():
    global mouse,mouseUp,tag,tagUp
    mouse = -1
    mouseUp = False
    tag = -1
    tagUp = False
 
def move_limit(i):
    if i<=-32:
        if mouse<34:
            return False
    elif i>=32:
        if mouse>254:
            return False
    if i==-36 or i==-2 or i==32:
        if mouse%17==0:
            return False
    elif i==-32 or i==2 or i==36:
        if mouse%17==16:
            return False
    return True
 
def move(valT,valMMU,valMMO,whicheta,loop = False,valOMove = 0,isfrog = False,froghas = False,pl=False):
    global keeploop,eta1,eta2,eta3,eta4,eta5,eta6,eta7,eta8,returnFroghas
    returnFroghas = froghas
    if loop:
        if m[mouse+valT] != 0 and b[mouse+valT] != t:
            if valset(mouse+valT,False)[1] != 15 or whicheta is eta2 or whicheta is eta7 or pl or valMMU == 1 or valMMU == 2 or valMMU == 3:
                if valset(mouse+valT,False)[1] != 13 or valMMU == 1 or valMMU == 2 or valMMU == 3 or valMMU == 13 or (valMMU == 4 and m[int(mouse+valT-valOMove/2)] == -1):
                    if whicheta != []:
                        etahas = True
                    else:
                        etahas = False
                    if m[mouse+valT-valOMove//2] == -1 or etahas:
                        if m[mouse+valT-valOMove//2] == -1:
                            whicheta.append(int(mouse+valT-valOMove/2))
                        if valMMO:
                            if (isfrog and froghas) or not isfrog:
                                c[mouse+valT] = 5
                        else:
                            if (isfrog and froghas) or not isfrog:
                                c[mouse+valT] = 6
                    else:
                        if (isfrog and froghas) or not isfrog:
                            c[mouse+valT] = 4
                    if isfrog:
                        returnFroghas = True
                    else:
                        keeploop = False
                elif not isfrog:
                    keeploop = False
            elif not isfrog:
                keeploop = False
        else:
            if (valMMO and m[mouse+valT]<20) or m[mouse+valT] == 0:
                if whicheta != []:
                    etahas = True
                else:
                    etahas = False
                if m[mouse+valT-valOMove//2] == -1 or etahas:
                    whicheta.append(int(mouse+valT-valOMove/2))
                    if valMMO:
                        if (isfrog and froghas) or not isfrog:
                            c[mouse+valT] = 2
                    else:
                        if (isfrog and froghas) or not isfrog:
                            c[mouse+valT] = 3
                else:
                    if (isfrog and froghas) or not isfrog:
                        c[mouse+valT] = 1
                if m[mouse+valT] != 0:
                    if isfrog:
                        returnFroghas = True
                    else:
                        keeploop = False
            else:
                if isfrog:
                    returnFroghas = True
                else:
                    keeploop = False
    else:
        if move_limit(valT):
            limit = True
        else:
            limit = False
        if limit:
            if m[mouse+valT] != 0 and b[mouse+valT] != t:
                if valset(mouse+valT,False)[1] != 15 or whicheta is eta2 or whicheta is eta7 or valMMU == 1 or valMMU == 2 or valMMU == 3:
                    if valset(mouse+valT,False)[1] != 13 or valMMU == 1 or valMMU == 2 or valMMU == 3 or valMMU == 13 or (valMMU == 4 and m[int(mouse+valT/2)] == -1):
                        if m[mouse+valT//2] == -1:
                            if valMMO:
                                c[mouse+valT] = 5
                            else:
                                c[mouse+valT] = 6
                            whicheta.append(int(mouse+valT/2))
                        else:
                            c[mouse+valT] = 4
            else:
                if (valMMO and m[mouse+valT]<20) or m[mouse+valT] == 0:
                    if m[mouse+valT//2] == -1:
                        if valMMO:
                            c[mouse+valT] = 2
                        else:
                            c[mouse+valT] = 3
                        whicheta.append(int(mouse+valT/2))
                    else:
                        c[mouse+valT] = 1
 
def whichToEta(valMMD,valT):
    if valMMD == 7:
        if t&1:
            if valT % 34 == 32:
                return eta1
            return eta3
        if valT % 34 == 32:
            return eta8
        return eta6
    else:
        if valT < 0:
            if valT % 36 == 0:
                return eta1
            elif valT % 34 == 0:
                return eta2
            elif valT % 32 == 0:
                return eta3
            elif valT % 2 == 0:
                return eta4
        else:
            if valT % 32 == 0:
                return eta6
            elif valT % 34 == 0:
                return eta7
            elif valT % 36 == 0:
                return eta8
            elif valT % 2 == 0:
                return eta5
 
def switch_dict(valMMD,valMMU,valMMO,t,mouse):
    global zu,zd,froghas,keeploop,returnFroghas
    if valMMD == 1 or valMMD == 13 or valMMD == 14 or valMMD == 15 or valMMD == 16:
        move(-36,valMMU,valMMO,eta1)
        move(-34,valMMU,valMMO,eta2)
        move(-32,valMMU,valMMO,eta3)
        move(-2,valMMU,valMMO,eta4)
        move(2,valMMU,valMMO,eta5)
        move(32,valMMU,valMMO,eta6)
        move(34,valMMU,valMMO,eta7)
        move(36,valMMU,valMMO,eta8)
    elif valMMD == 2:
        move(-36,valMMU,valMMO,eta1)
        move(-34,valMMU,valMMO,eta2)
        move(-32,valMMU,valMMO,eta3)
        move(32,valMMU,valMMO,eta6)
        move(34,valMMU,valMMO,eta7)
        move(36,valMMU,valMMO,eta8)
    elif valMMD == 3:
        move(-36,valMMU,valMMO,eta1)
        move(-32,valMMU,valMMO,eta3)
        move(-2,valMMU,valMMO,eta4)
        move(2,valMMU,valMMO,eta5)
        move(32,valMMU,valMMO,eta6)
        move(36,valMMU,valMMO,eta8)
    elif valMMD == 4 or valMMD == 10:
        if t == 1:
            move(-34,valMMU,valMMO,eta2)
        else:
            move(34,valMMU,valMMO,eta7)
    elif valMMD == 5:
        move(-34,valMMU,valMMO,eta2)
        move(-2,valMMU,valMMO,eta4)
        move(2,valMMU,valMMO,eta5)
        move(34,valMMU,valMMO,eta7)
    elif valMMD == 6:
        if t == 1:
            keeploop = True
            i = -36
            while (mouse + i) % 17 != 1 and (mouse + i) >= 0 and keeploop:
                move(i,valMMU,valMMO,eta1,True,-36)
                i -= 36
            keeploop = True
            i = -34
            while (mouse + i) >= 0 and keeploop:
                move(i,valMMU,valMMO,eta2,True,-34)
                i -= 34
            keeploop = True
            i = -32
            while (mouse + i) % 17 != 15 and (mouse + i) >= 0 and keeploop:
                move(i,valMMU,valMMO,eta3,True,-32)
                i -= 32
        else:
            keeploop = True
            i = 36
            while (mouse + i) % 17 != 15 and (mouse + i) < 289 and keeploop:
                move(i,valMMU,valMMO,eta8,True,36)
                i += 36
            keeploop = True
            i = 34
            while (mouse + i) < 289 and keeploop:
                move(i,valMMU,valMMO,eta7,True,34)
                i += 34
            keeploop = True
            i = 32
            while (mouse + i) % 17 != 1 and (mouse + i) < 289 and keeploop:
                move(i,valMMU,valMMO,eta6,True,32)
                i += 32
    elif valMMD == 7:
        if t == 1:
            keeploop = True
            move(-36,valMMU,valMMO,eta1,True,-36)
            i = -70
            while (mouse + i) >= 0 and keeploop:
                move(i,valMMU,valMMO,eta1,True,-34,pl=True)
                i -= 34
            keeploop = True
            move(-32,valMMU,valMMO,eta3,True,-32)
            i = -66
            while (mouse + i) >= 0 and keeploop:
                move(i,valMMU,valMMO,eta3,True,-34,pl=True)
                i -= 34
        else:
            keeploop = True
            move(36,valMMU,valMMO,eta6,True,36)
            i = 70
            while (mouse + i) < 289 and keeploop:
                move(i,valMMU,valMMO,eta6,True,34,pl=True)
                i += 34
            keeploop = True
            move(32,valMMU,valMMO,eta8,True,32)
            i = 66
            while (mouse + i) < 289 and keeploop:
                move(i,valMMU,valMMO,eta8,True,34,pl=True)
                i += 34
    elif valMMD == 8:
        move(-34,valMMU,valMMO,eta2)
        move(34,valMMU,valMMO,eta7)
        keeploop = True
        i = -2
        while (mouse + i) % 17 != 15 and keeploop:
            move(i,valMMU,valMMO,eta4,True,-2)
            i -= 2
        keeploop = True
        i = 2
        while (mouse + i) % 17 != 1 and keeploop:
            move(i,valMMU,valMMO,eta5,True,2)
            i += 2
    elif valMMD == 9 or valMMD == 18:
        keeploop = True
        froghas = False
        returnFroghas = False
        i = -34
        while (mouse + i) >= 0 and keeploop:
            move(i,valMMU,valMMO,eta2,True,-34,True,froghas)
            froghas = returnFroghas
            i -= 34
        keeploop = True
        froghas = False
        returnFroghas = False
        i = -2
        while (mouse + i) % 17 != 15 and keeploop:
            move(i,valMMU,valMMO,eta4,True,-2,True,froghas)
            froghas = returnFroghas
            i -= 2
        keeploop = True
        froghas = False
        returnFroghas = False
        i = 2
        while (mouse + i) % 17 != 1 and keeploop:
            move(i,valMMU,valMMO,eta5,True,2,True,froghas)
            froghas = returnFroghas
            i += 2
        keeploop = True
        froghas = False
        returnFroghas = False
        i = 34
        while (mouse + i) < 289 and keeploop:
            move(i,valMMU,valMMO,eta7,True,34,True,froghas)
            froghas = returnFroghas
            i += 34
    elif valMMD == 17:
        for i in range(289):
            if b[i] == t and i != mouse:
                c[i] = 1
    elif valMMD == 19:
        keeploop = True
        i = -34
        while (mouse + i) >= 0 and keeploop:
            move(i,valMMU,valMMO,eta2,True,-34)
            i -= 34
        keeploop = True
        i = -2
        while (mouse + i) % 17 != 15 and keeploop:
            move(i,valMMU,valMMO,eta4,True,-2)
            i -= 2
        keeploop = True
        i = 2
        while (mouse + i) % 17 != 1 and keeploop:
            move(i,valMMU,valMMO,eta5,True,2)
            i += 2
        keeploop = True
        i = 34
        while (mouse + i) < 289 and keeploop:
            move(i,valMMU,valMMO,eta7,True,34)
            i += 34
    if valMMD == 16:
        i = -34
        keep = True
        while mouse+i >= 0 and keep:
            if b[mouse+i] != t and b[mouse+i] != 0:
                zu = mouse+i
                if c[mouse+i] == 0:
                    if valset(mouse+i,False)[1] != 13 or valMMU == 1 or valMMU == 2 or valMMU == 3 or valMMU == 13 or (valMMU == 4 and m[mouse+i+17] == -1):
                        c[mouse+i] = 7
                else:
                    if valset(mouse+i,False)[1] != 13 or valMMU == 1 or valMMU == 2 or valMMU == 3 or valMMU == 13 or (valMMU == 4 and m[mouse+i+17] == -1):
                        c[mouse+i] += 4
                keep = False
            i -= 34
        i = 34
        keep = True
        while mouse+i < 289 and keep:
            if b[mouse+i] != t and b[mouse+i] != 0:
                zd = mouse+i
                if valset(mouse+i,False)[1] != 13 or valMMU == 1 or valMMU == 2 or valMMU == 3 or valMMU == 13 or (valMMU == 4 and m[mouse+i-17] == -1):
                    if c[mouse+i] == 0:
                        c[mouse+i] = 7
                    else:
                        c[mouse+i] += 4
                keep = False
            i += 34
 
def valset(where,whereUp):
    if m[where] > 19:
        if whereUp:
            valMMD = m[where] // 20
            valMMU = m[where] // 20
            valMMO = True
        else:
            valMMD = m[where] % 20
            valMMU = m[where] // 20
            valMMO = False
    else:
        valMMD = m[where]
        valMMU = m[where]
        valMMO = True
    return [valMMD,valMMU,valMMO]
 
def first_set(mouseUp):
    global tag,tagUp
    if not mouseUp or (mouseUp and m[mouse]>19):
        valMMD,valMMU,valMMO = valset(mouse,mouseUp)[0],valset(mouse,mouseUp)[1],valset(mouse,mouseUp)[2]
        each_reset()
        switch_dict(valMMD,valMMU,valMMO,t,mouse)
        tag = mouse
        tagUp = mouseUp
 
def appleDel(mouse,tag):
    for j in whichToEta(valset(tag,tagUp)[0],mouse-tag):
        if (j < mouse and tag < j) or (j < tag and mouse < j):
            m[int(j)] = b[int(j)] = 0
 
def whale(t,where,self):
    global m,b
    for i in [-36,-34,-32,-2,2,32,34,36]:
        if move_limit(i):
            if b[where+i] != t:
                if valset(where+i,False)[1] == 18:
                    m[self] = 0
                if valset(where+i,False)[1] != 13 and (valset(where+i,False)[1] != 15 or i == 34 or i == -34):
                    m[where+i] = 0
                    b[where+i] = 0
 
def toPen():
    for i in range(17):
        down = m[i]%20
        up = m[i]//20
        if b[i] == 1:
            if up == 4 or up == 6 or up == 7 or up == 10:
                m[i] -= up*20
                m[i] += 380
            if down == 4 or down == 6 or down == 7 or down == 10:
                m[i] -= down
                m[i] += 19
    for i in range(272,289):
        down = m[i]%20
        up = m[i]//20
        if b[i] == 2:
            if up == 4 or up == 6 or up == 7 or up == 10:
                m[i] -= up*20
                m[i] += 380
            if down == 4 or down == 6 or down == 7 or down == 10:
                m[i] -= down
                m[i] += 19
 
def born():
    each_reset()
    second_reset()
    output()
    if t == 1:
        pygame.draw.line(screen,(0,0,0),[dist_wd-int(0.5*bdone),dist_hi+int(10.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi+int(10.5*bdone)],linewd)
        pygame.draw.line(screen,(0,0,0),[dist_wd+int(9.5*bdone),dist_hi+int(9.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi+int(10.5*bdone)],linewd)
    else:
        pygame.draw.line(screen,(0,0,0),[dist_wd-int(0.5*bdone),dist_hi-int(0.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi-int(0.5*bdone)],linewd)
        pygame.draw.line(screen,(0,0,0),[dist_wd+int(9.5*bdone),dist_hi-int(1.5*bdone)],[dist_wd+int(9.5*bdone),dist_hi-int(0.5*bdone)],linewd)
    for i in range(1,11):
        if t==1:
            screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\background\\vkImage0.png").convert(),(bdone,bdone)),(dist_wd+int((i-1.5)*bdone),dist_hi+int(9.5*bdone)))
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\background\\vkImage0.png").convert(),(bdone,bdone)),(dist_wd+int((9.5-i)*bdone),dist_hi-int(1.5*bdone)))
    for i in range(1,11):
        if t==1:
            screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(i)+"_"+str(t)+".png").convert_alpha(),(bdone,bdone)),(dist_wd+int((i-1.5)*bdone),dist_hi+int(9.5*bdone)))
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(i)+"_"+str(t)+".png").convert_alpha(),(bdone,bdone)),(dist_wd+int((9.5-i)*bdone),dist_hi-int(1.5*bdone)))
    pygame.display.update()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if t == 1:
                x = int(event.pos[0] - dist_wd + 0.5*bdone)
                y = int(event.pos[1] - dist_hi - 9.5*bdone)
                if 0 < x and x < 10*bdone and 0 < y and y < bdone:
                    if m[280] != 0:
                        m[280] += (1+int(x//bdone)) * 20
                    else:
                        m[280] = 1+int(x//bdone)
                        b[280] = 1
                    break
            else:
                x = event.pos[0] - dist_wd + 0.5*bdone
                y = event.pos[1] - dist_hi + 1.5*bdone
                if 0 < x and x < 10*bdone and 0 < y and y < bdone:
                    if m[8] != 0:
                        m[8] += int(10-(x//bdone)) * 20
                    else:
                        m[8] = 10-int(x//bdone)
                        b[8] = 2
                    break
    output()
    pygame.display.update()
 
def howManyKmdl():
    kmdl = 0
    for i in range(289):
        if b[i] == t and (m[i] == 1 or m[i] // 20 == 1 or m[i] % 20 == 1):
            kmdl += 1
    return kmdl
 
def second_set():
    if valset(tag,False)[1] == 14 or ((c[mouse] == 2 or c[mouse] == 3 or c[mouse] == 5 or c[mouse] == 6) and valset(tag,False)[1] == 5):
        whale(t,mouse,tag)
    if valset(tag,tagUp)[0] == 17:
        m[mouse],m[tag] = m[tag],m[mouse]
        if m[tag]//20 == 14 or (m[tag] < 20 and m[tag] == 14):
            whale(t,tag,tag)
        toPen()
    else:
        if (c[mouse] == 2 or c[mouse] == 3 or c[mouse] == 4 or c[mouse] == 5 or c[mouse] == 6) and valset(tag,tagUp)[1] == 1:
            kmdlborn = True
        else:
            kmdlborn = False
        if c[mouse] == 2 or c[mouse] == 3 or c[mouse] == 5 or c[mouse] == 6:
            appleDel(mouse,tag)
        if c[mouse] == 4 or c[mouse] == 5 or c[mouse] == 6:
            if valset(mouse,False)[1] == 18 and not (valset(tag,tagUp)[1] == 13 or (valset(tag,tagUp)[1] == 4 and (c[mouse] == 5 or c[mouse] == 6))) and not (valset(tag,tagUp)[1] == 15 and ((mouse-tag)%34) != 0):
                m[mouse] = b[mouse] = 0
            else:
                if tagUp:
                    if c[mouse] == 5:
                        if (m[tag]//20) < 11 and (m[tag]//20) != 1 and (m[tag]//20) != 2 and (m[tag]//20) != 3:
                            m[mouse] = m[tag] // 20 + 9
                        else:
                            m[mouse] = m[tag] // 20
                    else:
                        m[mouse] = m[tag] // 20
                else:
                    if c[mouse] == 5:
                        if m[tag] < 11 and m[tag] != 1 and m[tag] != 2 and m[tag] != 3:
                            m[mouse] = m[tag] + 9
                        else:
                            m[mouse] = m[tag]
                    else:
                        m[mouse] = m[tag]
                    b[tag] = 0
                if m[mouse] != 0:
                    b[mouse] = t
        elif c[mouse] == 1 or c[mouse] == 2 or c[mouse] == 3:
            if m[mouse] == 0:
                if tagUp:
                    if c[mouse] == 2:
                        if (m[tag]//20) < 11 and (m[tag]//20) != 1 and (m[tag]//20) != 2 and (m[tag]//20) != 3:
                            m[mouse] = m[tag] // 20 + 9
                        else:
                            m[mouse] = m[tag] // 20
                    else:
                        m[mouse] = m[tag] // 20
                else:
                    if c[mouse] == 2:
                        if m[tag] < 11 and m[tag] != 1 and m[tag] != 2 and m[tag] != 3:
                            m[mouse] = m[tag] + 9
                        else:
                            m[mouse] = m[tag]
                    else:
                        m[mouse] = m[tag]
                    b[tag] = 0
                if m[mouse] != 0:
                    b[mouse] = t
            else:
                if tagUp:
                    if c[mouse] == 2:
                        if (m[tag]//20) < 11 and (m[tag]//20) != 1 and (m[tag]//20) != 2 and (m[tag]//20) != 3:
                            m[mouse] += (m[tag] // 20 + 9) * 20
                        else:
                            m[mouse] += (m[tag] // 20) * 20
                    else:
                        m[mouse] += (m[tag] // 20) * 20
                else:
                    if c[mouse] == 2:
                        if m[tag] < 11 and m[tag] != 1 and m[tag] != 2 and m[tag] != 3:
                            m[mouse] += (m[tag] + 9) * 20
                        else:
                            m[mouse] += m[tag] * 20
                    else:
                        m[mouse] += m[tag] * 20
                    b[tag] = 0
        if tagUp:
            m[tag] %= 20
        else:
            m[tag] = 0
            b[tag] = 0
        if c[mouse] == 3 or c[mouse] == 6:
            m[mouse] = 0
            b[mouse] = 0
        toPen()
        if kmdlborn and ((m[280]<20 and (b[280] == 1 or b[280] == 0) and t == 1) or (m[8]<20 and (b[8] == 2 or b[8] == 0) and t == 2)):
                born()
 
def shotPosion():
    kmdlborn = False
    if m[tag] // 20 == 1:
        kmdlborn = True
    if m[tag]//20 == 14:
        whale(t,mouse,tag)
    if valset(mouse,False)[1] == 18 and valset(tag,tagUp) != 13:
        m[tag] = 0
        b[tag] = 0
    m[mouse] = 0
    b[mouse] = 0
    if kmdlborn:
        born()
 
def m_output(i):
    if i % 2 == 0 and i % 34 < 17:
        if m[i] > 19:
            if b[i] == 1:
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(m[i]//20)+"_"+str(b[i])+".png").convert_alpha(),(bdone//2,bdone//2)),(((i%17)//2)*bdone+bdone//4+dist_wd,((i//17)//2)*bdone+dist_hi))
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(m[i]%20)+"_"+str(b[i])+".png").convert_alpha(),(bdone//2,bdone//2)),(((i%17)//2)*bdone+bdone//4+dist_wd,((i//17)//2)*bdone+bdone//2+dist_hi))
            else:
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(m[i]//20)+"_"+str(b[i])+".png").convert_alpha(),(bdone//2,bdone//2)),(((i%17)//2)*bdone+bdone//4+dist_wd,((i//17)//2)*bdone+bdone//2+dist_hi))
                screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(m[i]%20)+"_"+str(b[i])+".png").convert_alpha(),(bdone//2,bdone//2)),(((i%17)//2)*bdone+bdone//4+dist_wd,((i//17)//2)*bdone+dist_hi))
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(m[i])+"_"+str(b[i])+".png").convert_alpha(),(bdone,bdone)),(((i%17)//2)*bdone+dist_wd,((i//17)//2)*bdone+dist_hi))
    elif m[i]:
        screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\chess\\vkImage"+str(m[i])+"_"+str(b[i])+".png").convert_alpha(),(bdone//2,bdone//2)),((i%17*bdone//2)+(bdone//4)+dist_wd,(i//17*bdone//2)+(bdone//4)+dist_hi))
 
def output():
    screen.blit(disp,(0,0))
    for i in range(0,289,2):
        if i % 34 > 17:
            i+=16
        screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\background\\vkImage"+str(c[i])+".png").convert(),(bdone,bdone)),(((i%17)//2)*bdone+dist_wd,((i//17)//2)*bdone+dist_hi))
    for i in range(289):
        m_output(i)
    pygame.draw.line(screen,(0,0,0),[dist_wd,dist_hi+9*bdone],[dist_wd+9*bdone,dist_hi+9*bdone],linewd)
    pygame.draw.line(screen,(0,0,0),[dist_wd+9*bdone,dist_hi],[dist_wd+9*bdone,dist_hi+9*bdone],linewd)
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\\image\\other\\undo.png").convert(),(bdone,bdone)),(int(-1.5*bdone+dist_wd),8*bdone+dist_hi))
    pygame.draw.line(screen,(0,0,0),[int(-0.5*bdone+dist_wd),8*bdone+dist_hi],[int(-0.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(-1.5*bdone+dist_wd),9*bdone+dist_hi],[int(-0.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\\image\\other\\change.png").convert(),(bdone,bdone)),(int(-1.5*bdone+dist_wd),int(6.5*bdone+dist_hi)))
    pygame.draw.line(screen,(0,0,0),[int(-0.5*bdone+dist_wd),int(6.5*bdone+dist_hi)],[int(-0.5*bdone+dist_wd),int(7.5*bdone+dist_hi)],linewd)
    pygame.draw.line(screen,(0,0,0),[int(-1.5*bdone+dist_wd),int(7.5*bdone+dist_hi)],[int(-0.5*bdone+dist_wd),int(7.5*bdone+dist_hi)],linewd)
    if ischange:
        screen.blit(first,(int(-1.5*bdone+dist_wd),dist_hi))
        screen.blit(second,(int(9.5*bdone+dist_wd),8*bdone+dist_hi))
    else:
        screen.blit(first,(int(9.5*bdone+dist_wd),8*bdone+dist_hi))
        screen.blit(second,(int(-1.5*bdone+dist_wd),dist_hi))
    pygame.draw.line(screen,(0,0,0),[int(-0.5*bdone+dist_wd),dist_hi],[int(-0.5*bdone+dist_wd),bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(-1.5*bdone+dist_wd),bdone+dist_hi],[int(-0.5*bdone+dist_wd),bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(10.5*bdone+dist_wd),8*bdone+dist_hi],[int(10.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    pygame.draw.line(screen,(0,0,0),[int(9.5*bdone+dist_wd),9*bdone+dist_hi],[int(10.5*bdone+dist_wd),9*bdone+dist_hi],linewd)
    pygame.display.update()
 
pygame.init()
scwd = int(780)
schi = int(780)
if schi//13 > scwd//10:
    bdone = scwd//10
else:
    bdone = schi//13
bdwd = bdhi = bdone*9
dist_wd = (scwd - bdwd)//2
dist_hi = (schi - bdhi)//2
linewd = bdone//128
if linewd < 1:
    linewd = 1
screen = pygame.display.set_mode((scwd,schi))
pygame.display.set_caption("科摩多龍棋")
dir = dirname(__file__)
# dir = "C:\\遊戲類昂\\vk\\image\\pyvk_alpha0c"
icon = pygame.image.load(dir+"\\image\\chess\\vkImage1_1.png")
first = pygame.transform.scale(pygame.image.load(dir+"\\image\\other\\first.png").convert(),(bdone,bdone))
second = pygame.transform.scale(pygame.image.load(dir+"\\image\\other\\second.png").convert(),(bdone,bdone))
pygame.display.set_icon(icon)
disp = pygame.Surface(screen.get_size()).convert()
disp.fill((255,255,255))
screen.blit(disp,(0,0))
pygame.event.set_blocked(pygame.MOUSEMOTION)
each_reset()
output()
 
while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if (-1.5*bdone+dist_wd < event.pos[0] < -0.5*bdone+dist_wd) and (8*bdone+dist_hi < event.pos[1] < 9*bdone+dist_hi):
            each_reset()
            second_reset()
            t,lt=lt,t
            for i in range(289):
                m[i],b[i],lm[i],lb[i]=lm[i],lb[i],m[i],b[i]
            output()
        elif (-1.5*bdone+dist_wd < event.pos[0] < -0.5*bdone+dist_wd) and (6.5*bdone+dist_hi < event.pos[1] < 7.5*bdone+dist_hi):
            ischange = not ischange
            t ^= 3
            lt^=3
            m.reverse()
            b.reverse()
            lm.reverse()
            lb.reverse()
            c = [0] * 289
            for i in range(0,289,2):
                if m[i]:
                    b[i] ^= 3
                if lm[i]:
                    lb[i] ^= 3
            output()
        else:
            x = event.pos[0] - dist_wd
            y = event.pos[1] - dist_hi
            if x >= 0 and x < bdwd and y >= 0 and y < bdhi:
                mouse = x//bdone*2+y//bdone*34
                if y%bdone < bdone//2:
                    mouseUp = True
                if t != 1:
                    mouseUp = not mouseUp
                if m[mouse] < 20 and b[mouse] == t:
                    mouseUp = False
                if (m[mouse] > 0 and b[mouse] == t and (not mouseUp or m[mouse]>19)) or c[mouse] != 0:
                    if tag == -1 and mouse != -1:
                        # check(0)
                        first_set(mouseUp)
                        # check()
                    elif c[mouse] > 0:
                        lt=t
                        lm = [i for i in m]
                        lb = [i for i in b]
                        if c[mouse] > 6:
                            if t!=1:
                                mouseUp = not mouseUp
                            if c[mouse] == 7:
                                mouseUp = True
                            if mouseUp:
                                shotPosion()
                            else:
                                c[mouse] -= 4
                                second_set()
                        else:
                            second_set()
                        t ^= 3
                        if not howManyKmdl():
                            break
                        each_reset()
                        second_reset()
                    else:
                        each_reset()
                        second_reset()
                    output()
                else:
                    each_reset()
                    second_reset()
                    output()
output()
if t==1:
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\other\\lose.png").convert_alpha(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi+int(9.5*bdone)))
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\other\\win.png").convert_alpha(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi-int(1.5*bdone)))
else:
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\other\\win.png").convert_alpha(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi+int(9.5*bdone)))
    screen.blit(pygame.transform.scale(pygame.image.load(dir+"\\image\\other\\lose.png").convert_alpha(),(bdone*3,bdone)),(dist_wd+3*bdone,dist_hi-int(1.5*bdone)))
pygame.display.update()
while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()