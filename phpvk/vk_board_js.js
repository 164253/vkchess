//2022/5/4
let gid=i=>document.getElementById(i);
let crE=i=>document.createElement(i);
let int=i=>parseInt(i);
let bdone=int(Math.min(window.innerWidth,window.innerHeight)/13*0.9);
let dist_wd=int((window.innerWidth-bdone*9)/2),dist_hi=int((window.innerHeight-bdone*9)/2);
let ischange=false;
let noquit=true;
let dir=".\\image\\";
let mp;
let bdcli=(x,y)=>{
    if(-1.5*bdone+dist_wd<x&&x<-0.5*bdone+dist_wd&&6.5*bdone+dist_hi<y&&y<7.5*bdone+dist_hi)ischange=!ischange;
    else{
        if(mp[81]&1){
            if(mp[81]&4){
                if(mp[81]&8^ischange){
                    x=int(x-dist_wd+0.5*bdone);
                    y=int(y-dist_hi+1.5*bdone);
                    if(0<x&&x<10*bdone&&0<y&&y<bdone)mp=cvkdlljs(10-int(x/bdone));
                }
                else{
                    x=int(x-dist_wd+0.5*bdone);
                    y=int(y-dist_hi-9.5*bdone);
                    if(0<x&&x<10*bdone&&0<y&&y<bdone)mp=cvkdlljs(1+int(x/bdone));
                }
                if(~mp[81]&4)for(let i=1;i^11;++i){gid(`bs${i}`).style.display="none";gid(`bf${i}`).style.display="none";gid(`bgks${i}`).style.display="none";gid(`bgkf${i}`).style.display="none";}
            }
            else{
                x-=dist_wd;
                y-=dist_hi;
                if(x>=0&&x<bdone*9&&y>=0&&y<bdone*9){
                    nm=int(x/bdone)+int(y/bdone)*9;
                    if(y%bdone<bdone/2)nm|=0x80;
                    if(mp[81]&16)nm^=0x80;
                    if(ischange){
                        nm=80-(nm&0x7f);
                        nm^=0x80;
                    }
                    mp[83]=nm;
                    mp=cvkdlljs(mp.join()).split(",");
                }
            }
            if(mp[81]&4){
                if(m[81]&8^ischange)for(let i=10;i;--i){gid(`bs${i}`).style.display="block";gid(`bgks${i}`).style.display="block";}
                else for(let i=10;i;--i){gid(`bf${i}`).style.display="block";gid(`bgkf${i}`).style.display="block";}
            }
        }
    }
    output();
}
let boardInit=(mp)=>{
    mp=mp.split(",");
    gid("spImg").style=`top:${dist_hi-bdone*1.5}px; left:${dist_wd-bdone*1.5}px; width:${bdone}px;`;
    gid("spImg").src=dir+"vkImage1_2.png";//wait4sql
    gid("spP").style=`top:${dist_hi-bdone*0.5}px; left:${dist_wd-bdone*1.5}px; margin:0px;`;
    gid("fpImg").style=`top:${dist_hi+bdone*9.5}px; left:${dist_wd+bdone*9.5}px; width:${bdone}px;`;
    gid("fpImg").src=dir+"vkImage1_1.png";//wait4sql
    gid("fpP").style=`top:${dist_hi+bdone*10.5}px; right:${dist_wd-bdone*1.8}px; margin:0px;`;//why1.8?idk too.i just try.
    gid("quickc").style=`top:${dist_hi}px; left:${dist_wd}px; width:${bdone*9}px;`;
    gid("quickc").src=dir+"boardline.png";
    let bd=document.body,p=0;
    for(let i=0;i<9;++i){
    	for(let j=0;j<9;++j){
    	    let m=crE("img"),mu=crE("img"),c=crE("img");
            m.id=`m${p}`;
            mu.id=`mu${p}`;
			c.id=`c${p}`;
            m.setAttribute("draggable","false");
            mu.setAttribute("draggable","false");
            c.setAttribute("draggable","false");
            m.setAttribute("class","pa");
            mu.setAttribute("class","pa");
			c.setAttribute("class","pa");
            m.style=`top:${dist_hi+bdone*i}px; left:${dist_wd+bdone*j}px; width:${bdone}px; z-index:3;`;
            mu.style=`top:${dist_hi+bdone*i}px; left:${dist_wd+bdone*(j+0.5)}px; width:${bdone}px; z-index:3; display:none;`;
			c.style=`top:${dist_hi+bdone*i}px; left:${dist_wd+bdone*j}px; width:${bdone}px; z-index:2;`;
        	bd.appendChild(m);
        	bd.appendChild(mu);
			bd.appendChild(c);
            ++p;
        }
        bd.appendChild(crE("br"));
    }
    for(let i=10;i;--i){
        let bf=crE("img"),bs=crE("img");
        bf.id=`bf${i}`;
        bs.id=`bs${i}`;
        bf.setAttribute("draggable","false");
        bs.setAttribute("draggable","false");
        bf.setAttribute("class","pa");
        bs.setAttribute("class","pa");
        bf.src=dir+`vkImage${i}_1.png`;
        bs.src=dir+`vkImage${i}_2.png`;
        bf.style=`top:${dist_hi+bdone*9.5}px; left:${dist_wd+bdone*(i-1.5)}px; width:${bdone}px; z-index:3; display:none;`;
        bs.style=`top:${dist_hi-bdone*1.5}px; left:${dist_wd+bdone*(9.5-i)}px; width:${bdone}px; z-index:3; display:none;`;
        bd.appendChild(bf);
        bd.appendChild(bs);
        let bgkf=crE("img"),bgks=crE("img");
        bgkf.id=`bgkf${i}`;
        bgks.id=`bgks${i}`;
        bgkf.setAttribute("draggable","false");
        bgks.setAttribute("draggable","false");
        bgkf.setAttribute("class","pa");
        bgks.setAttribute("class","pa");
        bgkf.src=dir+"vkImage0_0_0.png";
        bgks.src=dir+"vkImage0_0_0.png";
        bgkf.style=`top:${dist_hi+bdone*9.5}px; left:${dist_wd+bdone*(i-1.5)}px; width:${bdone}px; z-index:2; display:none;`;
        bgks.style=`top:${dist_hi-bdone*1.5}px; left:${dist_wd+bdone*(9.5-i)}px; width:${bdone}px; z-index:2; display:none;`;
        bd.appendChild(bgkf);
        bd.appendChild(bgks);
    }
    let l,xl=[1,9,25,33],i;
    for(i=0;i^4;++i){
        l=crE("img");
        l.id=`l${i}`;
        l.setAttribute("class","pa");
        l.setAttribute("draggable","false");
        l.src=dir+"vkImage-1_2.png";
        l.style=`top:${dist_hi+bdone*15/4}px; left:${dist_wd+bdone*xl[i] /4}px; width:${bdone/2}px; z-index:4;`;
        bd.appendChild(l);
    }
    for(++i;i^8;++i){
        l=crE("img");
        l.id=`l${i}`;
        l.setAttribute("class","pa");
        l.setAttribute("draggable","false");
        l.src=dir+"vkImage-1_1.png";
        l.style=`top:${dist_hi+bdone*19/4}px; left:${dist_wd+bdone*xl[i-4] /4}px; width:${bdone/2}px; z-index:4;`;
        bd.appendChild(l);
    }
    output();
}
let output=()=>{
    if(mp[81]&2){
        gid("quickc").style.display="none";
        for(p=0;p^81;++p){gid(`c${p}`).src=dir+`vkImage${mp[p]>>>12&3}_${mp[p]>>>11&1}_${mp[p]>>>10&1}.png`;gid(`c${p}`).style.display="block";}
        let z=mp[82]>>>7&127;
        if(z^127)gid(`c${z}`).src=`vkImagep${(mp[z]>>>13&1)+(mp[z]>>>11&1)}.png`;
        z=mp[82]&127;
        if(z^127)gid(`c${z}`).src=`vkImagep${(mp[z]>>>13&1)+(mp[z]>>>11&1)}.png`;
    }
    else{gid("quickc").style.display="block";for(p=0;p^81;++p)gid(`c${p}`).style.display="none";}
    for(let p=0;p^81;++p){
        if(mp[p]&0x3e0){
            gid(`m${mp[p]>>>15?'':'u'}${p}`).style=`top:${dist_hi+bdone*int(p/9)}px; left:${dist_wd+bdone*(p%9+0.25)}px; width:${bdone/2}px; z-index:3; display:block;`;
            gid(`mu${p}`).src=dir+`vkImage${mp[p]>>>5&0x1f}_${mp[p]>>>14&3}.png`;
            gid(`m${mp[p]>>>15?'u':''}${p}`).style=`top:${dist_hi+bdone*(int(p/9)+0.5)}px; left:${dist_wd+bdone*(p%9+0.25)}px; width:${bdone/2}px; z-index:3;`;
            gid(`mu${p}`).style.display="block";
        }
        else{
            gid(`mu${p}`).style.display="none";
            gid(`m${p}`).style=`top:${dist_hi+bdone*int(p/9)}px; left:${dist_wd+bdone*(p%9)}px; width:${bdone}px; z-index:3;`;
        }
        gid(`m${p}`).src=dir+`vkImage${mp[p]&0x1f}_${mp[p]>>>14&3}.png`;
    }
    let l=mp[81]>>>5&0xff,i;
    for(i=0;i^4;++i)gid(`l${i}`).style.display=l&1<<i?"block":"none";
    for(++i;i^8;++i)gid(`l${i}`).style.display=l&1<<i?"block":"none";
    if(!(mp[81]&1)){
        let win=crE("img"),lose=crE("img");
        win.id="win";
        lose.id="lose";
        win.src=dir+"win.png";
        lose.src=dir+"lose.png";
        win.setAttribute("draggable","false");
        lose.setAttribute("draggable","false");
        win.setAttribute("class","pa");
        lose.setAttribute("class","pa");
        win.style=`top:${dist_hi+bdone*(mp[81]&16?9.5:-1.5)}px; left:${dist_wd+bdone*3}px; width:${bdone*3}px; z-index:4;`;
        lose.style=`top:${dist_hi+bdone*(mp[81]&16?-1.5:9.5)}px; left:${dist_wd+bdone*3}px; width:${bdone*3}px; z-index:4;`;
        document.body.appendChild(win);
        document.body.appendChild(lose);
    }
}