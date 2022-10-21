//2022/10/21 0.1.7.1
/*未完成
準備上色跟更多優化
*/
/*definition of structs and functions
struct sMap{U C b:2,me:2,p:1,e:1,up:5,down:5}m[81];
struct control{U C t:1,kmdlborn:1,zu:7,zd:7,mouse:8,tag:8}c;//kmdlborn用不到了,sad
r=reset  ml=move limit  ft=foot and turtle  pf=poisonfrog  ia=is apple  mo=move  we=which to eta  sd=switch dict  fs=first set  wh=whale  tp=to pen  sp=shot poison  bo=born  ar=apple range  ss=second set
(in many functions)w=where  s=self  u=up  d=down  th=there*/
/*註解略寫 //請使用ctrl+f自行搜尋
[t差] t=目的地差值
[wu] whereUp=where(兩高用.up,一高用.down)
[su] selfUp=self(兩高用.up,一高用.down)
[w鱷龜] if(w無鱷龜)=1; elif同直行=1; else 0;
*/

#include <stdio.h>
#include <stdlib.h>
#define U unsigned
#define C char
#define V void
#define R return
#define WS U C w,U C s
#define T C t
#define cr(i,j) case i:R j;
#define clr(i,j) case i:R l&1<<j?j:8;
U short int m[81]={
0x8007,0x8005,0x8004,0x8003,0x8001,0x8002,0x8004,0x8005,0x8006,
     0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
     0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
0x4006,0x4005,0x4004,0x4002,0x4001,0x4003,0x4004,0x4005,0x4007};
U int c=0x3fff7f7f;U C l=0xef,eta[8]={0};//c{t,kmdlborn,mouseUp,tagUp=0;其他=1;} l{[4]=0;其他=1;} eta清空
V r(){//只有迴圈能壓的reset
    U C i=8;while(i--)eta[i]=0;//eta清空
    i=81;while(i--)m[i]&=0xc3ff;c|=0x3fff0000;//m[i].c,zu,zd清空
}
U C ml(WS){//無規律只能窮舉
    switch(w-s){
        cr(-10,s%9&&s>8);
        cr(-9,s>8);//非最上橫排
        cr(-8,s%9^8&&s>8);
        cr(-1,s%9);//非最左橫排
        cr(1,s%9^8);//非最右橫排
        cr(8,s%9&&s<72);
        cr(9,s<72);//非最下橫排
    }
    R s%9^8&&s<72;
    //剩的自己排列組合
}
U C ft(WS){//s=mou(==ts)
    U C wu=m[w]>>(m[w]&0x3e0?5:0)&0x1f,su=m[s]>>(m[s]&0x3e0?5:0)&0x1f;//[wu]
    if(su<4)R 1;//if(su==1||su==2||su==3)R 1;
    if(wu^13)R wu^15||!((w-s)%9);//if(w沒大腳怪)[w鱷龜]
    //w大腳怪
        if(su^13)R 0;R wu^15||!((w-s)%9);//if(s沒大腳怪)[w鱷龜]
}
U C pf(WS){
    U C wu=m[w]>>(m[w]&0x3e0?5:0)&0x1f;//[wu]
    if(wu^18)R 0;//w沒箭毒蛙
    //w箭毒蛙
        U C su=m[s]>>(m[s]&0x3e0?5:0)&0x1f;//[su]
        if(su^15)R su^13;//if(s無鱷龜)R if(s大腳怪)=1; else  0;
        R !((w-s)%9);//s鱷龜 if(同直行)=1; else=0;
}
U C ia(WS){
    if(s%9==w%9){//同直排
        switch(s>w?w:s){//switch偏上者
            clr(27,0);
            clr(29,1);
            clr(33,2);
            clr(35,3);
            clr(38,5);
            clr(42,6);
            clr(44,7);
    }   }
    R 8;//不同排,後面ap^8即此意
}
U C mo(WS,U C epa){//e=evolution p=ispoison a=whichEta//R &1keep &2p &4e
    U C mou=c>>8&0x7f;
    if(ml(w,s)){
        if(m[w]>>14==(c>>31?1:2)){//敵人//吃人無論如何都是return 0
            if(ft(w,mou)){
                U C ap=ia(w,s);
                m[w]|=0x2000;//m[w].me=2
                if(epa&16||ap^8){//見ia()
                    m[w]|=0x400;//m[w].e=1
                    eta[epa&7]|=1<<ap;//eta[a]加入第ap個銅錢草
                    if(epa&8||~c&0x8000&&m[mou]&0x3e0){m[w]|=0x800;R 6;}//if(p||(!mouseUp&&m[s].up))m[w].p=1
                    R 4;
        }   }   }
        else if(!m[w]||!(m[w]&0x3e0)&&(c&0x8000||!(m[mou]&0x3e0))){//m[w]空||(m[w].up空&&(mouseUp||m[s].up空))
            U C ap=ia(w,s);
            m[w]|=0x1000;//m[w].me=1
            if(epa&16||ap^8){
                m[w]|=0x400;
                eta[epa&7]|=1<<ap;
                if(epa&8||~c&0x8000&&m[mou]&0x3e0){
                    m[w]|=0x800;
                    R 6|!(m[w]&0x1f);
                }
                R 4|!(m[w]&0x1f);
            }
            R !(m[w]&0x1f);
    }   }
    R 0;//所有沒return,要中斷迴圈都來這
}
U C wh(T){//t=where只是省字用
    C movelist[]={-10,-9,-8,-1,1,8,9,10},p=0;//八格遍歷,只能窮舉
    for(U C th,tu,i=0;i^8;++i){
        th=t+movelist[i];
        tu=m[th]>>(m[th]&0x3e0?5:0)&0x1f;
        if(ml(t,th)&&m[th]>>14==(c>>31?1:2)&&tu^13&&(tu^15||i==1||i==6)){
            if(tu==18)p=1;//自己頭上必鯨魚
            m[th]=0;
    }   }
    R p;
}
V tp(){
    U C i=72,up,down;
    for(;i^81;++i){
        if(m[i]&0x8000){//b==2
            up=m[i]>>5&0x1f,down=m[i]&0x1f;
            if(up&&(up==6||up==7||up==4||up==10))m[i]=m[i]&0xfc1f|0x260;//頭up只是拿來加速短路
            if(down==6||down==7||down==4||down==10)m[i]=m[i]&0xffe0|0x13;
    }   }
    for(i=0;i^9;++i){
        if(m[i]&0x4000){//b==1
            up=m[i]>>5&0x1f,down=m[i]&0x1f;
            if(up&&(up==6||up==7||up==4||up==10))m[i]=m[i]&0xfc1f|0x260;//頭up只是拿來加速短路
            if(down==6||down==7||down==4||down==10)m[i]=m[i]&0xffe0|0x13;
}   }   }
V nco();
C o[]={
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
"#    #    #    #    #    #    #    #    #    #\n"
"#    #    #    #    #>   #    #    #    #    #\n"
"#    #    #    #    #    #    #    #    #    #\n"
"##############################################\n"
};
V bo(){
    r();
    nco();
    U C kgc,knm=1,ko[]={">1 2 3 4 5 6 7 8 9 10"},nm=c>>31?4:76;
    o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+1]=' ',o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+48]=' ';
    if((c>>31&&m[4]&0x3e0)||(~c>>31&&m[76]&0x3e0)){nm|=0x80;o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+1]='>';}
    else o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+48]='>';
    while(1){
        ko[(knm-1)<<1]='>';
        system("cls");
        printf("%s\n%s",o,ko);
        ko[(knm-1)<<1]=' ';
        do /*scanf("%c",&kgc);*/kgc=getchar(); while(kgc=='\t'||kgc=='\n');
        kgc|=0x20;
        if(kgc==97){--knm;if(!knm)knm=10;}
        else if(kgc==100){++knm;if(knm==11)knm=1;}
        else if(kgc==32){m[nm]|=knm<<(m[nm]?5:0)|(c&0x80000000?0x8000:0x4000);o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+48]=' ';nco();break;}
}   }
U C hk(U T){
    for (U C i=0;i^81;++i)if((m[i]>>14)-1==t&&((m[i]&0x1f)==1||(m[i]&0x3e0)==32))R 1;
    R 0;
}
U C ar(WS){
    if(w>s)w^=s^=w^=s;//w恆小
    R (w<=27&&s>=36)|(w<=29&&s>=38)<<1|(w<=33&&s>=42)<<2|(w<=35&&s>=44)<<3|(w<=38&&s>=47)<<5|(w<=42&&s>=51)<<6|(w<=44&&s>=53)<<7;
}
V ss(){
    U C w=c>>8&0x7f,s=c&0x7f,tu=m[s]>>(m[s]&0x3e0?5:0)&0x1f,td=m[s]>>(c&0x80?5:0)&0x1f,t=c>>31;
    if(tu==14||tu==5&&m[w]&0x400)m[w]|=wh(w)?0x800:0;//if(tu鯨魚||(tu鯰魚&&m[w].e)whale
    if(td==17){//鬣蜥
        m[s]^=m[w]^=m[s]^=m[w];//換
        if((m[s]>>(m[s]&0x3e0?5:0)&0x1f)==14)if(wh(s))m[s]=0;//wh
        tp();//to pen
    }
    else{
        if(m[w]&0x400){
            C we=w-s;
            l^=eta[td^7?(we<0?we%10?we%9?we%8?3:2:1:0:we%10?we%9?we%8?4:5:6:7):t?(we%9^1?5:7):we%9^-1?2:0]&ar(w,s);//appleDel
        }
        if(m[w]&0x2000){//吃
            if(pf(w,s))m[w]&=0x3c00;//wb=wu=wd=0
            else{
                m[w]=(m[w]&0x3c00)|td|(t+1<<14);//wb=t+1,wd=td,wu=0
                if(m[s]&0x3e0
                &&~c&0x80)m[w]|=tu<<5;//if(tu&&!tagUp)wu=tu
        }   }
        else if(m[w]>>14)m[w]|=tu<<5;//if(wb)wu=tu
        else{
            m[w]|=td|(t+1<<14);//wd=td,wb=tb
            if(m[s]&0x3e0&&~c&0x80)m[w]|=tu<<5;//if(su&&!tagUp)wu=tu
        }
        if(m[w]&0x400&&tu^1&&tu^2&&tu^3&&tu<11)m[w]+=9<<(m[w]&0x3e0?5:0);//if((m[w].e)&&(tu^1)&&(tu^2)&&(tu^3)&&未進化)m[w].down=tu+9;//進化
        m[s]&=0xfc1f;//su=0;
        if(~c&0x80)m[s]&=0x3fe0;//if(!tagUp)sd=sb=0;
        if(m[w]&0x800)m[w]&=0x3c00;//if(m[w].p)wu=wd=wb=0
        tp();
        if(tu==1&&m[w]&0x2400){//if(tu=1&&(m[w].me=2||m[w].e))
            if(t){if(!(m[4]&0x4000)&&!(m[4]&0x3e0))bo();}//if(後手)if(m[4].b!=1&&m[4].up空)born()
            else if(!(m[76]&0x8000)&&!(m[76]&0x3e0))bo();//else if(m[76].b!=2&&m[76].up空)born()
        }
}   }
V sp(){
    U C w=c>>8&0x7f,s=c&0x7f;
    if((m[s]>>5&0x1f)==14)if(wh(w))m[s]=0;
    c|=((m[s]>>5&0x1f)==1)<<30;
    if(pf(w,s))m[s]&=0x3c00;
    if(ft(w,s))m[w]&=0x3c00;
    if(c&0x40000000){
        if(t){if(!(m[4]&0x4000)&&!(m[4]&0x3e0))bo();}//if(後手)if(m[4].b!=1&&m[4].up空)born()
        else if(!(m[76]&0x8000)&&!(m[76]&0x3e0))bo();//else if(m[76].b!=2&&m[76].up空)born()
    }
    c&=0xbfffffff;
}
/*
o[num]=o[48+num/9*188+num%9*5+x];
x=if c|nm up 0
elif c|nm !up 47
elif u 2 & 3 =%2d
elif d 2+47 & 3+47 =%2d
elif x{s} 1
elif y{m,e,k,p} 1+47
>suu
 {mekp}dd
*/
#define gco system("cls");printf("%s",o)
V nco(){
    U int p=46,i,j;
    for(i=0;i^9;++i){
        for(j=0;j^9;++j){
            p+=3;o[p]=' ';++p;
            if((m[i*9+j]>>5&0x1f)>9){o[p]='0'+(m[i*9+j]>>5&0x1f)/10;++p;o[p]='0'+(m[i*9+j]>>5&0x1f)%10;}
            else if(m[i*9+j]&0x3e0){o[p]=' ';++p;o[p]='0'+(m[i*9+j]>>5&0x1f)%10;}
            else{o[p]=' ';++p;o[p]=' ';}
        }p+=2;
        for(j=0;j^9;++j){
            p+=3;o[p]=' ';++p;
            if((m[i*9+j]&0x1f)>9){o[p]='0'+(m[i*9+j]&0x1f)/10;++p;o[p]='0'+(m[i*9+j]&0x1f)%10;}
            else if(m[i*9+j]&0x1f){o[p]=' ';++p;o[p]='0'+(m[i*9+j]&0x1f)%10;}
            else{o[p]=' ';++p;o[p]=' ';}
        }p+=2;
        for(j=0;j^9;++j){
            p+=3;
            if(m[i*9+j]&0x8000){o[p]='2';++p;o[p]='n';++p;o[p]='d';}
            else if(m[i*9+j]&0x4000){o[p]='1';++p;o[p]='s';++p;o[p]='t';}
            else{o[p]=' ';++p;o[p]=' ';++p;o[p]=' ';}
        }p+=49;
    }
    o[754]=o[755]=l&1?'a':'#';o[764]=o[765]=l&2?'a':'#';o[784]=o[785]=l&4?'a':'#';o[794]=o[795]=l&8?'a':'#';
    o[952]=o[953]=l&32?'a':'#';o[972]=o[973]=l&64?'a':'#';o[982]=o[983]=l&128?'a':'#';
    gco;
}
V co(){
    U int p=96,i,j;
    for(i=0;i^9;++i){
        for(j=0;j^9;++j){
            if(m[i*9+j]&0x800)o[p]='p';else if(m[i*9+j]&0x2000)o[p]='k';else if(m[i*9+j]&0x400)o[p]='e';else if(m[i*9+j]&0x1000)o[p]='m';p+=5;
        }p+=143;
    }
    U C nm=c>>16&0x7f;
    if(nm^127)o[48+nm/9*188+nm%9*5+1]='s';
    nm=c>>23&0x7f;
    if(nm^127)o[48+nm/9*188+nm%9*5+1]='s';
    gco;
}
#define cdel o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5]=' ',o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5+47]=' '
#define cadd o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5+47]='>';nm&=0x7f
int main(){
    nco();
    U C gc,nm=76,end=1;
    while(end){
        do /*scanf("%c",&gc);*/gc=getchar(); while(gc=='\t'||gc=='\n');
        gc|=0x20;
        switch(gc){
            case 97:cdel;if((nm&0x7f)%9)--nm;else nm+=8;cadd;gco;break;
            case 100:cdel;++nm;if((nm&0x7f)%9==0)nm-=9;cadd;gco;break;
            case 115:cdel;nm+=9;if((nm&0x7f)>80)nm-=81;cadd;gco;break;
            case 119:cdel;if((nm&0x7f)<9)nm+=72;else nm-=9;cadd;gco;break;
            case 113:
                if(m[nm]&0x3e0||(nm^127&&((nm==(c>>23&0x7f))||(nm==(c>>16&0x7f))))){
                    o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5+47]=nm&0x80?'>':' ';
                    o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5]=nm&0x80?' ':'>';
                    nm^=0x80;gco;
                }
                break;
            case 59:R 0;
            case 32:
                c=c&0xffff00ff|nm<<8;//mou=nm&0xff
                if(((c&0x7f)==127)&&(m[c>>8&0x7f]>>14==(c>>31)+1)){//if((tag==127(|255))&&m[mou]t)
                    if(!(m[c>>8&0x7f]&0x3e0))c&=0xffff7fff;//if(m[mouse].up空)mouseUp=0
                    r();
                    U T=c>>31,s=c>>8&0x7f;//t=c.t,s=mouse
                    switch(m[c>>8&0x7f]>>(c&0x8000?5:0)&0x1f){
                        C i,j;
                        case 16:
                            for(i=s-9;i>=0;i-=9){
                                //printf("%d\n",i);
                                if(m[i]>>14==(t?1:2)){//敵人
                                    if(ft(i,s)){c=c&0xc07fffff|i<<23;}//zu
                                    break;
                            }   }
                            for(i=s+9;i<81;i+=9){
                                if(m[i]>>14==(t?1:2)){
                                    if(ft(i,s)){c=c&0xff80ffff|i<<16;}//zd
                                    break;
                            }   }//沒錯case 16後面接著判八格
                        case 1:case 13:case 14:case 15:
                            mo(s-1,s,3);mo(s+1,s,4);
                        case 2:
                            mo(s-10,s,0);mo(s-9,s,1);mo(s-8,s,2);
                            mo(s+8,s,5);mo(s+9,s,6);mo(s+10,s,7);break;//前面的到這裡一起break
                        case 3:
                            mo(s-10,s,0);mo(s-8,s,2);mo(s-1,s,3);
                            mo(s+1,s,4);mo(s+8,s,5);mo(s+10,s,7);break;
                        case 4:case 10:
                            t?mo(s+9,s,6):mo(s-9,s,1);break;
                        case 5:
                            mo(s-9,s,1);mo(s-1,s,3);mo(s+1,s,4);mo(s+9,s,6);break;
                        case 6:
                            if(t){
                                for(i=s,j=1;j&1;i+=10)j=mo(i+10,i,7|j<<2&0x18);//所有loop mo都是先&在|
                                for(i=s,j=1;j&1;i+=9)j=mo(i+9,i,6|j<<2&0x18);
                                for(i=s,j=1;j&1;i+=8)j=mo(i+8,i,5|j<<2&0x18);
                                break;
                            }
                            for(i=s,j=1;j&1;i-=8)j=mo(i-8,i,2|j<<2&0x18);
                            for(i=s,j=1;j&1;i-=9)j=mo(i-9,i,1|j<<2&0x18);
                            for(i=s,j=1;j&1;i-=10)j=mo(i-10,i,0|j<<2&0x18);
                            break;
                        case 7:
                            if(t){
                                for(i=s+10,j=mo(s+10,s,7);j&1;i+=9)j=mo(i+9,i,7|j<<2&0x18);
                                for(i=s+8,j=mo(s+8,s,5);j&1;i+=9)j=mo(i+9,i,5|j<<2&0x18);
                                break;
                            }
                            for(i=s-8,j=mo(s-8,s,2);j&1;i-=9)j=mo(i-9,i,2|j<<2&0x18);
                            for(i=s-10,j=mo(s-10,s,0);j&1;i-=9)j=mo(i-9,i,0|j<<2&0x18);
                            break;
                        case 8:
                            mo(s-9,s,1);
                            mo(s+9,s,6);
                            for(i=s,j=1;j&1;--i)j=mo(i-1,i,3|j<<2&0x18);
                            for(i=s,j=1;j&1;++i)j=mo(i+1,i,4|j<<2&0x18);
                            break;
                        case 9:case 18:{//這括號不加不能宣告ap,p 編譯器全責
                            U C ap,p=m[s]&0x3e0&&~c&0x8000;//will p
                            for(i=s-9,j=1;i>=0;i-=9){
                                ap=ia(i+9,i);
                                if(ap^8){j=p?7:5;eta[1]|=1<<ap;}
                                if(m[i]){i-=9;break;}
                            }
                            for(;i>=0;i-=9)j=mo(i,i+9,1|j<<2&0x18);
                            for(i=s-1,j=1;(i+1)%9;--i){
                                ap=ia(i+1,i);
                                if(ap^8){j=p?7:5;eta[3]|=1<<ap;}
                                if(m[i]){--i;break;}
                            }
                            for(;(i+1)%9;--i)j=mo(i,i+1,3|j<<2&0x18);
                            for(i=s+1,j=1;i%9;++i){
                                ap=ia(i-1,i);
                                if(ap^8){j=p?7:5;eta[4]|=1<<ap;}
                                if(m[i]){++i;break;}
                            }
                            for(;i%9;++i)j=mo(i,i-1,4|j<<2&0x18);
                            for(i=s+9,j=1;i<81;i+=9){
                                ap=ia(i-9,i);
                                if(ap^8){j=p?7:5;eta[6]|=1<<ap;}
                                if(m[i]){i+=9;break;}
                            }
                            for(;i<81;i+=9)j=mo(i,i-9,6|j<<2&0x18);
                            break;
                        }
                        case 17:for(i=0;i^81;++i)if(m[i]>>14==t+1&&s^i)m[i]|=0x1000;break;
                        case 19:
                            for(i=s,j=1;j&1;i-=9)j=mo(i-9,i,1|j<<2&0x18);
                            for(i=s,j=1;j&1;--i)j=mo(i-1,i,3|j<<2&0x18);
                            for(i=s,j=1;j&1;++i)j=mo(i+1,i,4|j<<2&0x18);
                            for(i=s,j=1;j&1;i+=9)j=mo(i+9,i,6|j<<2&0x18);
                    }
                    c=c^(c&0xff)|(c>>8&0xff);//tag(Up)=mouse(Up)
                    co();
                }
                else{
                    if((c>>8&0x7f^127&&(((c>>8&0x7f)==(c>>23&0x7f))||((c>>8&0x7f)==(c>>16&0x7f)))) && (c&0x8000||!(m[c>>8&0x7f]&0x3c00))){//if((mou!=127&&((mou==zu)||(mou==zd))) && (mouUp||!m[mou]mepe))
                        sp();r();c^=0x80000000;
                        if(!(hk(c>>31)&&hk(~c>>31)))end=0;
                        c=c&0xffffff00|0x7f;nco();
                    }
                    else if(m[c>>8&0x7f]&0x3c00){//if(c[])ss();
                        ss();r();c^=0x80000000;
                        if(!(hk(c>>31)&&hk(~c>>31)))end=0;c=c&0xffff0000|0x7f7f;nco();
                    }
                    else{r();c=c&0xffff0000|0x7f7f;nco();}
    }   }       }
    nco();
    if(!hk(c>>31)&&!hk(~c>>31))printf("\ndraw...?");
    else if(c>>31)printf("\nthe first player win");
    else printf("\nthe second player win");
    /*scanf("%c");*/getchar();R 0;
}
