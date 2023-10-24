from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from datetime import datetime
import pickle


from Controller import Controller

app = Flask(__name__)

# Set a secret key for session management
app.config['SECRET_KEY'] = 'your_secret_key_here'

controller = Controller()

@app.route("/")
def home():
    movie_list = controller.get_movie_list()
    return render_template("home.html", movie_list=movie_list, title="homepage")

@app.route("/customer_home")
def customer_home():
    movie_list = controller.get_movie_list()
    role = session.get('role')
    customer_serialized = session.get('customer')
    customer = pickle.loads(customer_serialized)
    return render_template("customer_home.html", movie_list=movie_list, role=role, customer=customer, title="customer_homepage")

@app.route("/admin_home")
def admin_home():
    movie_list = controller.get_movie_list()
    role = session.get('role')
    admin_serialized = session.get('admin')
    admin = pickle.loads(admin_serialized)
    return render_template("admin_home.html", movie_list=movie_list, role=role, admin=admin, title="admin_homepage")

@app.route("/staff_home")
def staff_home():
    movie_list = controller.get_movie_list()
    role = session.get('role')
    staff_serialized = session.get('staff')
    staff = pickle.loads(staff_serialized)
    return render_template("staff_home.html", movie_list=movie_list, role=role, staff=staff, title="staff_homepage")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if controller.register(username, email, password):
            msg = "Register successed, Please Login to the system"
        else:
            msg = "Email is already registered, please try again"
        return render_template("login.html", msg = msg, title="Login")
    return render_template("login.html", title="Login")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        movie_list = controller.get_movie_list()
        if role == "customer":
            if controller.customer_login(email, password):
                customer = controller.customer_login(email, password)               
                customer_serialized = pickle.dumps(customer)
                session['customer'] = customer_serialized
                session['role'] = 'Customer'
                return render_template("customer_home.html", movie_list=movie_list, role=session['role'], customer=customer)
            msg = "Login failed, Please try again"
            return render_template("login.html", msg = msg, title="Login")
        if role == "admin":
            if controller.admin_login(email, password):
                admin = controller.admin_login(email, password)
                admin_serialized = pickle.dumps(admin)
                session['admin'] = admin_serialized
                session['role'] = 'Admin'
                return render_template("admin_home.html", movie_list=movie_list, role=session['role'], admin=admin)
            msg = "Login failed, Please try again"
            return render_template("login.html", msg = msg, title="Login")
        if role == "staff":
            if controller.staff_login(email, password):
                staff = controller.staff_login(email, password)
                staff_serialized = pickle.dumps(staff)
                session['staff'] = staff_serialized
                session['role'] = 'Staff'
                return render_template("staff_home.html", movie_list=movie_list, role=session['role'], staff=staff)
            msg = "Login failed, Please try again"
            return render_template("login.html", msg = msg, title="Login")
    return render_template("login.html", title="Login")

@app.route('/logout', methods=['GET'])
def logout():
    # Clear the session data
    session.clear()
    return redirect(url_for('login'))

@app.route("/search_genre", methods=['POST'])
def search_genre():
    role = session.get('role')
    genre = request.form.get('genre')
    movies = controller.get_movie_list()
    if genre == 'All':
        filtered_movies = movies
    else:
        filtered_movies = [movie for movie in movies if movie.genre == genre]
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        return render_template("customer_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], customer=customer)
    elif role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        return render_template("admin_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], admin=admin)
    elif role == 'Staff':
        staff_serialized = session.get('staff')
        staff = pickle.loads(staff_serialized)
        return render_template("staff_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], staff=staff)
    else:
        return render_template("home.html", filtered_movies = filtered_movies)

@app.route("/search_lang", methods=['POST'])
def search_lang():
    role = session.get('role')
    lang = request.form.get('lang')
    movies = controller.get_movie_list()
    if lang == 'All':
        filtered_movies = movies
    else:
        filtered_movies = [movie for movie in movies if movie.language == lang]
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        return render_template("customer_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], customer=customer)
    elif role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        return render_template("admin_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], admin=admin)
    elif role == 'Staff':
        staff_serialized = session.get('staff')
        staff = pickle.loads(staff_serialized)
        return render_template("staff_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], staff=staff)
    else:
        return render_template("home.html", filtered_movies = filtered_movies)

@app.route("/search_date", methods=['POST'])
def search_date():
    role = session.get('role')
    date = request.form.get('date')
    movies = controller.get_movie_list()
    if date == 'All':
        filtered_movies = movies
    else:
        filtered_movies = []
        for movie in movies:
            releaseDate = datetime.strptime(movie.releaseDate, '%Y-%m-%d')
            year = releaseDate.year
            if str(year) == date:
                filtered_movies.append(movie)
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        return render_template("customer_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], customer=customer)
    elif role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        return render_template("admin_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], admin=admin)
    elif role == 'Staff':
        staff_serialized = session.get('staff')
        staff = pickle.loads(staff_serialized)
        return render_template("staff_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], staff=staff)
    else:
        return render_template("home.html", filtered_movies = filtered_movies)

@app.route("/search_title", methods=['POST'])
def search_title():
    role = session.get('role')
    title = request.form.get('title')
    movies = controller.get_movie_list()
    if title == 'All':
        filtered_movies = movies
    else:
        filtered_movies = [movie for movie in movies if movie.title == title]
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        return render_template("customer_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], customer=customer)
    elif role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        return render_template("admin_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], admin=admin)
    elif role == 'Staff':
        staff_serialized = session.get('staff')
        staff = pickle.loads(staff_serialized)
        return render_template("staff_home.html", filtered_movies = filtered_movies,  movie_list=movies, role=session['role'], staff=staff)
    else:
        return render_template("home.html", filtered_movies = filtered_movies)

@app.route('/movie_detail', methods=['GET'])
def movie_detail():
    role = session.get('role')
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        movie_id = request.args.get('movie_id')
        movie = controller.search_movie_by_id(int(movie_id))
        title=movie.title
        screenglist = movie.getScreeningList()
        return render_template("movie_detail.html", screenglist=screenglist, title=title, movie=movie, movie_id=movie_id, role=role, customer=customer)
    if role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        movie_id = request.args.get('movie_id')
        movie = controller.search_movie_by_id(int(movie_id))
        title=movie.title
        screenglist = movie.getScreeningList()
        return render_template("movie_detail.html", screenglist=screenglist, title=title, movie=movie, movie_id=movie_id, role=role, admin=admin)
    if role == 'Staff':
        staff_serialized = session.get('staff')
        staff = pickle.loads(staff_serialized)
        movie_id = request.args.get('movie_id')
        movie = controller.search_movie_by_id(int(movie_id))
        title=movie.title
        screenglist = movie.getScreeningList()
        return render_template("movie_detail.html", screenglist=screenglist, title=title, movie=movie, movie_id=movie_id, role=role, staff=staff)

@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form.get('title')
    language = request.form.get('language')
    genre = request.form.get('genre')
    releaseDate = request.form.get('releaseDate')
    role = session.get('role')  
    if role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        if controller.add_movie(admin, title, language, genre, releaseDate):
            msg="New movie added"
        else:
            msg="Add movie failed"
        movie_list = controller.get_movie_list()
        return render_template("admin_home.html", msg=msg, movie_list=movie_list, role=role, admin=admin, title="admin_homepage")

@app.route('/add_screening', methods=['POST'])
def add_screening(): 
    screeningDate = request.form.get('date')
    startTime = request.form.get('startTime')
    endTime = request.form.get('endTime')
    hallName = request.form.get('hallName')
    hall = controller.search_hall(hallName)
    role = session.get('role')
    movie_id = request.form.get('movie_id')
    movie = controller.search_movie_by_id(int(movie_id))  
    if role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        if controller.add_screening(admin, movie, screeningDate, startTime, endTime, hall):
            msg="New screening added"
        else:
            msg="Add screening failed"
        movie_list = controller.get_movie_list()
        screenglist = movie.getScreeningList()
        return render_template("movie_detail.html", movie=movie, screenglist=screenglist, msg=msg, movie_list=movie_list, role=role, admin=admin, title="admin_homepage")


@app.route('/screening_seat', methods=['POST'])
def screening_seat(): 
    screeningID = request.form.get('screeningID')
    screening = controller.search_screening_by_id(int(screeningID))
    hall = screening.hall
    hall_name = hall.name
    movieID = request.form.get('movieID')
    role = session.get('role')
    movie_id = request.form.get('movie_id')
    movie = controller.search_movie_by_id(int(movie_id))  
    if role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        if controller.add_screening(admin, movie):
            msg="New screening added"
        else:
            msg="Add screening failed"
        movie_list = controller.get_movie_list()
        screenglist = movie.getScreeningList()
        return render_template("seat.html", booked_seats=booked_seats, movie=movie, screenglist=screenglist, msg=msg, movie_list=movie_list, role=role, admin=admin, title="admin_homepage")

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