from flask import *
from flask_sqlalchemy import SQLAlchemy
from time import time
import random,hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:6666@localhost:3306/pastebin'
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
		


syntaxs = [ {'id':1,'text':'pain text' },{'id':2,'text':'Python' } ]

@app.route('/')
def index():
	return render_template('main.html',syntaxs=syntaxs)

@app.route('/new',methods = ['POST'])
def	newpaste():
	poster = request.form.get('poster')
	syntax = int(request.form.get('syntax'))
	expiration2 = request.form.get('expiration')
	expiration = "2018-11-23"
	content = request.form.get('content')
	#得到一个ID
	idsrc = poster+content+request.remote_addr+str(time())+str(random.uniform(0,100))
	md5 = hashlib.md5()
	md5.update(idsrc.encode('utf-8'))
	id = md5.hexdigest()
	
	new = Message(id,poster,syntax,content,expiration)
	db.session.add(new)
	db.session.commit()
	
	return 	id
	
if __name__ == '__main__':
	#db.drop_all()
	#db.create_all()
	app.run(debug='true')
	
