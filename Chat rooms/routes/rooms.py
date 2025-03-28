from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.room import rooms

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/')
def index():
    return render_template('index.html', rooms=rooms, user=session.get('user'))

@rooms_bp.route('/create_room', methods=['POST'])
def create_room():
    if 'user' not in session:
        flash("Vous devez être connecté pour créer une salle.", 'error')
        return redirect(url_for('auth.login'))

    room_name = request.form.get('room_name')
    room_type = request.form.get('room_type')
    description = request.form.get('description')
    room_code = request.form.get('room_code') if room_type == 'Privé' else None

    if not room_name or not room_type or not description:
        flash("Tous les champs sont obligatoires.", 'error')
    else:
        new_room = {
            "name": room_name,
            "type": room_type,
            "description": description,
            "created_by": session['user'],
            "code": room_code
        }
        rooms.append(new_room)
        flash(f"La salle '{room_name}' a été créée avec succès.", 'success')

    return redirect(url_for('rooms.index'))

@rooms_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filtered_rooms = [room for room in rooms if query in room['name'].lower() or query in room['description'].lower()]
    return render_template('index.html', rooms=filtered_rooms, user=session.get('user'))

@rooms_bp.route('/join/<room_name>', methods=['GET', 'POST'])
def join_room(room_name):
    room = next((room for room in rooms if room['name'] == room_name), None)
    if not room:
        flash(f"La salle '{room_name}' n'existe pas.", 'error')
        return redirect(url_for('rooms.index'))

    if room['type'] == 'Privé':
        if request.method == 'POST':
            entered_code = request.form.get('room_code')
            if entered_code == room['code']:
                return f"Vous avez rejoint la salle privée {room_name}"
            else:
                flash("Code incorrect. Veuillez réessayer.", 'error')
        return render_template('enter_code.html', room_name=room_name)
    else:
        return f"Vous avez rejoint la salle publique {room_name}"