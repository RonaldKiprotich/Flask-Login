from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors





from flask import Blueprint

auth = Blueprint('main',__name__)

from . import views,forms

