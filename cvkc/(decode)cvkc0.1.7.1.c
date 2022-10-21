//2022/10/01 0.1.7.1
/*未完成
準備上色跟更多優化
*/
/*definition of structs and functions
struct sMap{unsigned char belongs:2,move or eat:2,poison:1,evolution:1,up:5,down:5}map[81];
struct control{unsigned char turn:1,kmdlborn:1,zebra_up:7,zebra_down:7,mouse:8,tag:8}c;//kmdlborn用不到了,sad
(in many functions)w=where  s=self  u=up  d=down  th=there*/
/*註解略寫 //請使用ctrl+f自行搜尋
[t差] t=目的地差值
[wu] whereUp=where(兩高用.up,一高用.down)
[su] selfUp=self(兩高用.up,一高用.down)
[w鱷龜] if(w無鱷龜)=1; elif同直行=1; else 0;
*/

#include <stdio.h>
#include <stdlib.h>
#define clr(i,j) case i:return l&1<<j?j:8;
unsigned short int map[81]={
0x8007,0x8005,0x8004,0x8003,0x8001,0x8002,0x8004,0x8005,0x8006,
     0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
     0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
0x4006,0x4005,0x4004,0x4002,0x4001,0x4003,0x4004,0x4005,0x4007};
unsigned int c=0x3fff7f7f;unsigned char l=0xef,eat_the_apple[8]={0};//c{t,kmdlborn,mouseUp,tagUp=0;其他=1;} l{[4]=0;其他=1;} eta清空
void reset(){//只有迴圈能壓的reset
    unsigned char i=8;while(i--)eat_the_apple[i]=0;//eta清空
    i=81;while(i--)map[i]&=0xc3ff;c|=0x3fff0000;//map[i].c,zu,zd清空
}
unsigned char move_limit(unsigned char where,unsigned char self){//無規律只能窮舉
    switch(w-s){
        case -10:return s%9&&s>8;
        case -9:return s>8;//非最上橫排
        case -8:return s%9^8&&s>8;
        case -1:return s%9;//非最左橫排
        case 1:return s%9^8;//非最右橫排
        case 8:return s%9&&s<72;
        case 9:return s<72;//非最下橫排
    }
    return s%9^8&&s<72;
    //剩的自己排列組合
}
unsigned char foot_turtle(unsigned char where,unsigned char self){//s=mou(==ts)
    unsigned char wu=map[w]>>(map[w]&0x3e0?5:0)&0x1f,su=map[s]>>(map[s]&0x3e0?5:0)&0x1f;//[wu]
    if(su<4)return 1;//if(su==1||su==2||su==3)return 1;
    if(wu^13)return wu^15||!((w-s)%9);//if(w沒大腳怪)[w鱷龜]
    //w大腳怪
        if(su^13)return 0;return wu^15||!((w-s)%9);//if(s沒大腳怪)[w鱷龜]
}
unsigned char poison_frog(unsigned char where,unsigned char self){
    unsigned char wu=map[w]>>(map[w]&0x3e0?5:0)&0x1f;//[wu]
    if(wu^18)return 0;//w沒箭毒蛙
    //w箭毒蛙
        unsigned char su=map[s]>>(map[s]&0x3e0?5:0)&0x1f;//[su]
        if(su^15)return su^13;//if(s無鱷龜)return if(s大腳怪)=1; else  0;
        return !((w-s)%9);//s鱷龜 if(同直行)=1; else=0;
}
unsigned char is_apple(unsigned char where,unsigned char self){
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
    return 8;//不同排,後面ap^8即此意
}
unsigned char move(unsigned char where,unsigned char self,unsigned char epa){//e=evolution p=ispoison a=whichEta//return &1keep &2p &4e
    unsigned char mou=c>>8&0x7f;
    if(move_limit(w,s)){
        if(map[w]>>14==(c>>31?1:2)){//敵人//吃人無論如何都是return 0
            if(foot_turtle(w,mou)){
                unsigned char ap=is_apple(w,s);
                map[w]|=0x2000;//map[w].me=2
                if(epa&16||ap^8){//見ia()
                    map[w]|=0x400;//map[w].e=1
                    eat_the_apple[epa&7]|=1<<ap;//eat_the_apple[a]加入第ap個銅錢草
                    if(epa&8||~c&0x8000&&map[mou]&0x3e0){map[w]|=0x800;return 6;}//if(p||(!mouseUp&&map[s].up))map[w].p=1
                    return 4;
        }   }   }
        else if(!map[w]||!(map[w]&0x3e0)&&(c&0x8000||!(map[mou]&0x3e0))){//map[w]空||(map[w].up空&&(mouseUp||map[s].up空))
            unsigned char ap=is_apple(w,s);
            map[w]|=0x1000;//map[w].me=1
            if(epa&16||ap^8){
                map[w]|=0x400;
                eat_the_apple[epa&7]|=1<<ap;
                if(epa&8||~c&0x8000&&map[mou]&0x3e0){
                    map[w]|=0x800;
                    return 6|!(map[w]&0x1f);
                }
                return 4|!(map[w]&0x1f);
            }
            return !(map[w]&0x1f);
    }   }
    return 0;//所有沒return,要中斷迴圈都來這
}
unsigned char whale(char t){//t=where只是省字用
    char movelist[]={-10,-9,-8,-1,1,8,9,10},p=0;//八格遍歷,只能窮舉
    for(unsigned char th,tu,i=0;i^8;++i){
        th=t+movelist[i];
        tu=map[th]>>(map[th]&0x3e0?5:0)&0x1f;
        if(move_limit(t,th)&&map[th]>>14==(c>>31?1:2)&&tu^13&&(tu^15||i==1||i==6)){
            if(tu==18)p=1;//自己頭上必鯨魚
            map[th]=0;
    }   }
    return p;
}
void to_penguin(){
    unsigned char i=72,up,down;
    for(;i^81;++i){
        if(map[i]&0x8000){//b==2
            up=map[i]>>5&0x1f,down=map[i]&0x1f;
            if(up&&(up==6||up==7||up==4||up==10))map[i]=map[i]&0xfc1f|0x260;//頭up只是拿來加速短路
            if(down==6||down==7||down==4||down==10)map[i]=map[i]&0xffe0|0x13;
    }   }
    for(i=0;i^9;++i){
        if(map[i]&0x4000){//b==1
            up=map[i]>>5&0x1f,down=map[i]&0x1f;
            if(up&&(up==6||up==7||up==4||up==10))map[i]=map[i]&0xfc1f|0x260;//頭up只是拿來加速短路
            if(down==6||down==7||down==4||down==10)map[i]=map[i]&0xffe0|0x13;
}   }   }
void nco();
char o[]={
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
void born(){
    reset();
    nco();
    unsigned char kgc,knm=1,ko[]={">1 2 3 4 5 6 7 8 9 10"},nm=c>>31?4:76;
    o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+1]=' ',o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+48]=' ';
    if((c>>31&&map[4]&0x3e0)||(~c>>31&&map[76]&0x3e0)){nm|=0x80;o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+1]='>';}
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
        else if(kgc==32){map[nm]|=knm<<(map[nm]?5:0)|(c&0x80000000?0x8000:0x4000);o[47+(nm&0x7f)/9*188+(nm&0x7f)%9*5+48]=' ';nco();break;}
}   }
unsigned char howmany_kmdl(unsigned char t){
    for (unsigned char i=0;i^81;++i)if((map[i]>>14)-1==t&&((map[i]&0x1f)==1||(map[i]&0x3e0)==32))return 1;
    return 0;
}
unsigned char apple_range(unsigned char where,unsigned char self){
    if(w>s)w^=s^=w^=s;//w恆小
    return (w<=27&&s>=36)|(w<=29&&s>=38)<<1|(w<=33&&s>=42)<<2|(w<=35&&s>=44)<<3|(w<=38&&s>=47)<<5|(w<=42&&s>=51)<<6|(w<=44&&s>=53)<<7;
}
void second_set(){
    unsigned char where=c>>8&0x7f,s=c&0x7f,tu=map[s]>>(map[s]&0x3e0?5:0)&0x1f,td=map[s]>>(c&0x80?5:0)&0x1f,t=c>>31;
    if(tu==14||tu==5&&map[w]&0x400)map[w]|=whale(w)?0x800:0;//if(tu鯨魚||(tu鯰魚&&map[w].e)whale
    if(td==17){//鬣蜥
        map[s]^=map[w]^=map[s]^=map[w];//換
        if((map[s]>>(map[s]&0x3e0?5:0)&0x1f)==14)if(whale(s))map[s]=0;
        to_penguin();
    }
    else{
        if(map[w]&0x400){
            char we=w-s;
            l^=eat_the_apple[td^7?(we<0?we%10?we%9?we%8?3:2:1:0:we%10?we%9?we%8?4:5:6:7):t?(we%9^1?5:7):we%9^-1?2:0]&apple_range(w,s);//appleDel
        }
        if(map[w]&0x2000){//吃
            if(poison_frog(w,s))map[w]&=0x3c00;//wb=wu=wd=0
            else{
                map[w]=(map[w]&0x3c00)|td|(t+1<<14);//wb=t+1,wd=td,wu=0
                if(map[s]&0x3e0
                &&~c&0x80)map[w]|=tu<<5;//if(tu&&!tagUp)wu=tu
        }   }
        else if(map[w]>>14)map[w]|=tu<<5;//if(wb)wu=tu
        else{
            map[w]|=td|(t+1<<14);//wd=td,wb=tb
            if(map[s]&0x3e0&&~c&0x80)map[w]|=tu<<5;//if(su&&!tagUp)wu=tu
        }
        if(map[w]&0x400&&tu^1&&tu^2&&tu^3&&tu<11)map[w]+=9<<(map[w]&0x3e0?5:0);//if((map[w].e)&&(tu^1)&&(tu^2)&&(tu^3)&&未進化)map[w].down=tu+9;//進化
        map[s]&=0xfc1f;//su=0;
        if(~c&0x80)map[s]&=0x3fe0;//if(!tagUp)sd=sb=0;
        if(map[w]&0x800)map[w]&=0x3c00;//if(map[w].p)wu=wd=wb=0
        to_penguin();
        if(tu==1&&map[w]&0x2400){//if(tu=1&&(map[w].me=2||map[w].e))
            if(t){if(!(map[4]&0x4000)&&!(map[4]&0x3e0))born();}//if(後手)if(map[4].b!=1&&map[4].up空)born()
            else if(!(map[76]&0x8000)&&!(map[76]&0x3e0))born();//else if(map[76].b!=2&&map[76].up空)born()
        }
}   }
void shoot_poison(){
    unsigned char where=c>>8&0x7f,s=c&0x7f;
    if((map[s]>>5&0x1f)==14)if(whale(w))map[s]=0;
    c|=((map[s]>>5&0x1f)==1)<<30;
    if(poison_frog(w,s))map[s]&=0x3c00;
    if(foot_turtle(w,s))map[w]&=0x3c00;
    if(c&0x40000000)born();
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
void nco(){
    unsigned int p=46,i,j;
    for(i=0;i^9;++i){
        for(j=0;j^9;++j){
            p+=3;o[p]=' ';++p;
            if((map[i*9+j]>>5&0x1f)>9){o[p]='0'+(map[i*9+j]>>5&0x1f)/10;++p;o[p]='0'+(map[i*9+j]>>5&0x1f)%10;}
            else if(map[i*9+j]&0x3e0){o[p]=' ';++p;o[p]='0'+(map[i*9+j]>>5&0x1f)%10;}
            else{o[p]=' ';++p;o[p]=' ';}
        }p+=2;
        for(j=0;j^9;++j){
            p+=3;o[p]=' ';++p;
            if((map[i*9+j]&0x1f)>9){o[p]='0'+(map[i*9+j]&0x1f)/10;++p;o[p]='0'+(map[i*9+j]&0x1f)%10;}
            else if(map[i*9+j]&0x1f){o[p]=' ';++p;o[p]='0'+(map[i*9+j]&0x1f)%10;}
            else{o[p]=' ';++p;o[p]=' ';}
        }p+=2;
        for(j=0;j^9;++j){
            p+=3;
            if(map[i*9+j]&0x8000){o[p]='2';++p;o[p]='n';++p;o[p]='d';}
            else if(map[i*9+j]&0x4000){o[p]='1';++p;o[p]='s';++p;o[p]='t';}
            else{o[p]=' ';++p;o[p]=' ';++p;o[p]=' ';}
        }p+=49;
    }
    o[754]=o[755]=l&1?'a':'#';o[764]=o[765]=l&2?'a':'#';o[784]=o[785]=l&4?'a':'#';o[794]=o[795]=l&8?'a':'#';
    o[952]=o[953]=l&32?'a':'#';o[972]=o[973]=l&64?'a':'#';o[982]=o[983]=l&128?'a':'#';
    gco;
}
void co(){
    unsigned int p=96,i,j;
    for(i=0;i^9;++i){
        for(j=0;j^9;++j){
            if(map[i*9+j]&0x800)o[p]='p';else if(map[i*9+j]&0x2000)o[p]='k';else if(map[i*9+j]&0x400)o[p]='e';else if(map[i*9+j]&0x1000)o[p]='m';p+=5;
        }p+=143;
    }
    unsigned char nm=c>>16&0x7f;
    if(nm^127)o[48+nm/9*188+nm%9*5+1]='s';
    nm=c>>23&0x7f;
    if(nm^127)o[48+nm/9*188+nm%9*5+1]='s';
    gco;
}
#define cdel o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5]=' ',o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5+47]=' '
#define cadd o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5+47]='>';nm&=0x7f
int main(){
    nco();
    unsigned char gc,nm=76,end=1;
    while(end){
        do /*scanf("%c",&gc);*/gc=getchar(); while(gc=='\t'||gc=='\n');
        gc|=0x20;
        switch(gc){
            case 97:cdel;if((nm&0x7f)%9)--nm;else nm+=8;cadd;gco;break;
            case 100:cdel;++nm;if((nm&0x7f)%9==0)nm-=9;cadd;gco;break;
            case 115:cdel;nm+=9;if((nm&0x7f)>80)nm-=81;cadd;gco;break;
            case 119:cdel;if((nm&0x7f)<9)nm+=72;else nm-=9;cadd;gco;break;
            case 113:
                if(map[nm]&0x3e0||(nm^127&&((nm==(c>>23&0x7f))||(nm==(c>>16&0x7f))))){
                    o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5+47]=nm&0x80?'>':' ';
                    o[48+(nm&0x7f)/9*188+(nm&0x7f)%9*5]=nm&0x80?' ':'>';
                    nm^=0x80;gco;
                }
                break;
            case 59:return 0;
            case 32:
                c=c&0xffff00ff|nm<<8;//mou=nm&0xff
                if(((c&0x7f)==127)&&(map[c>>8&0x7f]>>14==(c>>31)+1)){//if((tag==127(|255))&&map[mou]t)
                    if(!(map[c>>8&0x7f]&0x3e0))c&=0xffff7fff;//if(map[mouse].up空)mouseUp=0
                    reset();
                    unsigned char t=c>>31,s=c>>8&0x7f;//t=c.t,s=mouse
                    switch(map[c>>8&0x7f]>>(c&0x8000?5:0)&0x1f){
                        char i,j;
                        case 16:
                            for(i=s-9;i>=0;i-=9){
                                //printf("%d\n",i);
                                if(map[i]>>14==(t?1:2)){//敵人
                                    if(foot_turtle(i,s)){c=c&0xc07fffff|i<<23;}//zu
                                    break;
                            }   }
                            for(i=s+9;i<81;i+=9){
                                if(map[i]>>14==(t?1:2)){
                                    if(foot_turtle(i,s)){c=c&0xff80ffff|i<<16;}//zd
                                    break;
                            }   }//沒錯case 16後面接著判八格
                        case 1:case 13:case 14:case 15:
                            move(s-1,s,3);move(s+1,s,4);
                        case 2:
                            move(s-10,s,0);move(s-9,s,1);move(s-8,s,2);
                            move(s+8,s,5);move(s+9,s,6);move(s+10,s,7);break;//前面的到這裡一起break
                        case 3:
                            move(s-10,s,0);move(s-8,s,2);move(s-1,s,3);
                            move(s+1,s,4);move(s+8,s,5);move(s+10,s,7);break;
                        case 4:case 10:
                            t?move(s+9,s,6):move(s-9,s,1);break;
                        case 5:
                            move(s-9,s,1);move(s-1,s,3);move(s+1,s,4);move(s+9,s,6);break;
                        case 6:
                            if(t){
                                for(i=s,j=1;j&1;i+=10)j=move(i+10,i,7|j<<2&0x18);//所有loop mo都是先&在|
                                for(i=s,j=1;j&1;i+=9)j=move(i+9,i,6|j<<2&0x18);
                                for(i=s,j=1;j&1;i+=8)j=move(i+8,i,5|j<<2&0x18);
                                break;
                            }
                            for(i=s,j=1;j&1;i-=8)j=move(i-8,i,2|j<<2&0x18);
                            for(i=s,j=1;j&1;i-=9)j=move(i-9,i,1|j<<2&0x18);
                            for(i=s,j=1;j&1;i-=10)j=move(i-10,i,0|j<<2&0x18);
                            break;
                        case 7:
                            if(t){
                                for(i=s+10,j=move(s+10,s,7);j&1;i+=9)j=move(i+9,i,7|j<<2&0x18);
                                for(i=s+8,j=move(s+8,s,5);j&1;i+=9)j=move(i+9,i,5|j<<2&0x18);
                                break;
                            }
                            for(i=s-8,j=move(s-8,s,2);j&1;i-=9)j=move(i-9,i,2|j<<2&0x18);
                            for(i=s-10,j=move(s-10,s,0);j&1;i-=9)j=move(i-9,i,0|j<<2&0x18);
                            break;
                        case 8:
                            move(s-9,s,1);
                            move(s+9,s,6);
                            for(i=s,j=1;j&1;--i)j=move(i-1,i,3|j<<2&0x18);
                            for(i=s,j=1;j&1;++i)j=move(i+1,i,4|j<<2&0x18);
                            break;
                        case 9:case 18:{//這括號不加不能宣告ap,p 編譯器全責
                            unsigned char ap,p=map[s]&0x3e0&&~c&0x8000;//will p
                            for(i=s-9,j=1;i>=0;i-=9){
                                ap=is_apple(i+9,i);
                                if(ap^8){j=p?7:5;eat_the_apple[1]|=1<<ap;}
                                if(map[i]){i-=9;break;}
                            }
                            for(;i>=0;i-=9)j=move(i,i+9,1|j<<2&0x18);
                            for(i=s-1,j=1;(i+1)%9;--i){
                                ap=is_apple(i+1,i);
                                if(ap^8){j=p?7:5;eat_the_apple[3]|=1<<ap;}
                                if(map[i]){--i;break;}
                            }
                            for(;(i+1)%9;--i)j=move(i,i+1,3|j<<2&0x18);
                            for(i=s+1,j=1;i%9;++i){
                                ap=is_apple(i-1,i);
                                if(ap^8){j=p?7:5;eat_the_apple[4]|=1<<ap;}
                                if(map[i]){++i;break;}
                            }
                            for(;i%9;++i)j=move(i,i-1,4|j<<2&0x18);
                            for(i=s+9,j=1;i<81;i+=9){
                                ap=is_apple(i-9,i);
                                if(ap^8){j=p?7:5;eat_the_apple[6]|=1<<ap;}
                                if(map[i]){i+=9;break;}
                            }
                            for(;i<81;i+=9)j=move(i,i-9,6|j<<2&0x18);
                            break;
                        }
                        case 17:for(i=0;i^81;++i)if(map[i]>>14==t+1&&s^i)map[i]|=0x1000;break;
                        case 19:
                            for(i=s,j=1;j&1;i-=9)j=move(i-9,i,1|j<<2&0x18);
                            for(i=s,j=1;j&1;--i)j=move(i-1,i,3|j<<2&0x18);
                            for(i=s,j=1;j&1;++i)j=move(i+1,i,4|j<<2&0x18);
                            for(i=s,j=1;j&1;i+=9)j=move(i+9,i,6|j<<2&0x18);
                    }
                    c=c^(c&0xff)|(c>>8&0xff);//tag(Up)=mouse(Up)
                    co();
                }
                else{
                    if((c>>8&0x7f^127&&(((c>>8&0x7f)==(c>>23&0x7f))||((c>>8&0x7f)==(c>>16&0x7f)))) && (c&0x8000||!(map[c>>8&0x7f]&0x3c00))){//if((mou!=127&&((mou==zu)||(mou==zd))) && (mouUp||!map[mou]mepe))
                        shoot_poison();reset();c^=0x80000000;
                        if(!(howmany_kmdl(c>>31)&&howmany_kmdl(~c>>31)))end=0;
                        c=c&0xffffff00|0x7f;nco();
                    }
                    else if(map[c>>8&0x7f]&0x3c00){//if(c[])second_set();
                        second_set();reset();c^=0x80000000;
                        if(!(howmany_kmdl(c>>31)&&howmany_kmdl(~c>>31)))end=0;c=c&0xffff0000|0x7f7f;nco();
                    }
                    else{reset();c=c&0xffff0000|0x7f7f;nco();}
    }   }       }
    nco();
    if(!howmany_kmdl(c>>31)&&!howmany_kmdl(~c>>31))printf("\ndraw...?");
    else if(c>>31)printf("\nthe first player win");
    else printf("\nthe second player win");
    /*scanf("%c");*/getchar();return 0;
}
