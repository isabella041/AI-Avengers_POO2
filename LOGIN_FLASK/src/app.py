from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_input = request.form['username'].strip()
        password_input = request.form['password'].strip()

        user = User(0, username_input, password_input)
        logged_user = ModelUser.login(db, user)

        if logged_user is not None:
            login_user(logged_user)
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for('home'))
        else:
            flash("Nombre de usuario o contraseña incorrectos.", "danger")
            return render_template('auth/login.html')

    return render_template('auth/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname'].strip()
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not fullname or not username or not password:
            flash('Todos los campos son obligatorios.', 'warning')
            return render_template('auth/register.html')

        from werkzeug.security import generate_password_hash

        hashed_password = generate_password_hash(password)

        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('El nombre de usuario ya existe.', 'warning')
            return render_template('auth/register.html')

        try:
            cursor.execute(
                "INSERT INTO user (fullname, username, password) VALUES (%s, %s, %s)",
                (fullname, username, hashed_password)
            )
            db.connection.commit()
            flash('Usuario registrado correctamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            print("Error al registrar:", e)
            flash('Ocurrió un error al registrar el usuario.', 'danger')
            return render_template('auth/register.html')

    return render_template('auth/register.html')



@app.route('/recover-password', methods=['GET', 'POST'])
def recover_password():
    if request.method == 'POST':
        username = request.form['username'].strip()
        new_password = request.form['new_password'].strip()

        from werkzeug.security import generate_password_hash

        hashed_password = generate_password_hash(new_password)

        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            cursor.execute("UPDATE user SET password = %s WHERE username = %s", (hashed_password, username))
            db.connection.commit()
            flash('Contraseña actualizada correctamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuario no encontrado.', 'danger')

    return render_template('auth/recover_password.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()