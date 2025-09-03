from flask import Blueprint, render_template, session

operatore_bp = Blueprint('operatore', __name__, url_prefix='/operatore')

@operatore_bp.route('/dashboard')
def dashboard():
    if 'username' not in session or session.get('role') != 'operatore':
        return redirect(url_for('auth.login'))
    return render_template('operatore.html', username=session['username'])
