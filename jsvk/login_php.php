<!--2022/5/9-->
<!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.js"></script> -->
<!DOCTYPE html>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<html>
    <head>
        <meta charset="utf-8">
        <title>科摩多龍棋 登陸或註冊</title>
        <!-- <link rel="stylesheet" type="text/css" href="login_css.css"> -->
    </head>
    <body>
        <form action="login_php.php" method="post" name="form" id="form" style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-size:180%;">
            <img src="logo.png" style="position:absolute; transform:translate(-110%,-25%); width:150%;">
            用戶名:<?php echo $_POST["username"];?><br>
            密碼:<?php echo $_POST["password"];?>
            用戶名:<input type="text" name="username" id="username" style="position:absolute; left:105%; font-size:100%; width:300%;"><br>
            <!-- 電子郵件:<input type="text" name="email" id="email"><br> -->
            密碼&nbsp;&nbsp;&nbsp;&nbsp;:<input type="password" name="password" id="password" style="position:absolute; left:105%; font-size:100%; width:300%;"><br>
            <input type="submit" name="submit" value="送出" style="position:absolute; font-size:70%; right:-300%;">
            <!-- <input type="button" name="submit" value="送出" onclick="formcli()" style="position:absolute; font-size:70%; right:-300%;"> -->
        </form>
    </body>
    <script src="login_js.js"></script>
</html>
