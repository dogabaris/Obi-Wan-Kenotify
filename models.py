from session import db

class User(db.Model):
    __fillable__ = ['username', 'password']

    @property
    def posts(self):
        return self.has_many('posts')

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __fillable__ = ['title', 'content', 'user_id', 'tag_id', 'published_at']

    @property
    def user(self):
        return self.belongs_to('users')

    @property
    def tag(self):
        return self.belongs_to('tags')

    def __repr__(self):
        return '<Post title %r>' % self.title


class Tag(db.Model):
    __fillable__ = ['name']

    @property
    def posts(self):
        return self.has_many('posts')
