'''環境設定
需要pip安裝 Flask,Flask-SQLAlchemy
'''
import re
from flask import Flask,session,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from ctypes import CDLL,c_uint16,byref
from os.path import dirname
cdllclick=CDLL(dirname(__file__)+"/static/cvkso0.1.7.so").cdllclick
# cdllclick=CDLL(dirname(__file__)+"/static/cvkdll0.1.7.dll").cdllclick
app=Flask(__name__)
app.secret_key='AngaNganG'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'vk_user'
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    def __init__(self,name,password):
        self.user_name = name
        self.user_password = password
'''這等到棋譜再用
class Two_play_data(db.model):
    __tablename__='two_play_data'
    game_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    u1=db.Column(db.Integer,nullable=False)
    u2=db.Column(db.Integer,nullable=False)
    board=db.Colunn(db.String(83),nullable=False)
'''
class two_play_data:
    __slots__=("u1","u2","m","move")
    def __init__(self,id1):
        self.u1=id1
        self.u2=-1
        self.move=0
        self.m=[
        0x8007,0x8005,0x8004,0x8003,0x8001,0x8002,0x8004,0x8005,0x8006,
             0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
        0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
             0,     0,     0,     0,     0,     0,     0,     0,     0,
             0,     0,     0,     0,     0,     0,     0,     0,     0,
             0,     0,     0,     0,     0,     0,     0,     0,     0,
        0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
             0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
        0x4006,0x4005,0x4004,0x4002,0x4001,0x4003,0x4004,0x4005,0x4007,
        0x1de1,0x3fff,0x3fff,0x7f7f,0,0,0,0]
wait_two_playing=-1
two_playing=[two_play_data(-1)]#放一個佔位置 session['game_id']==0會變成刪除session
usable=[]

def start_game(u1):
    global two_playing,usable
    if not usable:
        two_playing.append(two_play_data(u1))
        return len(two_playing)-1
    index=usable.pop()
    two_playing[index]=two_play_data(u1)
    return index

def end_game(index):
    global two_playing,usable
    if index<len(two_playing):
        two_playing.pop(index)
        if index<len(two_playing):usable.append(index)
'''
@socketio.on('connect')
def connect():
    session['gaming']=-1

@socketio.on('disconnect')
def disconnect():
    if session['gaming']==2:
        end_game(session['game_id'])
        #emit(,to=str(session['game_id'])) #通知對方
        session['gaming']=-1
'''
@app.route('/')
def index():
    return redirect(url_for('main_screen' if session.get('login') else 'login'))

@app.route('/register',methods=['GET','POST'])
def register():
    game_clear()
    if request.method=='POST':
        username=request.values["username"]
        password=request.values["password"]
        str=""
        if not re.match("[a-zA-Z0-9]{6,20}",username):
            str+="用戶名僅能包含大小不拘英數且長度需在6~20.\n"
        if not re.match("[a-zA-Z0-9]{6,20}",password):
            str+="密碼僅能包含大小不拘英數且長度需在6~20."
        if str:
            return "<script>alert('"+str+"');window.location.href='"+url_for('register')+"';</script>"
        if db.session.query(User).filter_by(user_name=username).first():
            return "<script>alert('已有帳號');window.location.href='"+url_for('login')+"';</script>"
        db.session.add(User(username,password))
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('login'):return redirect(url_for('main_screen'))
    game_clear()
    if request.method=='POST':
        result=User.query.filter_by(user_name=request.values["username"]).first()
        if result and result.user_password==request.values["password"]:
            session["login"]=True
            session["user_id"]=result.user_id
            session["user_name"]=result.user_name
            return redirect('/main_screen')
        return "<script>alert('帳號或密碼錯誤');window.location.href='"+url_for('login')+"';</script>'"
    return render_template('login.html')

@app.route('/logout')
def logout():
    if session['gaming']==2:
        end_game(session['game_id'])
        #emit(,to=str(session['game_id'])) #通知對方
        session['gaming']=-1
    session.clear()
    return redirect(url_for('index'))

def game_clear():
    session['gaming']=-1
    session['two_waiting']=False
    if session.get('play_mode'):
        if session['play_mode']==2:
            if session.get('game_id'):end_game(session['game_id'])
            session['turn']=False
            session['game_id']=False
            session['move']=False
        session['play_mode']=False
        session['two_waiting']=False
    if session.get('board'):session['board']=False

@app.route('/main_screen')
def main_screen():
    if not session.get('login'):return redirect(url_for('login'))
    game_clear()
    return render_template('main_screen.html') if session.get('login') else redirect(url_for('logout'))
'''
@socketio.on('stop_wait_play2')
def stop_wait_play2():
    global wait_two_playing
    if not session.get('two_waiting'):
        wait_two_playing=-1
        end_game(session['game_id'])
        leave_room(str(session['game_id']))
        session['two_waiting']=False
'''
'''
@socketio.on('start_wait_play2')
def start_wait_play2():
    global wait_two_playing
    print("yes")
'''
@app.route('/play2')
def play2():
    global wait_two_playing,two_playing
    if not session.get('login'):return redirect(url_for('login'))
    if not session.get('two_waiting'):
        if wait_two_playing!=-1:
            session['game_id']=wait_two_playing
            wait_two_playing=-1
            two_playing[session['game_id']].u2=session['user_id']
            session['turn']=2
            session['play_mode']=2
            session['board']=two_playing[session['game_id']].m
            session['gaming']=2
            session['move']=0
            print("2a",two_playing[session['game_id']].u2,session['user_id'])
            return render_template('board2.html',u1=db.session.query(User).filter_by(user_id=two_playing[session['game_id']].u1).first().user_name,u2=session['user_name'],u1img="11.png",u2img="12.png",rev=1)
        else:
            print("start wait play2")
            session['game_id']=start_game(session['user_id'])
            wait_two_playing=session['game_id']
            session['two_waiting']=True
            print("2b")
            return render_template('wait2.html',wait_time=int(request.args.get('wait_time','0')),game_room=session['game_id'])
    # print(session['game_id'],two_playing[0])
    print(two_playing[session['game_id']].u2,session['user_id'])
    if session['game_id']>=len(two_playing):
        end_game(session['game_id'])
        session['game_id']=start_game(session['user_id'])
    if two_playing[session['game_id']].u2!=-1:
        session['two_waiting']=False
        session['turn']=1
        session['play_mode']=2
        session['board']=two_playing[session['game_id']].m
        session['gaming']=2
        session['move']=0
        print("2c")
        return render_template('board2.html',u1=db.session.query(User).filter_by(user_id=two_playing[session['game_id']].u2).first().user_name,u2=session['user_name'],u1img="12.png",u2img="11.png",rev=0)
    print("2d")
    return render_template('wait2.html',wait_time=int(request.args.get('wait_time','0')),game_room=session['game_id'])

@app.route('/play1')
def play1():
    session['gaming']=1
    if not session.get('login'):return redirect(url_for('login'))
    session['board']=[
    0x8007,0x8005,0x8004,0x8003,0x8001,0x8002,0x8004,0x8005,0x8006,
         0,0x8009,     0,     0,     0,     0,     0,0x8008,     0,
    0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,0x800a,
         0,     0,     0,     0,     0,     0,     0,     0,     0,
         0,     0,     0,     0,     0,     0,     0,     0,     0,
         0,     0,     0,     0,     0,     0,     0,     0,     0,
    0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,0x400a,
         0,0x4008,     0,     0,     0,     0,     0,0x4009,     0,
    0x4006,0x4005,0x4004,0x4002,0x4001,0x4003,0x4004,0x4005,0x4007,
    0x1de1,0x3fff,0x3fff,0x7f7f,0,0,0,0]
    return render_template('board1.html')

@app.route('/click1')
def click1():
    if int(request.values['nm'])&0x7f<81:
        # print(session['board'])
        m=(c_uint16*89)(*session['board'])
        cdllclick(byref(m),c_uint16(int(request.values['nm'])))
        session['board']=[m[i] for i in range(89)]
        # print(session['board'])
    return ",".join([str(x) for x in session['board']])

@app.route('/click2')
def click2():
    global two_playing
    #後手噴吃不能噴
    #同回輸 後死贏
    if two_playing[session['game_id']].move>session['move']:
        session['board']=two_playing[session['game_id']].m
        session['move']=two_playing[session['game_id']].move
    elif int(request.values['nm'])&0x7f<81 and (session['turn']-1==session['board'][81]>>4&1)^(session['board'][81]>>2&1):
        was_click=session['board'][81]&2
        m=(c_uint16*89)(*session['board'])
        cdllclick(byref(m),c_uint16(int(request.values['nm'])))
        if was_click^m[81]&2 or m[81]&0x2000:
            session['board']=[m[i] for i in range(89)]
            if m[81]&0x2000:
                two_playing[session['game_id']].m=session['board']
                two_playing[session['game_id']].move+=1
                session['move']+=1
    return ",".join([str(x) for x in session['board']])

@app.route('/reset_play2_aaaaang')
def reset_play2_aaaaang():
    global wait_two_playing
    wait_two_playing=-1
    game_clear()
    return "why u r here?"

if __name__=="__main__":
    app.run(debug=True)