from datetime import date
from flask import (
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from myblog import db

from myblog.models.compra import Compra
from myblog.models.detcompra import DetCompra
from myblog.models.producto import Producto
from myblog.models.tercero import Tercero
from myblog.views.auth import login_required
from werkzeug.exceptions import abort

compras = Blueprint('compras', __name__, url_prefix='/compras')


@compras.route("/", methods=('GET', 'POST'))
@login_required
def index():
    # TODO tercero default
    if request.method == 'POST' and "txtcategoria" in request.form:
        if (request.form['txtcategoria'] == ''):
            compras = reversed(Compra.query.all())
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
        compras = reversed(Compra.query.all())
        compras = list(compras)
        compras = compras[:5]
        db.session.commit()
    return render_template('compra/index.html', compras=compras)


@compras.route('/registerTercero', methods=('GET', 'POST'))
@login_required
def registerTercero():
    print("*"*50)
    print("baseurl", request.base_url)
    print("path", request.path)
    print("fullpath", request.full_path)
    print("scriptroot", request.script_root)
    print("url", request.url)
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


@compras.route('/registerCompra/<string:id>', methods=('GET', 'POST'))
@login_required
def registerCompra(id):
    tercero = Tercero.query.get(id)
    print("*"*50)
    print("baseurl", request.base_url)
    print("path", request.path)
    print("fullpath", request.full_path)
    print("scriptroot", request.script_root)
    print("url", request.url)
    # last_compra = Compra.query.order_by(Compra.numcom.desc()).first()
    last_compra = reversed(Compra.query.all())
    last_compra = list(last_compra)
    last_compra = last_compra[:1]
    last_compra = int(last_compra[0].numcom) + 1
    error = None
    if request.method == 'POST':
        numcom = request.form['numcom']
        docext = request.form['docext']
        feccom = request.form['feccom']
        vencom = request.form['vencom']
        horcom = request.form['horcom']
        forpag = request.form['forpag']
        nitter = tercero.nitter
        nomter = tercero.nomcom
        dirter = tercero.dirter
        telter = tercero.telter
        corele = tercero.corele
        codemp = g.user.username
        nomdoc = "COMPRA"
        subcom = 0
        totiva = 0
        totcom = 0
        estcom = "B"
        obscom = ""
        codclas = "S18"
        totdct = 0
        totaju = 0
        compra = Compra(numcom, nomdoc, docext, feccom, vencom, nitter, nomter, dirter, telter, corele,
                        subcom, totiva, totcom, estcom, codemp, horcom, obscom, codclas, forpag, totdct, totaju)
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
            error = 'Error al registrar la compra ' + error
        else:
            db.session.add(compra)
            db.session.commit()
            # TODO mostrar error
            error = f'Compra {numcom} : {nitter} DONE'
            print("*"*10, error)
            return redirect(url_for('compras.registerProductos', id=numcom))
            # return render_template('compra/registerCompra.html',compra=compra.numcom)
        flash(error)
    return render_template('compra/registerCompra.html', last_compra=last_compra)


@compras.route('/registerProductos/<string:id>', methods=('GET', 'POST'))
def registerProductos(id):
    # productos_Compra= DetCompra.select(DetCompra.c.numcom == id).execute().all() # no funciona

    # get products from detcompra by numcom
    # productos_Compra =  DetCompra.query.all()
    # productos_Compra = DetCompra.query.filter_by(numcom=id)

    # productos_Compra=DetCompra.query.filter(DetCompra.numcom == id).all()
    # frameworks =[framework for framework in productos_Compra if framework.numcom == id]

    # data1 = session.query(DetCompra).all() # no editado
    # data = DetCompra.query.filter_by(numcom=id).all()
    # data2 = db.session.query(DetCompra).filter(DetCompra.numcom == id).all()
    productos_Compra = DetCompra.query.filter(DetCompra.numcom ==id).all() 
    # for album in data2:
    #     print("Album: " + album.codprod)

    # session = db.session()
    # cursos = session.execute(
    #     f"select * from detcompras where numcom = '{id}'").cursor.fetchall()
    # tercero = cursos

    

    if request.method == 'POST' and "txtcategoria" in request.form:
        if (request.form['txtcategoria'] == ''):
            #TODO optimizar
            productos = reversed(Producto.query.all())
            productos = list(productos)
            productos = productos[:5]
            db.session.commit()
        else:
            print("**"*20)
            productos1 = db.session.query(Producto).filter(
                Producto.codprod.like("%"+request.form['txtcategoria']+"%")).all()
            productos2 = db.session.query(Producto).order_by(Producto.nomprod).filter(
                Producto.nomprod.like("%"+request.form['txtcategoria']+"%")).all()
            productos = productos1 + productos2
            db.session.commit()
            return render_template('compra/registerProductos.html', productos=productos, id_compra=id, productos_Compra=productos_Compra)
    else:
        productos = reversed(Producto.query.all())
        productos = list(productos)
        productos = productos[:5]
        db.session.commit()

    return render_template('compra/registerProductos.html', productos=productos, id_compra=id, productos_Compra=productos_Compra)

# numcom, codprod, #codcon, nomdet, #serdet, venfec, valuni, candet, ivapor, ivapes,
# cosuni, totdet, numite, codclas, #dctpor, undfra, #reginv


@compras.route('/registerProductos/<string:id_compra>/Agregar/<int:id_producto>', methods=('GET', 'POST'))
@login_required
def agregarProducto(id_compra, id_producto):
    compra = Compra.query.get(id_compra)
    producto = Producto.query.get(id_producto)
    # TODO CHECKOUT
    query = db.session.query(DetCompra.numcom).filter(
        DetCompra.numcom == id_compra).all()

    print("*"*50, "\n", query, len(query), "\n", "*"*50)
# numcom, codprod, #codcon, nomdet, #serdet, venfec, valuni, candet, ivapor, ivapes, cosuni, totdet, numite, codclas, dctpor, undfra, reginv

    if request.method == 'POST':

        # TODO IDEA evitar errores de duplicidad de productos
        numcom = compra.numcom  # request.form['numcom']
        codprod = producto.codprod  # request.form['codprod']
        nomdet = producto.nomprod  # request.form['nomdet']
        venfec = date.today() #str
        ivapor = request.form['ivapor']
        valor = request.form['valuni']
        dctpor = request.form['dctpor']        
        candet = request.form['candet']
        print(request.form['ivaIncluido'] ) #
        if(request.form['ivaIncluido'] == '1'):
            valuni = valor/(ivapor/100+1) # 909.09
            ivapes = (valuni-valor) # 1000 - 909.09 = 90.91 # request.form['ivapes']       
            ivapes = ivapes-(ivapes*dctpor/100) # 90.91 - (90.91*10/100) = 81.82
            cosuni = valor+ivapes # 1000
            cosuni = cosuni-(cosuni*dctpor/100) # 1000 - (1000*10/100) = 900
            totdet = cosuni*candet # request.form['totdet']
        else:
            valuni = valor # 1000
            cosuni = valor*(ivapor/100+1) # 1000*1.1 = 1100
            cosuni = cosuni-(cosuni*dctpor/100) # 1100 - (1100*10/100) = 990
            ivapes = cosuni-valor #1100-1000= 100 # request.form['ivapes']       
            ivapes = ivapes - (ivapes*dctpor/100) # 100 - (100*10/100) = 90      
            totdet = cosuni*candet 
        
        
        numite = str(len(query)+1)  # request.form['numite']
        codclas = request.form['codclas']
        undfra = producto.undfra  # request.form['undfra']

        # TODO FIX 0000000

        detcompra = DetCompra(numcom, codprod, nomdet, venfec, valuni, candet,
                              ivapor, ivapes, cosuni, totdet, numite, codclas, dctpor, undfra)

        db.session.add(detcompra)
        db.session.commit()

        print("*"*50, "\n", detcompra, "\n", "*"*50)

        ivaIncluido = request.form['ivaIncluido']
        print("*"*50, "\n", ivaIncluido, "\n", "*"*50)

    return render_template('compra/agregarProducto.html', compra=compra, producto=producto)
