from flask import Blueprint

q_bp = Blueprint('question',__name__,url_prefix='/question')
a_bp = Blueprint('answer',__name__,url_prefix='/answer')

API_CATEGORY = "Board"

from board.controllers.question import *
from board.controllers.answer import *