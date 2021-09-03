from flask import Blueprint, render_template, redirect,request,url_for

from board.models.answer import Answer
from board.models.question import Question
from board import db
from board.forms import AnswerForm
from datetime import datetime


a_bp = Blueprint('answer',__name__,url_prefix='/answer')

@a_bp.route('/create/<int:question_id>',methods=['POST'])
def create(question_id):
    question = Question.query.get(question_id)
    form = AnswerForm()
    if form.validate_on_submit():
        content = request.form.get('content')
        answer = Answer(question = question,content=content,create_date=datetime.now())
        db.session.add(answer)
        db.session.commit()
        
        return redirect(url_for('question.detail',question_id=question_id))
    return render_template('question/question_detail.html',question=question,form=form)
