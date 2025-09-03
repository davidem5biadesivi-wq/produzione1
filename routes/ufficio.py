from flask import Blueprint, render_template, session

ufficio_bp = Blueprint('ufficio', __name__, url_prefix='/ufficio')

@ufficio_bp.route('/dashboard')
def dashboard():
    if 'username' not in session or session.get('role') != 'ufficio':
        return redirect(url_for('auth.login'))
    return render_template('ufficio.html', username=session['username'])
