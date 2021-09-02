from flask import Blueprint,render_template
from board.models.question import Question

q_bp = Blueprint('question',__name__,url_prefix='/question')

@q_bp.route('/list')
def list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',
                            question_list=question_list)

@q_bp.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html',
                            question=question)