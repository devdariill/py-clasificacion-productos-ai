from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from myblog import db

from myblog.models.compra import Compra
from myblog.views.auth import login_required




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
            

            #compras = compras1 #+ compras2
            
            db.session.commit()
            return render_template('compra/index.html', compras=compras)
    else:
        compras = reversed( Compra.query.all() ) 
        compras = list(compras)  
        compras = compras[:5]  
        db.session.commit()

    return render_template('compra/index.html', compras=compras)

# Registara Producto
@compras.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    last_compra = Compra.query.order_by(Compra.numcom.desc()).first()
    
    # numcom, nomdoc, precom, docext, feccom, vencom, nitter, nomter, dirter, telter, corele, subcom, totiva, totcom, estcom, codemp,
    # horcom, obscom, codclas, forpag, totdct, totaju

    if request.method == 'POST':
        numcom = request.form.get('numcom')
        nomdoc = request.form.get('nomdoc')
        precom = request.form.get('precom')
        docext = request.form.get('docext')
        feccom = request.form.get('feccom')
        vencom = request.form.get('vencom')
        nitter = request.form.get('nitter')
        nomter = request.form.get('nomter')
        dirter = request.form.get('dirter')
        telter = request.form.get('telter')
        corele = request.form.get('corele')
        subcom = request.form.get('subcom')
        totiva = request.form.get('totiva')
        totcom = request.form.get('totcom')
        estcom = request.form.get('estcom')
        codemp = request.form.get('codemp')
        horcom = request.form.get('horcom')
        obscom = request.form.get('obscom')
        codclas = request.form.get('codclas')
        forpag = request.form.get('forpag')
        totdct = request.form.get('totdct')
        totaju = request.form.get('totaju')

        compra = Compra(
            numcom=numcom,
            nomdoc=nomdoc,
            precom=precom,
            docext=docext,
            feccom=feccom,
            vencom=vencom,
            nitter=nitter,
            nomter=nomter,
            dirter=dirter,
            telter=telter,
            corele=corele,
            subcom=subcom,
            totiva=totiva,
            totcom=totcom,
            estcom=estcom,
            codemp=codemp,
            horcom=horcom,
            obscom=obscom,
            codclas=codclas,
            forpag=forpag,
            totdct=totdct,
            totaju=totaju
        )
        
        error = None

        if not numcom:
            error = 'El número de compra es requerido.'
        elif not nomdoc:
            error = 'El nombre del documento es requerido.'
        elif not precom:
            error = 'El precio de compra es requerido.'
        elif not docext:
            error = 'El documento externo es requerido.'
        elif not feccom:    
            error = 'La fecha de compra es requerida.'
        elif not vencom:    
            error = 'La fecha de vencimiento es requerida.'
        elif not nitter:    
            error = 'El nit del tercero es requerido.'
        elif not nomter:    
            error = 'El nombre del tercero es requerido.'
        elif not dirter:    
            error = 'La dirección del tercero es requerida.'    
        elif not telter:    
            error = 'El teléfono del tercero es requerido.'
        elif not corele:    
            error = 'El correo electrónico del tercero es requerido.'
        elif not subcom:    
            error = 'El subtotal de compra es requerido.'
        elif not totiva:    
            error = 'El total de iva es requerido.'
        elif not totcom:    
            error = 'El total de compra es requerido.'
        elif not estcom:    
            error = 'El estado de compra es requerido.'
        elif not codemp:    
            error = 'El código de empleado es requerido.'
        elif not horcom:    
            error = 'La hora de compra es requerida.'
        elif not obscom:    
            error = 'La observación de compra es requerida.'
        elif not codclas:    
            error = 'El código de clasificación es requerido.'
        elif not forpag:    
            error = 'La forma de pago es requerida.'
        elif not totdct:    
            error = 'El total de descuento es requerido.'
        elif not totaju:    
            error = 'El total de ajuste es requerido.'

        compra_id= Compra.query.filter_by(docext=docext).first()

        if compra_id == None:
            db.session.add(compra)
            db.session.commit()
            error = f'La compra {docext} - {nitter} - {numcom} ha sido registrada exitosamente.'
            return redirect(url_for('compras.index'))

        else:
            error = f'ERROR: el codprod {docext} - {numcom} - {nitter}, ya esta registrado'
        flash(error)
        

    return render_template('compra/register.html',last_producto=int(last_compra.numcom)+1)

