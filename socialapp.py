from app import create_app, cli


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    from app import db
    from app.models import User, Post, Notification, Message
    
    return {'db': db,
            'User': User,
            'Post': Post,
            'Message':Message,
            'Notification':Notification}