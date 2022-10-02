//2022/9/9
let dir="static/"
let start_game_btn_onclick=()=>{
    $("#btn1").attr({"src":dir+"single_play.png","onclick":"window.location.href='play1';"});
    $("#btn2").attr({"src":dir+"multiple_play.png","onclick":"window.location.href='play2';"});
    $("#btn3").attr({"src":dir+"back.png","onclick":'start_game_btn_back_onclick()'});
}
let start_game_btn_back_onclick=()=>{
    $("#btn1").attr("src",dir+"home.png");
    $("#btn1").removeAttr("onclick");
    $("#btn2").attr("src",dir+"lotto.png");
    $("#btn2").removeAttr("onclick");
    $("#btn3").attr({"src":dir+"start_game.png","onclick":'start_game_btn_onclick()'});
}