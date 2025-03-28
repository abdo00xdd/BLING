from flask import Flask
from routes.auth import auth_bp
from routes.rooms import rooms_bp

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'

# Enregistrement des Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(rooms_bp)

if __name__ == '__main__':
    app.run(debug=True)