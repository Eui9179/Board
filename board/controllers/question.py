from board.models.answer import Answer
from flask import Blueprint,render_template,request,make_response,redirect

from datetime import datetime

from flask.helpers import url_for
from board.models.question import Question
from board import db

from board.forms import QuestionForm, AnswerForm

q_bp = Blueprint('question',__name__,url_prefix='/question')

@q_bp.route('/list')
def list():
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html',
                            question_list=question_list)

@q_bp.route('/detail/<int:question_id>')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html',
                            question=question,form=form)
                    

@q_bp.route('/create', methods=['GET','POST'])
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(
            subject = form.subject.data,
            content = form.content.data,
            create_date = datetime.now()
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html',form=form)


@q_bp.route('/del/<int:question_id>')
def delete(question_id):
    q = Question.query.get(question_id)
    db.session.delete(q)
    db.session.commit()

    return make_response("seccess",200)
