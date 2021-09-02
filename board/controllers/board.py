from flask import Blueprint, jsonify
from board import db
from board.models.question import Question
from board.models.answer import Answer

from datetime import datetime

bp = Blueprint('main',__name__)

@bp.route('/post')
def create_post():
    q = Question(subject = "Test", content = "test", create_date = datetime.now())
    db.session.add(q)
    db.session.commit()

    return jsonify({
        "q_id":q.content
    })

@bp.route('/answer')
def create_answer():
    q = Question.query.get(1)
    a = Answer(question=q, content = 'yes',create_date=datetime.now())
    db.session.add(a)
    db.session.commit()

    return jsonify({
        "a":a.content
    })

@bp.route('/delete')
def delete():
    q = Question.query.get(2)
    db.session.delete(q)
    db.session.commit()

    return jsonify({
        "result":"success"
    })