# app/main.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# IMPORTANTE: Importar os modelos para poder buscar no banco
from .models import User, Service 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Busca todos os usuários que têm a role 'provider' (prestadores)
    providers = User.query.filter_by(role='provider').all()
    
    # Passa a variável 'providers' para dentro do HTML
    return render_template('index.html', providers=providers)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')