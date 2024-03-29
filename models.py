from session import db

class User(db.Model):
    __fillable__ = ['username', 'password']
    __hidden__ = ['created_at', 'updated_at', 'password']

    @property
    def posts(self):
        return self.has_many('posts')

    @property
    def roles(self):
        return self.belongs_to_many('tags')

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __fillable__ = ['title', 'content', 'user_id', 'tag_id', 'published_at']
    __hidden__ = ['created_at', 'updated_at', 'user_id', 'tag_id']

    @property
    def user(self):
        return self.belongs_to('users')

    @property
    def tag(self):
        return self.belongs_to('tags')

    def test(self):
        return self.user.username

    def __repr__(self):
        return '<Post title %r>' % self.title


class Tag(db.Model):
    __fillable__ = ['name']
    __hidden__ = ['created_at', 'updated_at', 'pivot']

    @property
    def posts(self):
        return self.has_many('posts')

    @property
    def users(self):
        return self.belongs_to_many('users')
