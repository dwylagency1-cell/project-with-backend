from blueprint.app import db

class study(db.Model):
    __tablename__ = 'todo_for_students'

    pid = db.Column(db.Integer , primary_key= True)
    subject = db.Column(db.Text(100), nullable = False)
    topic = db.Column(db.Text(200), nullable = False)

    def __repr__(self):
        return f"subject: {self.subject}, topic: {self.topic}"