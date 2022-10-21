//2022/10/16
let int=i=>parseInt(i);
let bdone=int(Math.min(window.innerWidth,window.innerHeight)/13*0.9);
let dist_wd=int((window.innerWidth-bdone*9)/2),dist_hi=int((window.innerHeight-bdone*9)/2);
let dir="./static/image/";
let m;
let born=()=>{
    for(let i=1;i^11;++i){
        $(`#bs${i}`).css("display","none");$(`#bsg${i}`).css("display","none");
        $(`#bf${i}`).css("display","none");$(`#bfg${i}`).css("display","none");
    }
    if(m[81]&4){
        if(m[81]>>3&1^ischange)for(let i=10;i;--i){$(`#bs${i}`).css("display","block");$(`#bsg${i}`).css("display","block");}
        else for(let i=10;i;--i){$(`#bf${i}`).css("display","block");$(`#bfg${i}`).css("display","block");}
    }
}
let socket = io.connect();
socket.on('return_click'+play_mode,r=>{
    m=r.split(',').map(Number);
    born();output();});
let change=()=>{
    $("#fpP").html([$("#spP").html(),$("#spP").html($("#fpP").html())][0]);
    $("#fpImg").attr("src",[$("#spImg").attr("src"),$("#spImg").attr("src",$("#fpImg").attr("src"))][0]);
    born();
};
let bdcli=(x,y)=>{
    if(-1.5*bdone+dist_wd<x&&x<-0.5*bdone+dist_wd&&6.5*bdone+dist_hi<y&&y<7.5*bdone+dist_hi){
        change();
        ischange=!ischange;
        output();
    }
    else{
        if(m[81]&1){
            if(m[81]&4){
                if(m[81]>>3&1^ischange){
                    x=int(x-dist_wd+0.5*bdone);
                    y=int(y-dist_hi+1.5*bdone);
                    if(0<x&&x<10*bdone&&0<y&&y<bdone)socket.emit('click'+play_mode,(10-int(x/bdone)).toString());
                }
                else{
                    x=int(x-dist_wd+0.5*bdone);
                    y=int(y-dist_hi-9.5*bdone);
                    if(0<x&&x<10*bdone&&0<y&&y<bdone)socket.emit('click'+play_mode,(1+int(x/bdone)).toString());
                }
            }
            else{
                x-=dist_wd;
                y-=dist_hi;
                if(x>=0&&x<bdone*9&&y>=0&&y<bdone*9){
                    nm=int(x/bdone)+int(y/bdone)*9;
                    if(y%bdone<bdone/2)nm|=0x80;
                    if(m[81]&16)nm^=0x80;
                    if(ischange){
                        nm=(nm&0x80)+80-(nm&0x7f);
                        nm^=0x80;
                    }
                    socket.emit('click'+play_mode,(nm).toString());
                }
            }
        }
    }
}
let boardInit=()=>{
    $("#spImg").css({"top":dist_hi-bdone*1.5,"left":dist_wd-bdone*1.5,"width":bdone});
    $("#spP").css({"top":dist_hi-bdone*0.5,"left":dist_wd-bdone*1.5,"margin":0});
    $("#fpImg").css({"top":dist_hi+bdone*9.5,"left":dist_wd+bdone*9.5,"width":bdone});
    $("#fpP").css({"top":dist_hi+bdone*10.5,"right":dist_wd-bdone*1.8,"margin":0});//why1.8?idk too.i just try.
    $("#quickc").css({"top":dist_hi,"left":dist_wd,"width":bdone*9});
    $("#changeImg").css({"top":dist_hi+bdone*6.5,"left":dist_wd-bdone*1.5,"width":bdone});
    $("#undoImg").css({"top":dist_hi+bdone*8,"left":dist_wd-bdone*1.5,"width":bdone});
    let i=9,j,p=80;
    for(;i--;$(document.body).append("<br>")){
    	for(j=9;j--;--p){
            $(document.body).append(`<img id='m${p}' class='z3' style='top:${dist_hi+bdone*i}px; left:${dist_wd+bdone*j}px; width:${bdone}px;'>`);
            $(document.body).append(`<img id='mu${p}' class='z3' style='top:${dist_hi+bdone*i}px; left:${dist_wd+bdone*(j+0.5)}px; width:${bdone}px;'>`);
            $(document.body).append(`<img id='c${p}' class='c z2' style='top:${dist_hi+bdone*i}px; left:${dist_wd+bdone*j}px; width:${bdone}px;'>`);
        }
    }
    for(i=11;--i;){
        $(document.body).append(`<img id='bf${i}' src='${dir}${i}1.png' class='b z3' style='top:${dist_hi+bdone*9.5}px; left:${dist_wd+bdone*(i-1.5)}px; width:${bdone}px;'>`);
        $(document.body).append(`<img id='bs${i}' src='${dir}${i}2.png' class='b z3' style='top:${dist_hi-bdone*1.5}px; left:${dist_wd+bdone*(9.5-i)}px; width:${bdone}px;'>`);
        $(document.body).append(`<img id='bfg${i}' src="${dir}c000.png" class='b z2' style='top:${dist_hi+bdone*9.5}px; left:${dist_wd+bdone*(i-1.5)}px; width:${bdone}px;'>`);
        $(document.body).append(`<img id='bsg${i}' src="${dir}c000.png" class='b z2' style='top:${dist_hi-bdone*1.5}px; left:${dist_wd+bdone*(9.5-i)}px; width:${bdone}px;'>`);
    }
    for(i=8;i--;)$(document.body).append(`<img id='l${i}' src='${dir}-1${int(1+i/4)}.png' class='z3' style='top:${dist_hi+bdone*(15/4+int(i/4))}px; left:${dist_wd+bdone*(12*(i&2)+((i&1)<<3)|1)/4}px; width:${bdone/2}px;'>`);
    $("#l4").css("display","none");
    $("img").attr("draggable","false");
    $("img").addClass("pa");
    socket.emit('click'+play_mode,"81");
}
let output=()=>{
    let p,i,k;
    if(m[81]&2){
        $("#quickc").css("display","none");
        for(i=81,p=80*!ischange,k=(ischange<<1)-1;i--;$(`#c${p}`).attr("src",dir+'c'+(m[i]>>>12&3)+(m[i]>>>11&1)+(m[i]>>>10&1)+".png"),p+=k)$(`#c${p}`).css("display","block");
        let z=m[82]>>>7&127;
        if(z^127)$(`#c${ischange?~z+81:z}`).attr("src",dir+'p'+((m[z]>>>13&1)+(m[z]>>>11&1))+".png");
        z=m[82]&127;
        if(z^127)$(`#c${ischange?~z+81:z}`).attr("src",dir+"p"+((m[z]>>>13&1)+(m[z]>>>11&1))+".png");
    }
    else for($("#quickc").css("display","block"),p=81;p--;)$(`#c${p}`).css("display","none");
    for(i=81,p=80*!ischange,k=(ischange<<1)-1;i--;$(`#m${p}`).attr("src",dir+(m[i]&0x1f)+(((m[i]>>>14&3)<<ischange)%3)+".png"),p+=k){
        if(m[i]&0x3e0){
            $(`#m${m[i]>>>15^ischange?'':'u'}${p}`).css({"top":dist_hi+bdone*int(p/9),"left":dist_wd+bdone*(p%9+0.25),"width":bdone/2,"display":"block"});
            $(`#mu${p}`).attr("src",dir+(m[i]>>>5&0x1f)+(((m[i]>>>14&3)<<ischange)%3)+".png");
            $(`#m${m[i]>>>15^ischange?'u':''}${p}`).css({"top":dist_hi+bdone*(int(p/9)+0.5),"left":dist_wd+bdone*(p%9+0.25),"width":bdone/2});
            $(`#mu${p}`).css("display","block");
        }
        else{
            $(`#mu${p}`).css("display","none");
            $(`#m${p}`).css({"top":dist_hi+bdone*int(p/9),"left":dist_wd+bdone*(p%9),"width":bdone});
        }
    }
    let l=m[81]>>>5&0xff;
    for(i=8;i--;)$(`#l${ischange?~i+8:i}`).css("display",l&1<<i?"block":"none");
    if(!(m[81]&1)){
        $(document.body).append(`<img id=${ischange?'lose':'win'} src='${dir+(ischange?'lose':'win')}.png' class='z3 pa' draggable='false' style='top:${dist_hi+bdone*(m[81]&16?9.5:-1.5)}px; left:${dist_wd+bdone*3}px; width:${bdone*3}px;'>`);
        $(document.body).append(`<img id=${ischange?'win':'lose'} src='${dir+(ischange?'win':'lose')}.png' class='z3 pa' draggable='false' style='top:${dist_hi+bdone*(m[81]&16?-1.5:9.5)}px; left:${dist_wd+bdone*3}px; width:${bdone*3}px;'>`);
    }
}
