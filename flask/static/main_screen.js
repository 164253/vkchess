//2022/9/9
let dir="static/"
let socket = io.connect();
let wait_play2_second,wait_play2_p_plus;
socket.on('redirect_play2',()=>{stop_wait_play2();window.location.herf='play2';})
let stop_wait_play2=()=>{
    socket.emit('stop_wait_play2');
    $("#wait_play2_div").css("display","none");
    clearInterval(wait_play2_p_plus);
}
let start_wait_play2=()=>{
    socket.emit('start_wait_play2');
    wait_play2_second=0;
    $("#wait_play2_div").css("display","block");
    wait_play2_p_plus=setInterval("++wait_play2_second;$('#wait_play2_p').html(`等待中 ${wait_play2_second}秒`);",1000);
}
let start_game_btn_onclick=()=>{
    $("#btn1").attr({"src":dir+"single_play.png","onclick":"window.location.href='play1';"});
    $("#btn2").attr({"src":dir+"multiple_play.png","onclick":"start_wait_play2()"});
    $("#btn3").attr({"src":dir+"back.png","onclick":'start_game_btn_back_onclick()'});
}
let start_game_btn_back_onclick=()=>{
    $("#btn1").attr("src",dir+"home.png");
    $("#btn1").removeAttr("onclick");
    $("#btn2").attr("src",dir+"lotto.png");
    $("#btn2").removeAttr("onclick");
    $("#btn3").attr({"src":dir+"start_game.png","onclick":'start_game_btn_onclick()'});
}