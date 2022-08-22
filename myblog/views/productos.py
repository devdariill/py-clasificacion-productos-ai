import functools #
from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)#
#1:12:39
from myblog.models.user import User #
from werkzeug.security import check_password_hash, generate_password_hash #
from myblog import db #
#/
from myblog.models.producto import Producto #

productos =Blueprint('productos', __name__, url_prefix='/productos')

#Registara Producto
@productos.route('/register',methods=('GET','POST'))
def register():
    if request.method =='POST':
        codprod = request.form.get('codprod')
        codbar  = request.form.get('codbar')
        nomprod = request.form.get('nomprod')
        exiprod = request.form.get('exiprod')
        cosprod = request.form.get('cosprod')
        venprod = request.form.get('venprod')
        pvenfra = request.form.get('pvenfra')

        producto=Producto(codprod, codbar, nomprod, exiprod, cosprod, venprod, pvenfra)     

        error=None   

        if not codprod:
          error='Se requiere codprod'
        elif not codbar:
          error='Se requiere codbar'
        elif not nomprod:
          error='Se requiere nomprod'
        elif not exiprod:
          error='Se requiere exiprod'
        elif not cosprod:
          error='Se requiere cosprod'
        elif not venprod:
          error='Se requiere venprod'
        elif not pvenfra:
          error='Se requiere pvenfra'
        
        user_name=Producto.query.filter_by(codprod=codprod).first()

        if user_name == None:
            db.session.add(producto)
            db.session.commit()
            #TODO
        else:
            error=f'el codprod {codprod}, ya esta registrado'
        flash(error)
            # return redirect(url_for('auth.login'))     
       
    return render_template('producto/register.html')



#     return render_template('auth/register.html')

# #INICAR SESION 1:27:54
# @auth.route('/login', methods=('GET', 'POST'))
# def login():
#     if request.method =='POST':
#         username = request.form.get('username')
#         password = request.form.get('password') 

#         error=None

        
#         user=User.query.filter_by(username=username).first()

#         if  user == None:
#             error='nobmre usuario incorrecto'
#         elif not check_password_hash(user.password,password):
#             error='error contraseña incorrecta'

#         if error is None:
#             session.clear()
#             session['user_id']=user.id
#             return redirect(url_for('blog.index'))           
#             #####return redirect(url_for('index'))           
        
#         #/
#         flash(error)

#     return render_template('auth/login.html')


# @auth.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')
#     if user_id is None :
#         g.user = None
#     else: 
#         g.user = User.query.get_or_404(user_id)

# @auth.route('/logout')
# def logout():    
#     session.clear()    
#     return redirect(url_for('blog.index'))  

# #1:46:42
# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))
#         return view(**kwargs)
#     return wrapped_view

