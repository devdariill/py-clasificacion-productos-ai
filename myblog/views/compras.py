from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from myblog import db

from myblog.models.producto import Producto
from myblog.views.auth import login_required
from werkzeug.exceptions import abort
from myblog.models.producto import Producto


compras = Blueprint('compras', __name__,url_prefix='/compras')
# productos =Blueprint('productos', __name__, url_prefix='/productos')

# listar todas la publicaciones
@compras.route("/",methods=('GET', 'POST'))
def index():
    return render_template('compras/index.html')
    
