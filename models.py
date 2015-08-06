from session import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Post', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50))
    posts = db.relationship('Post', secondary='tag_post_link')


45
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    content = db.Column(db.Text)
    tags = db.relationship(Tag, secondary='tag_post_link')

    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content


class TagPostLink(db.Model):
    __tablename__ = 'tag_post_link'
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    tag = db.relationship(Tag, backref=db.backref('post_assoc'))
    post = db.relationship(Post, backref=db.backref('post_assoc'))

# AI = models.Tag.query.filter_by(label='AI').all()
# for tag in tags:
#    for post in tag.posts
#        print post.content
