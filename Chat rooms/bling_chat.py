from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, static_folder='.', template_folder='.')
app.secret_key = 'votre_clé_secrète'  # Nécessaire pour utiliser les sessions

# Données simulées pour les salles de chat
rooms = [
    {"name": "Privé", "type": "Privé", "description": "Salle privée pour les membres VIP", "created_by": "Admin"},
    {"name": "Public", "type": "Public", "description": "Salle publique pour tout le monde", "created_by": "Admin"}
]

# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        if nickname:
            session['user'] = nickname  # Stocker le nickname dans la session
            flash(f"Bienvenue, {nickname} !", 'success')
            return redirect(url_for('index'))
        else:
            flash("Veuillez entrer un nickname.", 'error')
    return render_template('login.html')

# Route pour la déconnexion
@app.route('/logout')
def logout():
    session.pop('user', None)  # Supprimer le nickname de la session
    flash("Vous avez été déconnecté.", 'success')
    return redirect(url_for('index'))

# Route pour créer une salle
@app.route('/create_room', methods=['POST'])
def create_room():
    if 'user' not in session:
        flash("Vous devez être connecté pour créer une salle.", 'error')
        return redirect(url_for('login'))

    room_name = request.form.get('room_name')
    room_type = request.form.get('room_type')
    description = request.form.get('description')

    if not room_name or not room_type or not description:
        flash("Tous les champs sont obligatoires.", 'error')
    else:
        new_room = {
            "name": room_name,
            "type": room_type,
            "description": description,
            "created_by": session['user']  # Utiliser le nickname de l'utilisateur connecté
        }
        rooms.append(new_room)
        flash(f"La salle '{room_name}' a été créée avec succès.", 'success')

    return redirect(url_for('index'))

# Route pour la page principale
@app.route('/')
def index():
    return render_template('index.html', rooms=rooms, user=session.get('user'))

# Route pour la recherche
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filtered_rooms = [room for room in rooms if query in room['name'].lower() or query in room['description'].lower()]
    return render_template('index.html', rooms=filtered_rooms, user=session.get('user'))

# Route pour rejoindre une salle
@app.route('/join/<room_name>')
def join_room(room_name):
    room = next((room for room in rooms if room['name'] == room_name), None)
    if room:
        return f"Vous avez rejoint la salle {room_name}"
    else:
        flash(f"La salle '{room_name}' n'existe pas.", 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)