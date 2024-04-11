from flask import Flask, url_for, request, render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.get("/")
def form():
    html = ''''
    <form action= "/" enctype="multipart/form-data" method="post">
        <input type="file" id="file_input" name="uploaded_file">
        <input type="submit">
    </form>
    '''
    return html

@app.post("/")
def submit_form():
    file = request.files["uploaded_file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join('.', filename))
    return "file uploaded succesfully"

# @app.route("/")
# def index():
#     return "index page"

# @app.route("/hello")
# def hello_world():
#     return "Hello, World"

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return f'post {post_id}.'

# @app.route('/path/<path:subpath>')
# def path(subpath):
#     return f'Subpathn{subpath}.'

# @app.route('/url')
# def url():
#     return f'''
#             <p>{url_for('index')}</p>
#             <p>{url_for('login')}</p>
#             <p>{url_for('login', next="/")}</p>
#             <p>{url_for('profile', username='John Doe')}</p>
# '''

# app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def login():
#     # error = None
#     return request.method 
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'

    # return render_template('login.html',error=error)