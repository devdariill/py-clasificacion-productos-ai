import functools
from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from myblog.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from myblog import db
import pandas as pd


ventas = Blueprint('ventas', __name__, url_prefix='/ventas')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def printAnalitycs(mes):    
    session = db.session()
    cursos = session.execute(f"select * from detfventas where venfec>='2022-{mes}-1' and venfec<='2022-{mes+1}-1'").fetchall()
    # session = db.session()    
    # cursos = session.execute(f"select * from detfventas where venfec>='2022-{mes}-1' and venfec<='2022-{mes+1}-1'").cursor.fetchall()   
    # print(len(cursos))
    # print(cursos[0])
    # print(cursos[len(cursos)-1])    
    row_as_dict = [dict(row) for row in cursos]
    df = pd.DataFrame(row_as_dict)
    print(df.head(1))  
    df_csv = df.to_csv('myblog/static/csv/ventas.csv', index=False)
    # print(len(row_as_dict))
    # print(type(row_as_dict))
    # print(row_as_dict[0])
    # print(row_as_dict[len(row_as_dict)-1])



@ventas.route('/', methods=('GET', 'POST'))
@login_required
def analitycs():
    printAnalitycs(5)
    return render_template('analitycs/ventas.html')
