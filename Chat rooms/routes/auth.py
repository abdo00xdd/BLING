from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        if nickname:
            session['user'] = nickname
            flash(f"Bienvenue, {nickname} !", 'success')
            return redirect(url_for('rooms.index'))
        else:
            flash("Veuillez entrer un nickname.", 'error')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Vous avez été déconnecté.", 'success')
    return redirect(url_for('auth.login'))