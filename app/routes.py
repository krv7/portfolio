from flask import render_template, url_for, request, redirect, flash
from app import app
from app import db
from app.models import Blog, Project, User
from app.forms import ProjectForm, BlogForm, ProjectUpdateForm, BlogUpdateForm, LoginForm
from flask_login import logout_user, login_required, current_user, login_user
from werkzeug.urls import url_parse

global root
root = "http://localhost:5000"

@app.route('/')
@app.route('/index')
def index():
    dark = True
    return render_template('index.html', title='RESEARCHING THE DATA',background_url="portada_index_min.png", dark=dark)

@app.route('/portfolio')
def portfolio():
    dark = False
    projects = Project.query.all()
    return render_template('portfolio.html', title='PORTFOLIO', entries=projects, background_url="portada_project.webp", dark=dark)

@app.route('/blog')
def blog():
    dark = False
    entries = Blog.query.all()
    return render_template('blog.html', title='BLOG', entries=entries, background_url="portada_blog.webp", dark=dark)

@app.route('/blog/entry/<int:id>')
def blog_entry(id):
    entry = Blog.query.filter_by(id=id).first_or_404()
    if entry.image == None:
        background_url = "portada_blog.webp"
    else:
        background_url = entry.image
    title = entry.title
    content = entry.content
    split_content = content.split("<-img->")
    return render_template('blog_entry.html', title=title, entry=entry, background_url=background_url, split_content=split_content)

@app.route('/project/entry/<int:id>')
def project_entry(id):
    entry = Project.query.filter_by(id=id).first_or_404()
    if entry.image == None:
        background_url = "portada_project.webp"
    else:
        background_url = entry.image
    title = entry.title
    content = entry.content
    split_content = content.split("<img>")
    return render_template('project_entry.html', title=title, entry=entry, background_url=background_url, split_content=split_content)

@app.route('/cms')
@login_required
def cms():
    projects = Project.query.all()
    entries = Blog.query.all()
    return render_template('cms.html', projects=projects, entries=entries, root=root)

@app.route('/add_project')
@login_required
def add_project():
    form = ProjectForm()
    return render_template('add_project.html', title='Create Project', form=form, root=root)

@app.route('/add_blog')
@login_required
def add_blog():
    form = BlogForm()
    return render_template('add_blog.html', title='Create Blog', form=form, root=root)

@app.route('/update_project/<int:id>')
@login_required
def edit_project(id):
    project = Project.query.get(id)
    form = ProjectUpdateForm()
    form.id.data = project.id
    form.title.data = project.title
    form.description.data = project.description
    form.content.data = project.content
    form.cat.data = project.cat
    form.image.data = project.image
    return render_template('update_project.html', title='Update Project', form=form, root=root)

@app.route('/update_blog/<int:id>')
@login_required
def edit_blog(id):
    blog = Blog.query.get(id)
    form = BlogUpdateForm()
    form.id.data = blog.id
    form.title.data = blog.title
    form.description.data = blog.description
    form.content.data = blog.content
    form.cat.data = blog.cat
    form.image.data = blog.image
    return render_template('update_blog.html', title='Update Blog', form=form, root=root)

########################################## CRUD ###############################################
# Project CRUD
@app.route('/api/add_project',methods=["POST"])
@login_required
def create_project():
    title = request.form.get('title')
    description = request.form.get('description')
    content = request.form.get('content')
    cat = request.form.get('cat')
    image = request.form.get('image')
    project = Project(title=title,description=description,content=content,cat=cat, image=image)
    db.session.add(project)
    db.session.commit()
    return redirect('/cms')

@app.route('/api/delete_project/<int:id>')
@login_required
def delete_project(id):
    project = Project.query.filter_by(id=id).first()
    db.session.delete(project)
    db.session.commit()

    return redirect('/cms')

@app.route('/api/update_project/<int:id>', methods=["PUT","POST"])
@login_required
def update_project(id):
    project=Project.query.filter_by(id=id).first_or_404()
    project.title = request.form.get('title')
    project.description = request.form.get('description')
    project.content = request.form.get('content')
    project.cat = request.form.get('cat')
    project.image = request.form.get('image')
    db.session.commit()
    return redirect('/cms')

# Blog CRUD
@app.route('/api/add_blog',methods=["POST"])
@login_required
def create_blog():
    title = request.form.get('title')
    description = request.form.get('description')
    content = request.form.get('content')
    cat = request.form.get('cat')
    image = request.form.get('image')
    blog = Blog(title=title,description=description,content=content,cat=cat, image=image)
    db.session.add(blog)
    db.session.commit()
    return redirect('/cms')

@app.route('/api/delete_blog/<int:id>')
@login_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()

    return redirect('/cms')

@app.route('/api/update_blog/<int:id>', methods=["PUT","POST"])
@login_required
def update_blog(id):
    blog=Blog.query.filter_by(id=id).first_or_404()
    blog.title = request.form.get('title')
    blog.description = request.form.get('description')
    blog.content = request.form.get('content')
    blog.cat = request.form.get('cat')
    blog.image = request.form.get('image')

    db.session.commit()
    return redirect('/cms')

########################################## CRUD END ###############################################


########################################## LOGIN #####################################


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('cms')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

