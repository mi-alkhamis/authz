from authz.authz import db
from authz.util import uuidgen,now,user_expires_at
from authz.config import Config

class User(db.Model):
    id = db.Column(db.String(64),primary_key=True, default=uuidgen)
    username = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(256),nullable=False)
    role = db.Column(db.String(32),index=True,nullable=False,default=Config.USER_DEFAULT_ROLE)
    created_at = db.Column(db.DateTime,nullable=False,default=now)
    expires_at = db.Column(db.DateTime,nullable=False,default=user_expires_at)
    last_login_at = db.Column(db.DateTime,default=None)
    last_active_at = db.Column(db.DateTime,default=None)
    failed_auth_at = db.Column(db.DateTime,default=None)
    failed_auth_count = db.Column(db.Integer, nullable=False,default=0)
    status = db.Column(db.Integer,nullable=False,default=Config.USER_DEFAULT_STATUS)
    
    def __repr__(self):
        return f"<user username={self.username}, role={self.role}, created at={self.created_at}"