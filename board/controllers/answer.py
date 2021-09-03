from flask import redirect,request,url_for,render_template
from board.models.answer import Answer
from board.models.question import Question
from board.controllers import a_bp
from board import db

from datetime import datetime



@a_bp.route('/create/<int:question_id>',methods=['POST'])
def create(question_id):
    if request.method == 'POST':
        content = request.form.get('content')
        question = Question.query.get(question_id)
        answer = Answer(question = question,content=content,create_date=datetime.now())
        db.session.add(answer)
        db.session.commit()
        
        return redirect(url_for('question.detail',question_id=question_id))