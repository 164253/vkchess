//5/4 0.1 from cvkdll0.1.5
//js化中
/*未完成*/
/*definition of structs and functions
struct sMap{b:2,me:2,p:1,e:1,up:5,down:5}m[83];
struct control{t:1,kmdlborn:1,zu:7,zd:7,mouse:8,tag:8}c;//kmdlborn用不到了,sad
r=reset  ml=move limit  ft=foot and turtle  pf=poisonfrog  ia=is apple  mo=move  we=which to eta  sd=switch dict  fs=first set  wh=whale  tp=to pen  sp=shot poison  bo=born  ar=apple range  ss=second set
(in many functions)w=where  s=self  u=up  d=down  th=there*/
/*註解略寫 //請使用ctrl+f自行搜尋
[t差] t=目的地差值
[wu] whereUp=where(兩高用.up,一高用.down)
[su] selfUp=self(兩高用.up,一高用.down)
[w鱷龜] if(w無鱷龜)=1; elif同直行=1; else 0;
*/
let m=[
0x8007,0x8005,0x8004,0x8003,0x8001,0x8002,0x8004,0x8005,0x8006,
     0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
     0,     0,     0,     0,     0,     0,     0,     0,     0,
0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
     0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
0x4006,0x4005,0x4004,0x4002,0x4001,0x4003,0x4004,0x4005,0x4007,0,0x3fff];
//m[81] dll return{0x2000 ismchange,l:8,&16 t(c>>>31),&8 t(when bo),&4 bo,&2 co,&1 keep game}
//m[82]{zu:7,zd:7}
let c=0x3fff7f7f,l=0xef,eta=[0,0,0,0,0,0,0,0];//c{t,kmdlborn,mouseUp,tagUp=0;其他=1;} l{[4]=0;其他=1;} eta清空
let r=()=>{//只有迴圈能壓的reset
    let i=8;while(i--)eta[i]=0;//eta清空
    i=81;while(i--)m[i]&=0xc3ff;c|=0x3fff0000;//m[i].c,zu,zd清空
}
let ml=(w,s)=>{//無規律只能窮舉
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
let ft=(w,s)=>{//s=mou(==ts)
    let wu=m[w]>>>(m[w]&0x3e0?5:0)&0x1f,su=m[s]>>>(m[s]&0x3e0?5:0)&0x1f;//[wu]
    if(su<4)return 1;//if(su==1||su==2||su==3)return 1;
    if(wu^13)return wu^15||!((w-s)%9);//if(w沒大腳怪)[w鱷龜]
    //w大腳怪
        if(su^13)return 0;return wu^15||!((w-s)%9);//if(s沒大腳怪)[w鱷龜]
}
let pf=(w,s)=>{
    let wu=m[w]>>>(m[w]&0x3e0?5:0)&0x1f;//[wu]
    if(wu^18)return 0;//w沒箭毒蛙
    //w箭毒蛙
        let su=m[s]>>>(m[s]&0x3e0?5:0)&0x1f;//[su]
        if(su^15)return su^13;//if(s無鱷龜)return if(s大腳怪)=1; else  0;
        return !((w-s)%9);//s鱷龜 if(同直行)=1; else=0;
}
let ia=(w,s)=>{
    if(s%9==w%9){//同直排
        switch(s>w?w:s){//switch偏上者
            case 27:return l&1<<0?0:8;
            case 29:return l&1<<1?1:8;
            case 33:return l&1<<2?2:8;
            case 35:return l&1<<3?3:8;
            case 38:return l&1<<5?5:8;
            case 42:return l&1<<6?6:8;
            case 44:return l&1<<7?7:8;
        }
    }
    return 8;//不同排,後面ap^8即此意
}
let mo=(w,s,epa)=>{//e=evolution p=ispoison a=whichEta//return &1keep &2p &4e
    let mou=c>>>8&0x7f;
    if(ml(w,s)){
        if(m[w]>>>14==(c>>>31?1:2)){//敵人//吃人無論如何都是return 0
            if(ft(w,mou)){
                let ap=ia(w,s);
                m[w]|=0x2000;//m[w].me=2
                if(epa&16||ap^8){//見ia()
                    m[w]|=0x400;//m[w].e=1
                    eta[epa&7]|=1<<ap;//eta[a]加入第ap個銅錢草
                    if(epa&8||~c&0x8000&&m[mou]&0x3e0){m[w]|=0x800;return 6;}//if(p||(!mouseUp&&m[s].up))m[w].p=1
                    return 4;
                }
            }
        }
        else if(!m[w]||!(m[w]&0x3e0)&&(c&0x8000||!(m[mou]&0x3e0))){//m[w]空||(m[w].up空&&(mouseUp||m[s].up空))
            let ap=ia(w,s);
            m[w]|=0x1000;//m[w].me=1
            if(epa&16||ap^8){
                m[w]|=0x400;
                eta[epa&7]|=1<<ap;
                if(epa&8||~c&0x8000&&m[mou]&0x3e0){
                    m[w]|=0x800;
                    return 6|!(m[w]&0x1f);
                }
                return 4|!(m[w]&0x1f);
            }
            return !(m[w]&0x1f);
        }
    }
    return 0;//所有沒return,要中斷迴圈都來這
}
let we=(d,t)=>{
    if(d^7)return t<0?t%10?t%9?t%8?3:2:1:0:t%10?t%9?t%8?4:5:6:7;
    if(c>>>31)return t%9^1?5:7;
    return t%9^-1?2:0;
}
let sd=d=>{
    let t=c>>>31,s=c>>>8&0x7f,i,j;//t=c.t,s=mouse
    switch(d){
        case 16:
            for(i=s-9;i>=0;i-=9){
                if(m[i]>>>14==(t?1:2)){//敵人
                    if(ft(i,s)){c=c&0xc07fffff|i<<23;m[82]=i<<7;}//zu
                    break;
                }
            }if(i<0)m[82]=0x3f80;
            for(i=s+9;i<81;i+=9){
                if(m[i]>>>14==(t?1:2)){
                    if(ft(i,s)){c=c&0xff80ffff|i<<16;m[82]|=i;}//zd
                    break;
                }
            }if(i>80)m[82]|=127;//沒錯case 16後面接著判八格
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
            let ap,p=m[s]&0x3e0&&~c&0x8000;//will p
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
        case 17:for(i=0;i^81;++i)if(m[i]>>>14==t+1&&s^i)m[i]|=0x1000;break;
        case 19:
            for(i=s,j=1;j&1;i-=9)j=mo(i-9,i,1|j<<2&0x18);
            for(i=s,j=1;j&1;--i)j=mo(i-1,i,3|j<<2&0x18);
            for(i=s,j=1;j&1;++i)j=mo(i+1,i,4|j<<2&0x18);
            for(i=s,j=1;j&1;i+=9)j=mo(i+9,i,6|j<<2&0x18);
    }
}
let fs=()=>{
    if(!(m[c>>>8&0x7f]&0x3e0))c&=0xffff7fff;//if(m[mouse].up空)mouseUp=0
    r();
    sd(m[c>>>8&0x7f]>>>(c&0x8000?5:0)&0x1f);//原理同[wu],[su]
    c=c^(c&0xff)|(c>>>8&0xff);//tag(Up)=mouse(Up)
}
let wh=t=>{//t=where只是省字用
    let movelist=[-10,-9,-8,-1,1,8,9,10];//八格遍歷,只能窮舉
    for(th,tu,i=0;i^8;++i){
        let th=t+movelist[i];
        tu=m[th]>>>((m[th]&0x3e0?5:0)&0x1f);
        if(ml(t,th)&&m[th]>>>14==(c>>>31?1:2)&&tu^13&&(tu^15||i==1||i==6)){
            if(tu==18)m[t]=0;//自己頭上必鯨魚
            m[th]=0;
        }
    }
}
let tp=()=>{
    let i=72,up,down;
    for(;i^81;++i){
        if(m[i]&0x8000){//b==2
            up=m[i]>>>5&0x1f,down=m[i]&0x1f;
            if(up&&(up==6||up==7||up==4||up==10))m[i]=m[i]&0xfc1f|0x260;//頭up只是拿來加速短路
            if(down==6||down==7||down==4||down==10)m[i]=m[i]&0xffe0|0x13;
        }
    }
    for(i=0;i^9;++i){
        if(m[i]&0x4000){//b==1
            up=m[i]>>>5&0x1f,down=m[i]&0x1f;
            if(up&&(up==6||up==7||up==4||up==10))m[i]=m[i]&0xfc1f|0x260;//頭up只是拿來加速短路
            if(down==6||down==7||down==4||down==10)m[i]=m[i]&0xffe0|0x13;
        }
    }
}
let hk=t=>{
    let i=0,n=0;
    while(i^81){
        if((m[i]&0x1f)==1&&(m[i]>>>14)-1==t)++n;
        if((m[i]&0x3e0)==32&&(m[i]>>>14)-1==t)++n;
        ++i;
    }
    return n;
}
let ar=(w,s)=>{
    if(w>s)w^=s^=w^=s;//w恆小
    return (w<=27&&s>=36)|(w<=29&&s>=38)<<1|(w<=33&&s>=42)<<2|(w<=35&&s>=44)<<3|(w<=38&&s>=47)<<5|(w<=42&&s>=51)<<6|(w<=44&&s>=53)<<7;
}
let ss=()=>{
    let w=c>>>8&0x7f,s=c&0x7f,tu=m[s]>>>(m[s]&0x3e0?5:0)&0x1f,td=m[s]>>>(c&0x80?5:0)&0x1f,t=c>>>31;
    if(tu==14||tu==5&&m[w]&0x400)wh(w);//if(tu鯨魚||(tu鯰魚&&m[w].e)whale
    if(td==17){//鬣蜥
        m[s]^=m[w]^=m[s]^=m[w];//換
        if(tu==14)wh(s);//wh
        tp();//to pen
    }
    else{
        if(m[w]&0x400)l^=eta[we(td,w-s)]&ar(w,s);//appleDel
        if(m[w]&0x2000){//吃
            if(pf(w,s))m[w]&=0x3fc0;//wb=wu=wd=0
            else{
                m[w]=(m[w]&0x3c00)|td|(t+1<<14);//wb=t+1,wd=td,wu=0
                if(m[s]&0x3e0
                &&~c&0x80)m[w]|=tu<<5;//if(tu&&!tagUp)wu=tu
            }
        }
        else if(m[w]>>>14)m[w]|=tu<<5;//if(wb)wu=tu
        else{
            m[w]|=td|(t+1<<14);//wd=td,wb=tb
            if(m[s]&0x3e0&&~c&0x80)m[w]|=tu<<5;//if(su&&!tagUp)wu=tu
        }
        if(m[w]&0x400&&tu^1&&tu^2&&tu^3&&tu<11)m[w]+=9;//if((m[w].e)&&(tu^1)&&(tu^2)&&(tu^3)&&未進化)m[w].down=tu+9;//進化
        m[s]&=0xfc1f;//su=0;
        if(~c&0x80)m[s]&=0x3fe0;//if(!tagUp)sd=sb=0;
        if(m[w]&0x800)m[w]&=0x3c00;//if(m[w].p)wu=wd=wb=0
        tp();
        if(tu==1&&m[w]&0x2400){//if(tu=1&&(m[w].me=2||m[w].e))
            if(t){if(!(m[4]&0x4000)&&!(m[4]&0x3e0))m[81]|=4|c>>>31<<3;}//if(後手)if(m[4].b!=1&&m[4].up空)born()
            else if(!(m[76]&0x8000)&&!(m[76]&0x3e0))m[81]|=4|c>>>31<<3;//else if(m[76].b!=2&&m[76].up空)born()
        }
    }
}
let sp=()=>{
    let w=c>>>8&0x7f,s=c&0x7f;
    if((m[s]>>>5&0x1f)==14)wh(w);
    c&=0xafffffff|((m[s]>>>5&0x1f)==1)<<30;
    if(pf(w,s))m[s]&=0x3c00;
    if(ft(w,s))m[w]&=0x3c00;
    if(c&0x40000000)m[81]|=4|c>>>31<<3;
    c&=0xafffffff;
}
let cvkdlljs=nm=>{
    if(m[81]&4){
        let home=m[81]&8?4:76;
        m[home]|=nm<<(m[home]?5:0)|(m[81]&8?0x8000:0x4000);
        m[81]&=0x1ff3;
        if(!hk(m[81]>>>3&1))m[81]&=0x1ffe;
        m[81]|=0x2000;
    }
    else{
        c=c&0xffff00ff|nm<<8;//mou=nm&0xff
        if(((c&0x7f)==127)&&(m[c>>>8&0x7f]>>>14==(c>>>31)+1)){fs();m[81]|=2;}//if((tag==127(|255))&&m[mou]t)fs();co();
        else{
            m[81]=m[81]&16|1;
            if((c>>>8&0x7f^127&&(((c>>>8&0x7f)==(c>>>23&0x7f))||((c>>>8&0x7f)==(c>>>16&0x7f)))) && (c&0x8000||!(m[c>>>8&0x7f]&0x3c00))){//if((mou!=127&&((mou==zu)||(mou==zd))) && (mouUp||!m[mou]mepe))
                sp();r();c^=0x80000000;m[81]^=16;
                if(!(hk(c>>>31)&&hk(~c>>>31)))m[81]=(m[81]&30)|(m[81]>>>2&&!hk(~c>>>31));
                c=c&0xffffff00|0x7f;m[81]|=0x2000;
            }
            else if(m[c>>>8&0x7f]&0x3c00){//if(c[])ss();
                ss();r();c^=0x80000000;m[81]^=16;
                if(!(hk(c>>>31)&&hk(~c>>>31)))m[81]=(m[81]&30)|(m[81]>>>2&&!hk(~c>>>31));
                c=c&0xffff0000|0x7f7f;m[81]|=0x2000;
            }
            else{r();c=c&0xffff0000|0x7f7f;}
            m[81]=m[81]&0x1f|l<<5;
        }
    }
    return m;
}
function dllexport(nm){return cvkdlljs(nm);}
// export {dllexport}