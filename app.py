from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ruolo = request.form.get('ruolo')
        session['ruolo'] = ruolo
        if ruolo == 'operatore':
            return redirect(url_for('dashboard_operatore'))
        elif ruolo == 'ufficio':
            return redirect(url_for('dashboard_ufficio'))
    return render_template('login.html')

@app.route('/operatore')
def dashboard_operatore():
    if session.get('ruolo') != 'operatore':
        return redirect(url_for('login'))
    return render_template('operatore.html')

@app.route('/ufficio')
def dashboard_ufficio():
    if session.get('ruolo') != 'ufficio':
        return redirect(url_for('login'))
    return render_template('ufficio.html')

if __name__ == '__main__':
    app.run(debug=True)
