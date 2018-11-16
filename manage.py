from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Comment,Pitch


app = create_app("development")

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(db = db, app = app, User = User, Pitch = Pitch, )