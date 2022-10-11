from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)
from myblog import db
from myblog.models.producto import Producto
from myblog.views.auth import login_required
from werkzeug.exceptions import abort



productos = Blueprint('productos', __name__)
# productos =Blueprint('productos', __name__, url_prefix='/productos')

# listar todas la publicaciones
@productos.route("/", methods=('GET', 'POST'))
def index():

    if request.method == 'POST' and "txtcategoria" in request.form:
        if(request.form['txtcategoria'] == ''):
            productos = reversed( Producto.query.all() ) 
            productos = list(productos)  
            productos = productos[:5]  
            db.session.commit()
        else:

            productos1 = db.session.query(Producto).filter(
                Producto.codprod.like("%"+request.form['txtcategoria']+"%")).all()
            productos2 = db.session.query(Producto).order_by(Producto.nomprod).filter(
                Producto.nomprod.like("%"+request.form['txtcategoria']+"%")).all()

            productos = productos1 + productos2
            db.session.commit()
            return render_template('producto/index.html', productos=productos)
    else:
        productos = reversed(Producto.query.all())
        productos = list(productos)      
        #TODO cache ultimo producto para enviarlo a nuevo registro producto  
        productos = productos[:5]        
        db.session.commit()

    return render_template('producto/index.html', productos=productos)


# Registara Producto
@productos.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    last_producto = Producto.query.order_by(Producto.codprod.desc()).first()    
    if request.method == 'POST':
        codprod = request.form.get('codprod')
        codbar = request.form.get('codbar')
        nomprod = request.form.get('nomprod')
        exiprod = request.form.get('exiprod')
        cosulc = request.form.get('cosulc')
        venprod = request.form.get('venprod')
        undfra = request.form.get('undfra')
        pvenfra = request.form.get('pvenfra')


        producto = Producto(codprod, codbar, nomprod,
                            exiprod, cosulc, venprod, undfra, pvenfra)

        error = None

        if not codprod:
            error = 'Se requiere codprod'
        # elif not codbar:
        #   error='Se requiere codbar'
        elif not nomprod:
            error = 'Se requiere nomprod'
        # elif not exiprod:
        #   error='Se requiere exiprod'
        elif not venprod:
            error = 'Se requiere venprod'
        elif not cosulc:
            error = 'Se requiere cosulc'
        elif not undfra:
            error = 'Se requiere undfra'
        elif not pvenfra:
            error = 'Se requiere pvenfra'

        print("user:",producto)
        cod_libre = Producto.query.filter_by(codprod=codprod).first()

        if cod_libre == None:
            db.session.add(producto)
            db.session.commit()
            error = f'Producto {nomprod} : {codprod} DONE'
            return redirect(url_for('productos.index'))
        else:
            error = f'ERROR: el codprod {codprod}, ya esta registrado'

        flash(error)
        # return redirect(url_for('auth.login'))

    return render_template('producto/register.html',last_producto=int(last_producto.codprod)+1)


# obtener producto por id
def get_producto(id):
    # producto = Producto.query.filter_by(id=id).first()
    producto = Producto.query.get(id)
    if producto is None:
        abort(404, "Producto id {0} doesn't exist.".format(id))
    return producto

# eliminar producto
@productos.route('/producto/delete/<int:id>', methods=('GET', 'POST'))
@login_required
def delete(id):
    producto = get_producto(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos.index'))

# actualziar producto
@productos.route('/producto/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    producto = get_producto(id)
    error = None    
    if request.method == 'POST':
        cod_prod = Producto.query.filter_by(codprod=request.form.get('codprod')).first()
        if (cod_prod != None and cod_prod.codprod != producto.codprod):
            error = f'ERROR: el codprod {producto.codprod}, ya esta registrado'
            flash(error)
            return render_template('producto/update.html', producto=producto)
        producto.codprod = request.form.get('codprod')
        producto.codbar  = request.form.get('codbar')
        producto.nomprod = request.form.get('nomprod')
        producto.exiprod = request.form.get('exiprod')
        producto.cosprod = request.form.get('cosprod')
        producto.venprod = request.form.get('venprod')
        producto.undfra  = request.form.get('undfra')
        producto.pvenfra = request.form.get('pvenfra')
        if not producto.codprod:
            error = 'Se requiere codprod'       
        elif not producto.codbar:
            error = 'Se requiere codbar'
        elif not producto.nomprod:
            error = 'Se requiere nomprod'
        elif not producto.exiprod:
            error = 'Se requiere exiprod'
        elif not producto.venprod:
            error = 'Se requiere venprod'
        elif not producto.cosprod:
            error = 'Se requiere cosprod'
        elif not producto.undfra:
            error = 'Se requiere undfra'
        elif not producto.pvenfra:
            error = 'Se requiere pvenfra'
        else:
            db.session.add(producto)
            db.session.commit()
            return redirect(url_for('productos.index'))
        flash(error)
    return render_template('producto/update.html', producto=producto)
