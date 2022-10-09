import functools #
from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)#

from myblog.models.user import User #
from werkzeug.security import check_password_hash, generate_password_hash #
from myblog import db #

auth =Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

#Crear o Registara Usuario
@auth.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user=User(username, generate_password_hash(password))

        error=None

        if not username:
            error='Se requiere nombre de usuario'
        elif not password:
            error='Se requiere contraseña'
            
        user_name=User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))     
        else:
            error=f'el usuario {username}, ya esta registrado'
        #/
        flash(error)

    return render_template('auth/register.html')

#INICAR SESION 1:27:54
@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password') 

        error=None

        
        user=User.query.filter_by(username=username).first()

        if  user == None:
            error='nobmre usuario incorrecto'
        elif not check_password_hash(user.password,password):
            error='error contraseña incorrecta'

        if error is None:
            session.clear()
            session['user_id']=user.id
            return redirect(url_for('productos.index'))           
            #####return redirect(url_for('index'))           
        
        #/
        flash(error)

    return render_template('auth/login.html')


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None :
        g.user = None
    else: 
        g.user = User.query.get_or_404(user_id)

@auth.route('/logout')
def logout():    
    session.clear()    
    return redirect(url_for('productos.index'))  



