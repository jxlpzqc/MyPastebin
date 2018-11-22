from flask import *
from flask_sqlalchemy import SQLAlchemy
from time import time,sleep
import threading
import random,hashlib,cgi,datetime

#数据库配置
SQL_USERNAME = 'root'
SQL_PASSWORD = '6666'
SQL_HOSTADDRESS = 'localhost'
SQL_HOSTPORT = '3306'
SQL_DATABASE = 'pastebin'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + SQL_USERNAME + ':' + SQL_PASSWORD + '@' + SQL_HOSTADDRESS + ':' + SQL_HOSTPORT + '/' + SQL_DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#下面是ORM模型
class Message(db.Model):
	__tablename__ = 'messages'
	id = db.Column(db.String(50), primary_key=True)
	poster = db.Column(db.String(50))
	syntax = db.Column(db.Integer)
	type = db.Column(db.Integer)
	content = db.Column(db.Text)
	expiration = db.Column(db.DateTime)
	password = db.Column(db.String(50),nullable=True)

	def __init__(self,id,poster,syntax,content,expiration,type=0,password=None):
		self.id = id
		self.poster = poster
		self.syntax = syntax
		self.content = content
		self.expiration = expiration
		self.type = type
		self.password = password
		
#工具函数
def reprocess_html(content):
	#转义html字符
	content = cgi.escape(content)
	content = content.replace('\n','<br/>')
	content = content.replace(' ','&nbsp')
	content = content.replace('\t','&nbsp&nbsp&nbsp&nbsp')
	return content

	
#Syntax处理器部分
def process_pain(content):
	return content
	

#syntax 定义
syntaxs = { 1:{'text':'Pain Text', 'function':process_pain}, 2:{'text':'Python'} , 3:{'text':'C++'} }

#自动删除过期数据
def autodelete():
	time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	sql = "delete from messages where expiration <'" + time + "'" 
	print("Cleanning at "+time)
	db.session.execute(sql)
	db.session.commit()
	sleep(60*60)
	autodelete()
	
def startauto():
	print("Auto Clean Service has benn launched")
	t = threading.Thread(target=autodelete)
	t.start()

#Controller部分
@app.route('/')
def index():
	return render_template('main.html',syntaxs=syntaxs)

@app.route('/p/<id>')
def show(id):
	message = Message.query.filter_by(id=id).first()
	if message == None:
		abort(404)
	print(message)
	return render_template('show.html',message=message)

	
@app.route('/new',methods = ['POST'])
def	newpaste():
	poster = request.form.get('poster')
	syntax = int(request.form.get('syntax'))
	expirationstr = request.form.get('expiration')
	now = datetime.datetime.now()
	if expirationstr=='day':
		exp = now + datetime.timedelta(days=1)
	elif expirationstr=='week':
		exp = now + datetime.timedelta(days=7)
	elif expirationstr=='month':
		exp = now + datetime.timedelta(days=30)
	elif expirationstr=='year':
		exp = now + datetime.timedelta(days=365)
	else:
		exp = now + datetime.timedelta(days=1)
	#expiration = "2018-11-23"
	expiration = exp.strftime("%Y-%m-%d %H:%M:%S")
	content = request.form.get('content')
	password = request.form.get('password')
	if content == '':
		return redirect(url_for('index'))
	if poster == '':
		poster = 'anonymous'
	#content = encode_html(content)
	content = reprocess_html(content)
	#使用处理器
	if 'function' in syntaxs[syntax].keys() and syntaxs[syntax]['function'] != None:
		content = syntaxs[syntax]['function'](content)
	
	
	#得到一个ID
	idsrc = poster+content+request.remote_addr+str(time())+str(random.uniform(0,100))
	md5 = hashlib.md5()
	md5.update(idsrc.encode('utf-8'))
	id = md5.hexdigest()
	new = Message(id,poster,syntax,content,expiration)
	db.session.add(new)
	db.session.commit()
	
	return redirect(url_for('show',id=id))


	
#启动函数
if __name__ == '__main__':
	#db.drop_all()
	#db.create_all()
	
	#startauto()
	app.run(debug='true')
	
	