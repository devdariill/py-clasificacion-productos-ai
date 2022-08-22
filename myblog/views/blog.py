from flask import (
    render_template,Blueprint,flash,g,redirect,request,url_for
)#
from werkzeug.exceptions import abort #
from myblog.models.post import Post #
from myblog.models.user import User #
from myblog.views.auth import login_required #
from myblog import  db #

#registar blueprint
blog = Blueprint('blog',__name__)

#obtener usuario mediuante id
def get_user(id):
    user = User.query.get_or_404(id)
    return user

#listar todas la publicaciones
@blog.route("/")
def index():
    posts = Post.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    #return render_template('blog/index.html',posts=posts)
    #2:16:44 envio de get_user, llamando al metodo desde el return
    return render_template('blog/index.html',posts=posts,get_user=get_user)
    #/

#CREAR PUBLICACONI
@blog.route('/blog/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method =='POST':
        title = request.form.get('title')
        body = request.form.get('body')

        #g tiene la sesion actual, la cual usaremos para sacar el id del login y automatizar el campo de mysql
        post = Post(g.user.id  ,title, body)

        error=None

        if not title:
            error='Se requiere un titulo '
        if error is not None:
            flash (error)
        # si error no es nulo pasara a registrar    
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))        
        flash(error)
    return render_template('blog/create.html')


#2:27:30
def get_post(id,check_author=True):
    post = Post.query.get(id)
    if post is None:
        abort(404,f'Id {id}, de la publicacion no existe ')
    if check_author and post.author != g.user.id:
        abort(404)
    return post

#CREAR PUBLICACONI
@blog.route('/blog/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    post=get_post(id)

    if request.method =='POST':
        post.title = request.form.get('title')
        post.body = request.form.get('body')       

        error=None

        if not post.title:
            error='Se requiere un titulo desde update'
        if error is not None:
            flash (error)
        # si error no es nulo
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))        
        flash(error)
    return render_template('blog/update.html',post=post)

#eliminar un post
@blog.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    post=get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))