<?php
session_start();
$_SESSION['board']=[
0x8007,0x8005,0x8004,0x8003,0x8001,0x8002,0x8004,0x8005,0x8006,
    0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
    0,     0,     0,     0,     0,     0,     0,     0,     0,
    0,     0,     0,     0,     0,     0,     0,     0,     0,
    0,     0,     0,     0,     0,     0,     0,     0,     0,
0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
    0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
0x4006,0x4005,0x4004,0x4002,0x4001,0x4003,0x4004,0x4005,0x4007,0,0x3fff];
$_SESSION['c']=0x3fff7f7f;$_SESSION['l']=0xef;$_SESSION['eta']=[0,0,0,0,0,0,0,0];
?>
<html style="height:100%;">
    <head>
        <meta charset="utf-8">
        <script src="vk_board_js.js"></script>
        <style>.pa{position:absolute;user-select:none;}</style>
    </head>
    <body class="pa" draggable="false" style="width:98%; height:98%;" onclick="bdcli(event.pageX,event.pageY)">
        <img id="spImg" draggable="false" class="pa">
        <p id="spP" class="pa">後手 未讀取到名字</p>
        <img id="fpImg" draggable="false" class="pa">
        <p id="fpP" class="pa">先手 未讀取到名字</p>
        <img id="quickc" draggable="false" class="pa">
        <script>boardInit();</script>
    </body>
</html>