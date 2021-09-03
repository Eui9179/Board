from flask import render_template,request,make_response,redirect,url_for
from datetime import datetime

from board.models.question import Question
from board import db
from board.controllers import q_bp


@q_bp.route('/list')
def list():
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html',
                            question_list=question_list)

@q_bp.route('/detail/<int:question_id>',methods=['GET'])
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html',
                            question=question)
                    

@q_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        subject = request.form.get('subject')
        content = request.form.get('content')
        question = Question(
            subject = subject,
            content = content,
            create_date = datetime.now()
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html')


@q_bp.route('/del/<int:question_id>')
def delete(question_id):
    q = Question.query.get(question_id)
    db.session.delete(q)
    db.session.commit()

    return redirect(url_for('question.list'))
