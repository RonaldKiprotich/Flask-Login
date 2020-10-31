from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import User


@main.route('/')
def index():
    return render_template('index.html')