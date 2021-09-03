from board import db

class Question(db.Model):
    __tablename__ = "question"
    __table_args__ = {"mysql_collate":"utf8_bin"}
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)