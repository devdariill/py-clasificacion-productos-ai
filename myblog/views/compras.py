from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from myblog import db

from myblog.models.compra import Compra
from myblog.models.tercero import Tercero
from myblog.views.auth import login_required
from werkzeug.exceptions import abort

compras = Blueprint('compras', __name__,url_prefix='/compras')

@compras.route("/",methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST' and "txtcategoria" in request.form:
        if(request.form['txtcategoria'] == ''):
            compras = reversed( Compra.query.all() ) 
            compras = list(compras)  
            compras = compras[:5]  
            db.session.commit()
        else:
            print("**"*20)
            compras1 = db.session.query(Compra).filter(
                Compra.numcom.like("%"+request.form['txtcategoria']+"%")).all()
            compras2 = db.session.query(Compra).order_by(Compra.docext).filter(
                Compra.docext.like("%"+request.form['txtcategoria']+"%")).all()
            compras = compras1 + compras2
            db.session.commit()
            return render_template('compra/index.html', compras=compras)
    else:
        compras = reversed( Compra.query.all() ) 
        compras = list(compras)  
        compras = compras[:5]  
        db.session.commit()
    return render_template('compra/index.html', compras=compras)


@compras.route('/registerTercero', methods=('GET', 'POST'))
@login_required
def registerTercero():
    terceros = reversed(Tercero.query.all())
    terceros = list(terceros)
    terceros = terceros[:5]
    if request.method == 'POST' and "txtcategoria" in request.form:
        if (request.form['txtcategoria'] == ''):            
            db.session.commit()
        else:
            terceros1 = db.session.query(Tercero).filter(
                Tercero.nitter.like("%"+request.form['txtcategoria']+"%")).all()
            terceros2 = db.session.query(Tercero).order_by(Tercero.nomcom).filter(
                Tercero.nomcom.like("%"+request.form['txtcategoria']+"%")).all()
            terceros = terceros1 + terceros2
            db.session.commit()
            return render_template('compra/registerTercero.html', terceros=terceros)
    return render_template('compra/registerTercero.html', terceros=terceros)


@compras.route('/compra/registerCompra/<string:id>', methods=('GET', 'POST'))
@login_required
def registerCompra(id):
    tercero = Tercero.query.get(id)
    last_compra = Compra.query.order_by(Compra.numcom.desc()).first()   
    last_compra = last_compra.numcom +1
    error = None    
    if request.method == 'POST':
        numcom = request.form['numcom']
        docext = request.form['docext']
        feccom = request.form['feccom']
        vencom = request.form['vencom']        
        horcom = request.form['horcom']
        forpag = request.form['forpag']
        nitter=tercero.nitter
        nomter=tercero.nomcom
        dirter=tercero.dirter
        telter=tercero.telter
        corele=tercero.corele
        codemp = g.user.username
        nomdoc="COMPRA"
        subcom=0
        totiva=0
        totcom=0
        estcom="B"
        obscom=""
        codclas="S18"
        totdct=0
        totaju=0
        compra = Compra(numcom,nomdoc,docext,feccom,vencom, 
                        nitter, nomter, dirter, telter, corele,subcom,
                        totiva,totcom,estcom,codemp, horcom,
                        obscom,codclas,forpag,totdct,totaju)
        if not numcom:
            error = 'numcom is required.'
        # elif not nomdoc:
        #     error = 'nomdoc is required.'
        elif not docext:
            error = 'docext is required.'
        elif not feccom:
            error = 'feccom is required.'
        elif not vencom:
            error = 'vencom is required.'    
        elif not codemp:
            error = 'codemp is required.'
        elif not horcom:
            error = 'horcom is required.'
        if error is not None:
            error = 'Error al registrar la compra ' +error
        else:
            db.session.add(compra)
            db.session.commit()
            #TODO mostrar error
            error = f'Compra {numcom} : {nitter} DONE'
            print("*"*10,error)
            return redirect(url_for('compras.registerProductos'))            
            #return render_template('compra/registerCompra.html',compra=compra.numcom)
        flash(error)
    return render_template('compra/registerCompra.html',last_compra=last_compra)

@compras.route('/compra/registerProductos/', methods=('GET', 'POST'))
@login_required
def registerProductos():
    # compra_actual=get_compra(id)
    # productos = reversed(Producto.query.all())

    #TODO get todos los productos registrados en detcompra by idcompra
    return render_template('compra/registerProductos.html')




