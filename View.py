from flask import Flask, render_template, request, session, jsonify, redirect, url_for, json
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

@app.route('/cancel_movie', methods=['POST'])
def cancel_movie():
    movieID = request.form.get('movieID')
    movie = controller.search_movie_by_id(int(movieID))
    role = session.get('role')  
    if role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        if controller.cancel_movie(admin, movie):
            msg="movie cancled"
        else:
            msg="Cancel movie failed"
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

@app.route('/cancel_screening', methods=['GET'])
def cancel_screening():   
    screeningID = request.args.get('screeningID')
    movieID = request.args.get('movieID')
    movie = controller.search_movie_by_id(int(movieID))
    screening = controller.search_screening_by_id(movie, int(screeningID))
    role = session.get('role')
    if role == 'Admin':
        admin_serialized = session.get('admin')
        admin = pickle.loads(admin_serialized)
        if controller.cancel_screening(admin, movie, screening):
            msg="screening cancled"
        else:
            msg="cancel screening failed"
    movie_list = controller.get_movie_list()
    screenglist = movie.getScreeningList()
    return render_template("movie_detail.html", movie=movie, screenglist=screenglist, msg=msg, movie_list=movie_list, role=role, admin=admin, title="admin_homepage")

@app.route('/screening_seat', methods=['POST'])
def screening_seat(): 
    screeningID = request.form.get('screeningID')
    movieID = request.form.get('movieID')
    movie = controller.search_movie_by_id(int(movieID)) 
    screening = controller.search_screening_by_id(movie, int(screeningID))
    hall = screening.hall
    seats = hall.listOfSeats
    # Get max row and column values
    max_row = max(seat.row for seat in seats)  
    max_column = max(seat.column for seat in seats)
    selected_seats = [] 
    total_price = 0   
    role = session.get('role')
    return render_template("seat.html", hall=hall, screening=screening, total_price=total_price , selected_seats=selected_seats, max_row=max_row, max_column=max_column, seats=seats, movie=movie,  role=role, title="Seat")

@app.route('/booking_seat', methods=['POST'])
def booking_seat():
  screeningID = request.form.get('screeningID')
  movieID = request.form.get('movieID')
  movie = controller.search_movie_by_id(int(movieID)) 
  screening = controller.search_screening_by_id(movie, int(screeningID))
  hall = screening.hall
  seats = hall.listOfSeats
  selected_seats = request.form.get('selected_seats')
  total_price_str = request.form.get('total_price')
  selected_seats = json.loads(selected_seats)
  # Initialize a list to store the selected seat objects
  selected_seat_objects = []
  for selected_seat in selected_seats:
        seat_id = selected_seat["seatId"]
        for seat in seats:
            if seat.seatID == int(seat_id):
                seat.booked = True
                selected_seat_objects.append(seat)
                break 
  selected_seat_id_list = [seat.seatID for seat in selected_seat_objects]
  role = session.get('role')
  coupon_list = controller.get_coupon_list() 
  total_price = float(total_price_str) 
  if role == 'Customer':
      return render_template("payment.html", coupon_list=coupon_list, selected_seat_id_list=selected_seat_id_list, total_price=total_price , screening=screening,  movie=movie, role=role, title="Payment")
  else:
      customer_list = controller.get_customer_list() 
      return render_template("payment.html", customer_list=customer_list, coupon_list=coupon_list, selected_seat_id_list=selected_seat_id_list, total_price=total_price , screening=screening,  movie=movie, role=role, title="Payment")

@app.route('/add_credit_card', methods=['POST'])
def add_credit_card():
  amount = request.form.get('amount')
  creditCardNum = request.form.get('num')
  nameOnCard = request.form.get('name')
  expiryDate = request.form.get('date')
  cvv = request.form.get('cvv')
  credit_card = controller.add_credit_card_payment(amount, creditCardNum, nameOnCard, expiryDate, cvv)
  couponID = request.form.get('couponID')   
  coupon = controller.search_coupon(couponID)
  discount = credit_card.calcDiscount(coupon)
  total_price = credit_card.calcFinalPayment(coupon)
  screeningID = request.form.get('screeningID')
  movieID = request.form.get('movieID')
  movie = controller.search_movie_by_id(int(movieID)) 
  screening = controller.search_screening_by_id(movie, int(screeningID))
  selected_seat_id_list = request.form.get('selected_seat_id_list')
  selected_seat_id_list = json.loads(selected_seat_id_list)
  selected_seat_objects = []
  for selected_seat_id in selected_seat_id_list:
        seat = controller.search_seat(screening, int(selected_seat_id))  # Implement your function to retrieve the seat
        if seat:
            selected_seat_objects.append(seat)
        else:
            print("seat not found")  
  role = session.get('role')
  if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        booking = controller.make_booking(customer, movie, screening, selected_seat_objects, credit_card)
        booking.status = "Paid"
  else:
        customer_email = request.form.get('customer_email') 
        customer = controller.search_customer(customer_email)
        booking = controller.make_booking(customer, movie, screening, selected_seat_objects, credit_card)
        booking.status = "Paid" 
  notification = controller.send_add_booking_notification(booking)
  msg = notification.content
  return render_template("ticket.html",msg=msg, booking=booking, selected_seat_objects=selected_seat_objects, discount=discount,  payment=credit_card, total_price=total_price , screening=screening, movie=movie, role=role, title="Ticket")

@app.route('/add_debit_card', methods=['POST'])
def add_debit_card():
  amount = request.form.get('amount')
  bankName = request.form.get('bname')
  cardNum = request.form.get('number')
  nameOnCard = request.form.get('name')
  debit_card = controller.add_debit_card_payment(amount, cardNum, bankName, nameOnCard)
  couponID = request.form.get('couponID')   
  coupon = controller.search_coupon(couponID)
  discount = debit_card.calcDiscount(coupon)
  total_price = debit_card.calcFinalPayment(coupon)
  screeningID = request.form.get('screeningID')
  movieID = request.form.get('movieID')
  movie = controller.search_movie_by_id(int(movieID)) 
  screening = controller.search_screening_by_id(movie, int(screeningID))
  selected_seat_id_list = request.form.get('selected_seat_id_list')
  selected_seat_id_list = json.loads(selected_seat_id_list)
  selected_seat_objects = []
  for selected_seat_id in selected_seat_id_list:
        seat = controller.search_seat(screening, int(selected_seat_id))  
        if seat:
            selected_seat_objects.append(seat)
        else:
            print("seat not found")  
  role = session.get('role')
  if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        booking = controller.make_booking(customer, movie, screening, selected_seat_objects, debit_card)
        booking.status = "Paid"
  else:
        customer_email = request.form.get('customer_email') 
        customer = controller.search_customer(customer_email)
        booking = controller.make_booking(customer, movie, screening, selected_seat_objects, debit_card)
        booking.status = "Paid" 
  notification = controller.send_add_booking_notification(booking)
  msg = notification.content
  return render_template("ticket.html",msg=msg, booking=booking, selected_seat_objects=selected_seat_objects, discount=discount,  payment=debit_card, total_price=total_price , screening=screening, movie=movie, role=role, title="Ticket")

@app.route('/add_cash', methods=['POST'])
def add_cash():
  amount = request.form.get('amount')
  cash = controller.add_cash_payment(amount)
  couponID = request.form.get('couponID')   
  coupon = controller.search_coupon(couponID)
  discount = cash.calcDiscount(coupon)
  total_price = cash.calcFinalPayment(coupon)
  screeningID = request.form.get('screeningID')
  movieID = request.form.get('movieID')
  movie = controller.search_movie_by_id(int(movieID)) 
  screening = controller.search_screening_by_id(movie, int(screeningID))
  selected_seat_id_list = request.form.get('selected_seat_id_list')
  selected_seat_id_list = json.loads(selected_seat_id_list)
  selected_seat_objects = []
  for selected_seat_id in selected_seat_id_list:
        seat = controller.search_seat(screening, int(selected_seat_id))  
        if seat:
            selected_seat_objects.append(seat)
        else:
            print("seat not found")  
  role = session.get('role')
  if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        booking = controller.make_booking(customer, movie, screening, selected_seat_objects, cash)
        booking.status = "Paid"
  else:
        customer_email = request.form.get('customer_email') 
        customer = controller.search_customer(customer_email)
        booking = controller.make_booking(customer, movie, screening, selected_seat_objects, cash)
        booking.status = "Paid" 
  notification = controller.send_add_booking_notification(booking)
  msg = notification.content
  return render_template("ticket.html",msg=msg, booking=booking, selected_seat_objects=selected_seat_objects, discount=discount,  payment=cash, total_price=total_price , screening=screening, movie=movie, role=role, title="Ticket")

@app.route("/booking_detail")
def booking_detail():  
    role = session.get('role')
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        booking_list = controller.get_booking_list_for_customer(customer)
    else:
        booking_list = controller.get_booking_list()   
    return render_template("booking_detail.html", booking_list=booking_list, role=role, title="booking_detail")

@app.route('/cancel_booking', methods=['GET'])
def cancel_booking():   
    bookingID = request.args.get('bookingID')
    booking = controller.search_booking(int(bookingID))
    if controller.cancel_booking(booking):
        notification = controller.send_cancel_booking_notification(booking)
        msg = notification.content
    else:
        msg = "Booking not found or already canceled"
    role = session.get('role')
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        booking_list = controller.get_booking_list_for_customer(customer) 
    else:
        booking_list = controller.get_booking_list()    
    return render_template("booking_detail.html", msg=msg, booking_list=booking_list, role=role, title="booking_detail")

@app.route('/refund_booking', methods=['GET'])
def refund_booking():   
    bookingID = request.args.get('bookingID')
    booking = controller.search_booking(int(bookingID))
    if controller.issue_refund(booking):
        msg = "Refund completed"
    role = session.get('role')
    if role == 'Customer':
        customer_serialized = session.get('customer')
        customer = pickle.loads(customer_serialized)
        booking_list = controller.get_booking_list_for_customer(customer) 
    else:
        booking_list = controller.get_booking_list()    
    return render_template("booking_detail.html", msg=msg, booking_list=booking_list, role=role, title="booking_detail")


if __name__ == '__main__':
    app.run(debug=True)