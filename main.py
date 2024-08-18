# from flask import Flask, render_template, request, session , redirect
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import secure_filename
# from flask_mail import Mail  #taaki jab koi user contact me apni details send krega to humpe gmail ki madad se mail aayega
# import os
# import math
# import json
# from datetime import datetime
#
# with open("config.json", 'r') as c:
#     params = json.load(c)["params"]
#
# local_server = True
#
# app = Flask(__name__)
# app.secret_key = "super-secret-key"
# app.config['UPLOAD_FOLDER'] = params['upload_location']
#
# app.config.update(
#
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT='465',
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=params['gmail-user'],
#     MAIL_PASSWORD=params['gmail-password']
#
# )
# mail = Mail(app)
# if local_server:
#     app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
#
# else:
#     app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
#
# db = SQLAlchemy(app)
#
#
# #Ye class database ki tables ko define karegi
#
# class Contacts(db.Model):
#     '''
#     sno,name,phone_num,msg,email
#     '''
#
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     email = db.Column(db.String(20), nullable=False)
#
#
# class Posts(db.Model):
#     '''
#     sno,name,phone_num,msg,email
#     '''
#
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(21), nullable=False)
#     content = db.Column(db.String(120), nullable=False)
#     tagline = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     img_file = db.Column(db.String(12), nullable=True)
#
#
# @app.route('/')
# def home():
#     posts = Posts.query.filter_by().all()
#     last=math.floor(len(posts)/int(params['no_of_posts']))
#     #Pagination Logic
#     # posts=posts[]
#     page=request.args.get('page')
#     if(not str(page).isnumeric()):
#         page=1
#
#     posts=Posts[page*int(params['no_of_posts'])+ int(params['no_of_posts'])]
#     if(page==1):
#        prev="#"
#        next="/?number= " + str(page+1)
#
#     elif(page==last):
#         prev="/?number= " + str(page- 1)
#         next="#"
#
#     else:
#         prev = "/?number= " + str(page - 1)
#         next = "/?number= " + str(page + 1)
#
#     #posts variable hum search krwayege database aur usse values uthayenge
#     return render_template('index.html', params=params, posts=posts, prev=prev , next=next)
#
#
# @app.route('/post/<string:post_slug>', methods=["GET"])
# def post_route(post_slug):
#     #post ko fetch kr rhe haii
#     post = Posts.query.filter_by(slug=post_slug).first()
#
#     return render_template('post.html', params=params, post=post)
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html', params=params)
#
#
# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     if 'user' in session and session['user'] == params['admin_user']:
#         posts = Posts.query.all()
#         return render_template('dashboard.html', params=params, posts=posts)
#
#     if request.method == 'POST':
#         username = request.form.get('uname')
#         userpass = request.form.get('pass')
#
#         if (username == params['admin_user'] and userpass == params['admin_password']):
#             #set the session variable
#             session['user'] = username
#             posts = Posts.query.all()
#             return render_template('dashboard.html', params=params, posts=posts)
#
#         #Redirecct to admin panel
#
#     return render_template('login.html', params=params)
#
#
# @app.route("/edit/<string:sno>", methods=['GET', 'POST'])
# def edit(sno):
#     #Cehck if user is log inned or not
#     if 'user' in session and session['user'] == params['admin_user']:
#         if request.method == 'POST':
#             box_title = request.form.get('title')
#             tline = request.form.get('tline')
#             slug = request.form.get('slug')
#             content = request.form.get('content')
#             img_file = request.form.get('img_file')
#             date = datetime.now()
#
#             if sno =='0':
#                 post=Posts(title=box_title,tagline=tline,slug=slug,content=content,img_file=img_file,date=date)
#
#                 db.session.add(post)
#                 db.session.commit()
#
#             else:
#                 post=Posts.query.filter_by(sno=sno).first()
#                 post.title=box_title
#                 post.slug=slug
#                 post.content=content
#                 post.tagline=tline
#                 post.img_file=img_file
#                 post.date=date
#                 db.session.commit()
#                 return redirect('/edit/' + sno)
#         post=Posts.query.filter_by(sno=sno).first()
#
#         return render_template('edit.html',params=params,post=post)
#
#
# @app.route('/uploader', methods=['GET', 'POST'])
# def uploader():
#     #agar banda logged in hai to
#     if 'user' in session and session['user'] == params['admin_user']:
#
#         if request.method=='POST':
#             f=request.files['file1']
#             f.save(os.path.join(app.config['UPLOAD_FOLDER'] , secure_filename(f.filename)))
#             return "Uploaded Successfully"
#
#
# @app.route('/logout')
# def logout():
#     session.pop('user')
#     return redirect('/dashboard')
#
#
# @app.route("/delete/<string:sno>", methods=['GET', 'POST'])
# def delete(sno):
#     if 'user' in session and session['user'] == params['admin_user']:
#         post = Posts.query.filter_by(sno=sno).first()
#         db.session.delete(post)
#         db.session.commit()
#
#     return redirect('/dashboard')
#
#
#
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         '''
#         Add Entry to database
#         '''
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#
#         entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
#
#         db.session.add(entry)
#         db.session.commit()
#         mail.send_message('New message from' + name,
#                           sender=email,
#                           recipients=[params['gmail-user']],
#                           body="message" + "\n" + phone
#
#                           )
#
#     return render_template('contact.html', params=params)
#
#
# app.run(debug=True)


from flask import Flask, render_template, request, session, redirect , flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import os
import math
import json
from datetime import datetime

# Load configuration
with open("config.json", 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)

mail = Mail(app)

# Configure database URI
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

db = SQLAlchemy(app)


# Define database models
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=True)
    img_file = db.Column(db.String(120), nullable=True)


class User(db.Model):
    email = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    confirm_password = db.Column(db.String(20), nullable=False)


@app.route('/')
def home():
    posts = Posts.query.all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))

    page = request.args.get('page', 1, type=int)
    posts = posts[(page - 1) * int(params['no_of_posts']):page * int(params['no_of_posts'])]

    prev = f"/?page={page - 1}" if page > 1 else "#"
    next = f"/?page={page + 1}" if page < last else "#"

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


# @app.route('/post/<string:post_slug>', methods=["GET"])
# def post_route(post_slug):
#     if 'user' in session and session['user'] == params['admin_user']:
#         post = Posts.query.filter_by(slug=post_slug).first_or_404()
#         return render_template('post.html', params=params, post=post)
#     else:
#         flash('You are not logged in. Please login first.')
#         return render_template('login.html', params=params);
@app.route('/post/<string:post_slug>', methods=["GET"])
def post_route(post_slug):
    if 'user' in session :
        post = Posts.query.filter_by(slug=post_slug).first_or_404()
        return render_template('post.html', params=params, post=post)
    else:

        return redirect('/dashboard')



@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/login', methods=['GET', 'POST'])
def login():


    if request.method == 'POST':

        username = request.form.get('email')
        userpass = request.form.get('pass')

        user = User.query.filter_by(email=username).first()
        if not user:
            return redirect("/signup")
        if username == user.email and userpass == user.password:
            session['user'] = username
            posts = Posts.query.all()
            return redirect('/dashboard')
    else:
        return render_template('login.html',params=params)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():





    # if request.method == 'POST':
    #
    #     username = request.form.get('email')
    #     userpass = request.form.get('pass')
    #
    #     user = User.query.filter_by(email=username).first()
    #     if not user:
    #         return redirect("/signup")
    #     if username == user.email and userpass == user.password:
    #         session['user'] = username
    #         posts = Posts.query.all()
    #         return render_template('dashboard.html', params=params, posts=posts)


    if 'user' not in session:
        return redirect('/login')
    else:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    # return render_template('login.html', params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):

        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno == '0':
                post = Posts(title=box_title, tagline=tline, slug=slug, content=content, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)



        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,post=post)




@app.route("/add", methods=['POST'])
def add():

        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()


            post = Posts(title=box_title, tagline=tline, slug=slug, content=content, img_file=img_file, date=date)
            db.session.add(post)
            db.session.commit()





        return redirect('/dashboard')







@app.route('/uploader', methods=['POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if 'file1' not in request.files:
            return "No file part"

        f = request.files['file1']
        if f.filename == '':
            return "No selected file"

        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Uploaded Successfully"


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/dashboard')


@app.route("/delete/<int:sno>", methods=['GET'])
def delete(sno):



    post = Posts.query.filter_by(sno=sno).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return redirect('/dashboard')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                         email=email)
        db.session.add(entry)
        db.session.commit()

        mail.send_message(
            f'New message from {name}',
            sender=email,
            recipients=[params['gmail-user']],
            body=f"Message: {message}\nPhone: {phone}"
        )

    return render_template('contact.html', params=params)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        print(confirm_password)

        # Validate form inputs
        if not name or not email or not password or not confirm_password:
            flash("Please fill out all fields.")
            return render_template('signup.html')

        if password != confirm_password:
            flash("Passwords do not match.")
            return render_template('signup.html')

        # Check if the email is already in use
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email is already in use.")
            return render_template('signup.html')

        # Hash the password before storing it


        # Create new user entry
        new_user = User(name=name, email=email, password=password,confirm_password=confirm_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.")
        return redirect('/dashboard')

    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)

