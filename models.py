from session import db

class User(db.Model):
    __fillable__ = ['username', 'password']

    @property
    def posts(self):
        return self.has_many('posts')

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __fillable__ = ['title', 'content']

    @property
    def user(self):
        return self.belongs_to('users')
