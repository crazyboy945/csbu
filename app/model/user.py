from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app, request, url_for
from app.exceptions import ValidationError
from app import db, login_manager


class User(UserMixin,db.Model):
    __tablename__='users'

    userid=db.Column("userid",db.Integer,primary_key=True)
    username=db.Column("username",db.String(40),unique=True)
    password=db.Column("password",db.String(128))
    email=db.Column("email",db.String(120),unique=True)
    employeeid=db.Column("employeeid",db.Integer)
    last_login=db.Column("last_login",db.DateTime(),default=datetime.utcnow())


    @property
    def id(self):
        return self.userid


    def ping(self):
        self.last_login = datetime.utcnow()
        db.session.add(self)
    
    def __repr__(self):
        return "User ID is :%d,User Name is :%s" %(self.userid,self.username)

    def __init__(self,username,password,email):
        self.username=username
        self.password=generate_password_hash(password)
        self.email=email
        self.last_login=datetime.utcnow()

    def change_password(self,old_password,new_password):
        if check_password_hash(self.password,old_password):
            self.password=generate_password_hash(new_password)
            db.session.add(self)
            return True
        else:
            return False

    def change_email(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        return True

    def to_json(self):
        return {
            "userid":self.userid,
            "username":self.username,
            "email":self.email,
            "employeeid":self.employeeid,
            "last_login":self.last_login

        }


    def verify_password(self,password):
        return check_password_hash(self.password,password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))