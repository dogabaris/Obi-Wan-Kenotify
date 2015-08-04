from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from session import app, db, basedir

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
