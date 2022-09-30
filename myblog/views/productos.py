#registrar productos
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
from myblog.views.auth import login_required #
from werkzeug.exceptions import abort #
from myblog.models.producto import Producto #

import os,time

    


productos = Blueprint('productos', __name__)
# productos =Blueprint('productos', __name__, url_prefix='/productos')

#listar todas la publicaciones
@productos.route("/",methods=('GET','POST'))

def index():
  
  if request.method == 'POST' and "txtcategoria" in request.form:  


    #TODO cache busquedas
    productos1 = db.session.query(Producto).filter(Producto.codprod.like("%"+request.form['txtcategoria']+"%")).all()
    productos2 = db.session.query(Producto).order_by(Producto.nomprod).filter(Producto.nomprod.like("%"+request.form['txtcategoria']+"%")).all()
    # productos2 = productos2.order_by(Producto.nomprod.desc())
    

    productos = productos1 + productos2

    #productos.insert(0, codList)
    
    # sql="select * from productos where nomprod like '%"+request.form['txtcategoria']+"%'"
    # productos = db.engine.execute(sql)    
    db.session.commit()
    return render_template('producto/index.html',productos=productos)
  else:
    productos = reversed(Producto.query.all())    
    productos = list(productos)
    productos = productos[:5]
  
  
  #     elif request.form['submit_button'] == 'Do Something Else':
  # print(" ~ file: productos.py ~ line 22 ~ productos", productos)    
  # obj = ObjectRes.query.all()
  # obj = session.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
  #productos = list(Producto.query.order_by(Producto.codbar.desc()).limit(5).all())
  db.session.commit()


  return render_template('producto/index.html',productos=productos)
  #/

#Registara Producto
@productos.route('/register',methods=('GET','POST'))
@login_required
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
        # elif not codbar:
        #   error='Se requiere codbar'
        elif not nomprod:
          error='Se requiere nomprod'
        # elif not exiprod:
        #   error='Se requiere exiprod'
        elif not venprod:
          error='Se requiere venprod'
        elif not cosprod:
          error='Se requiere cosprod'
        elif not pvenfra:
          error='Se requiere pvenfra'
        
        user_name=Producto.query.filter_by(codprod=codprod).first()

        if user_name == None:
            db.session.add(producto)
            db.session.commit()
            error=f'Producto {nomprod} : {codprod} DONE'            
        else:
            error=f'ERROR: el codprod {codprod}, ya esta registrado'
        flash(error)
            # return redirect(url_for('auth.login'))     

    return render_template('producto/register.html')


#obtener producto por id
def get_producto(id):
    # producto = Producto.query.filter_by(id=id).first()    
    producto = Producto.query.get(id)
    if producto is None:
        abort(404, "Producto id {0} doesn't exist.".format(id))
        
    return producto

#eliminar producto
@productos.route('/producto/delete/<int:id>', methods=('GET', 'POST'))
@login_required
def delete(id):
  producto=get_producto(id)  
  db.session.delete( producto )
  db.session.commit()
  return redirect(url_for('productos.index'))

#crear producto
@productos.route('/producto/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):

  producto=get_producto(id)  
  error=None  

  if request.method =='POST':      
    producto.codprod = request.form.get('codprod')
    producto.codbar  = request.form.get('codbar')
    producto.nomprod = request.form.get('nomprod')
    producto.exiprod = request.form.get('exiprod')
    producto.cosprod = request.form.get('cosprod')
    producto.venprod = request.form.get('venprod')
    producto.pvenfra = request.form.get('pvenfra')   
    print("b",request.form)

    if not producto.codprod:
      error='Se requiere codprod'
    elif not producto.codbar:
      error='Se requiere codbar'
    elif not producto.nomprod:
      error='Se requiere nomprod'
    elif not producto.exiprod:
      error='Se requiere exiprod'
    elif not producto.venprod:
      error='Se requiere venprod'
    elif not producto.cosprod:
      error='Se requiere cosprod'
    elif not producto.pvenfra:
      error='Se requiere pvenfra'

    if error is not None:
        flash(error)
    else:
      db.session.add( producto )
      db.session.commit()
      return redirect(url_for('productos.index'))
    flash(error)        

  return render_template('producto/update.html',producto=producto)








