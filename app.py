from flask import Flask, render_template, request, redirect, url_for
import datetime


from Controller import Controller

app = Flask(__name__)

#Date time global variables for queries
today=datetime.date.today()
today_string=today.strftime("%Y-%m-%d")

controller = Controller()

@app.route("/")
def home():
    return render_template("home.html", title="homepage")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        controller.register(username, email, password)
        msg = "Register successed"
        return render_template("login.html", msg = msg, title="Login")
    return render_template("login.html", title="Login")

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/test")
def test():
    return render_template("test.html", title="Test")

# Define a route to handle the form submission and display the file content
@app.route('/read_file', methods=['POST'])
def read_file():
    try:
        # file_path = project/file/movies.txt
        # Get the file name and location from the form
        file_path = request.form['file_path']
        
        # Open and read the specified file
        with open(file_path, 'r') as file:
            file_content = file.read()
        return render_template('test.html', content=file_content)
    except FileNotFoundError:
        return "File not found."
    
@app.route('/write_file', methods=['POST'])
def write_file():
    try:
        # file_path = project/file/movies.txt
        # Get the file name and location from the form
        movie_name = request.form['movie_name']
        file_path = "project/file/movies.txt"
        
        # Open and read the specified file
        with open(file_path, 'a') as file:
            movie_info = f"\n {movie_name}"
            file.write(movie_info)
        return render_template('test.html')
    except FileNotFoundError:
        return "File not found."
    


if __name__ == '__main__':
    app.run(debug=True)