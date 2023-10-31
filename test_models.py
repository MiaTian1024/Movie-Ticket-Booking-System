from datetime import datetime, date
from Models import User, Guest, Customer, Admin, FrontDeskStaff, Movie, Screening, CinemaHall, Coupon, CreditCard, Payment, Booking, ScreeningSeat, DebitCard, Cash, Notification

# Sample test cases for the Customer class
class TestCustomer:
    def test_customer_creation(self):
        customer = Customer("customer123", "customer@example.com", "password")
        assert customer is not None
        assert customer.username == "customer123"
        assert customer.email == "customer@example.com"
        assert customer.password == "password"

    def test_customer_login_success(self):
        customer = Customer("customer123", "customer@example.com", "password")
        assert customer.login("customer@example.com", "password") is True

    def test_customer_login_failure(self):
        customer = Customer("customer123", "customer@example.com", "password")
        assert customer.login("user@example.com", "wrongpassword") is False

    def test_customer_logout(self):
        customer = Customer("customer123", "customer@example.com", "password")
        assert customer.logout() is True

    def test_customer_reset_password(self):
        customer = Customer("customer123", "customer@example.com", "password")
        customer.resetPassword("newpassword")
        assert customer.password == "newpassword"

    def test_customer_make_booking(self):
        customer = Customer("customer123", "customer@example.com", "password")
        booking = Booking(customer, None, None, None, None)
        customer.makeBooking(booking)
        assert booking in customer.getBookingList()

    def test_customer_cancel_booking(self):
        customer = Customer("customer123", "customer@example.com", "password")
        booking = Booking(customer, None, None, None, None)
        customer.makeBooking(booking)
        customer.cancelBooking(booking)
        assert booking not in customer.getBookingList()
        

# Sample test cases for the Admin class
class TestAdmin:
    def test_admin_creation(self):
        admin = Admin("admin123", "admin@example.com", "password")
        assert admin is not None
        assert admin.username == "admin123"
        assert admin.email == "admin@example.com"
        assert admin.password == "password"

    def test_admin_login_success(self):
        admin = Admin("admin123", "admin@example.com", "password")
        assert admin.login("admin@example.com", "password") is True

    def test_admin_login_failure(self):
        admin = Admin("admin123", "admin@example.com", "password")
        assert admin.login("user@example.com", "wrongpassword") is False

    def test_admin_logout(self):
        admin = Admin("admin123", "admin@example.com", "password")
        assert admin.logout() is True

    def test_admin_reset_password(self):
        admin = Admin("admin123", "admin@example.com", "password")
        admin.resetPassword("newpassword")
        assert admin.password == "newpassword"

    def test_admin_add_movie(self):
        admin = Admin("admin123", "admin@example.com", "password")
        movie = admin.addMovie("Movie Title", "English", "Action", datetime(2023, 10, 30))
        assert isinstance(movie, Movie)
        assert movie.title == "Movie Title"

    def test_admin_add_screening(self):
        admin = Admin("admin123", "admin@example.com", "password")
        hall = CinemaHall("Hall A", 100)
        screening = admin.addScreening(date(2023, 11, 1), datetime(2023, 11, 1, 15, 0), datetime(2023, 11, 1, 17, 0), hall)
        assert isinstance(screening, Screening)
        assert screening.screeningDate == date(2023, 11, 1)

    def test_admin_cancel_movie(self):
        admin = Admin("admin123", "admin@example.com", "password")
        movie = Movie("Movie Title", "English", "Action", datetime(2023, 10, 30))
        result = admin.cancelMovie(movie)
        assert result == movie

    def test_admin_cancel_screening(self):
        admin = Admin("admin123", "admin@example.com", "password")
        hall = CinemaHall("Hall A", 100)
        screening = Screening(date(2023, 11, 1), datetime(2023, 11, 1, 15, 0), datetime(2023, 11, 1, 17, 0), hall)
        result = admin.cancelScreening(screening)
        assert result == screening

# Sample test cases for the FrontDeskStaff class
class TestFrontDeskStaff:
    def test_front_desk_staff_creation(self):
        staff = FrontDeskStaff("staff123", "staff@example.com", "password")
        assert staff is not None
        assert staff.username == "staff123"
        assert staff.email == "staff@example.com"
        assert staff.password == "password"

    def test_front_desk_staff_login_success(self):
        staff = FrontDeskStaff("staff123", "staff@example.com", "password")
        assert staff.login("staff@example.com", "password") is True

    def test_front_desk_staff_login_failure(self):
        staff = FrontDeskStaff("staff123", "staff@example.com", "password")
        assert staff.login("user@example.com", "wrongpassword") is False

    def test_front_desk_staff_logout(self):
        staff = FrontDeskStaff("staff123", "staff@example.com", "password")
        assert staff.logout() is True

    def test_front_desk_staff_reset_password(self):
        staff = FrontDeskStaff("staff123", "staff@example.com", "password")
        staff.resetPassword("newpassword")
        assert staff.password == "newpassword"


# Sample test cases for the Guest class
class TestGuest:
    def test_register_customer(self):
        guest = Guest()
        customer = guest.register("testuser", "testuser@example.com", "password123")
        assert customer is not None
        assert customer.username == "testuser"
        assert customer.email == "testuser@example.com"
        assert customer.password == "password123"


# Sample test cases for the Movie class
class TestMovie:
    def test_movie_init(self):
        # Create a Movie object
        movie = Movie("The Matrix", "English", "Science Fiction", "2023-10-15")

        # Check if the movie attributes are set correctly
        assert movie.title == "The Matrix"
        assert movie.language == "English"
        assert movie.genre == "Science Fiction"
        assert movie.releaseDate == "2023-10-15"

    def test_get_screening_list(self):
        movie = Movie("Inception", "English", "Science Fiction", "2023-10-20")
        assert movie.getScreeningList() == []

    def test_add_screening(self):
        movie = Movie("Avengers", "English", "Action", "2023-10-22")
        # Assuming you have a Screening object to add
        screening = Screening("2023-10-22", "13:00", "15:30", "Hall A")

        # Add the screening to the movie
        movie.add_screening(screening)
        
        # Check if the screening was added to the movie's screening list
        assert screening in movie.getScreeningList()

    def test_search_screening(self):
        movie = Movie("The Shawshank Redemption", "English", "Drama", "2023-10-18")

        # Create a Screening object
        screening = Screening("2023-10-18", "15:00", "17:30", "Hall B")

        # Add the screening to the movie
        movie.add_screening(screening)

        # Search for the added screening
        found_screening = movie.search_screening(screening.screeningID)

        # Check if the found screening matches the added screening
        assert found_screening == screening

# Sample test cases for the Screening class
class TestScreening:
    def test_screening_creation(self):
        hall = CinemaHall("Test Hall", 100)
        screening_date = date(2023, 11, 1)
        start_time = datetime(2023, 11, 1, 12, 0)
        end_time = datetime(2023, 11, 1, 14, 0)
        screening = Screening(screening_date, start_time, end_time, hall)
        assert screening is not None
        assert screening.screeningDate == screening_date
        assert screening.startTime == start_time
        assert screening.endTime == end_time
        assert screening.hall == hall


# Sample test cases for the CinemaHall class
class TestCinemaHall:
    def test_cinema_hall_creation(self):
        cinema_hall = CinemaHall("Hall A", 100)
        assert cinema_hall is not None
        assert cinema_hall.name == "Hall A"
        assert cinema_hall.totalSeats == 100
        assert len(cinema_hall.listOfSeats) == 0


# Sample test cases for the ScreeningSeat class
class TestScreeningSeat:
    def test_screening_seat_creation(self):
        seat = ScreeningSeat(1, 1, 10.0)
        assert seat is not None
        assert seat.row == 1
        assert seat.column == 1
        assert seat.price == 10.0
        assert seat.booked is False


# Sample test cases for the Booking class
class TestBooking:
    def test_booking_creation(self):
        customer = Customer("Customer", "customer@example.com", "password")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 10, 30))
        hall = CinemaHall("Test Hall", 100)
        screening = Screening(date(2023, 11, 1), datetime(2023, 11, 1, 12, 0), datetime(2023, 11, 1, 14, 0), hall)
        seat = ScreeningSeat(1, 1, 10.0)
        payment = Cash(10.0)
        booking = Booking(customer, movie, screening, [seat], payment)
        assert booking is not None
        assert booking.customer == customer
        assert booking.movie == movie
        assert booking.screening == screening
        assert booking.bookingSeats == [seat]
        assert booking.payment == payment
        assert booking.status == "Pending"

    def test_send_add_booking_notification(self):
        customer = Customer("Customer", "customer@example.com", "password")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 10, 30))
        hall = CinemaHall("Test Hall", 100)
        screening = Screening(date(2023, 11, 1), datetime(2023, 11, 1, 12, 0), datetime(2023, 11, 1, 14, 0), hall)
        seat = ScreeningSeat(1, 1, 10.0)
        payment = Cash(10.0)
        booking = Booking(customer, movie, screening, [seat], payment)
        notification = booking.sendAddBookingNotification()
        assert notification is not None
        assert notification.content == f"Booking details:\n Movie: {movie.title}\nScreening Date: {screening.screeningDate}\nCustomer: {customer.username}"

    def test_send_cancel_booking_notification(self):
        customer = Customer("Customer", "customer@example.com", "password")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 10, 30))
        hall = CinemaHall("Test Hall", 100)
        screening = Screening(date(2023, 11, 1), datetime(2023, 11, 1, 12, 0), datetime(2023, 11, 1, 14, 0), hall)
        seat = ScreeningSeat(1, 1, 10.0)
        payment = Cash(10.0)
        booking = Booking(customer, movie, screening, [seat], payment)
        notification = booking.sendCancelBookingNotification()
        assert notification is not None
        assert notification.content == f"Canceling details:\n Movie: {movie.title}\nScreening Date: {screening.screeningDate}\nCustomer: {customer.username}"

# Sample test cases for the Notification class
class TestNotification:
    def test_notification_initialization(self):
        content = "This is a test notification."     
        notification = Notification(content)
        assert notification.notificationID is not None
        assert notification.content == content

    def test_notification_content_update(self):
        initial_content = "Initial content of the notification."
        notification = Notification(initial_content)
        new_content = "Updated content of the notification."
        notification.content = new_content
        assert notification.content == new_content


# Sample test cases for the CreditCard class
class TestCreditCard:
    def test_credit_card_creation(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2023, 12, 31), "123")
        assert credit_card is not None
        assert credit_card.amount == 50.0
        assert credit_card.creditCardNum == "1234567890123456"
        assert credit_card.nameOnCard == "John Doe"
        assert credit_card.expiryDate == datetime(2023, 12, 31)
        assert credit_card.cvv == "123"

    def test_calc_discount_no_coupon(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2023, 12, 31), "123")
        coupon = None
        assert credit_card.calcDiscount(coupon) == 0.0

    def test_calc_final_payment_no_coupon(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2023, 12, 31), "123")
        coupon = None
        assert credit_card.calcFinalPayment(coupon) == 50.0

    def test_calc_discount_with_valid_coupon(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2022, 12, 30), "123")
        coupon = Coupon("TestCoupon", "2023-12-31", 10.0)
        assert credit_card.calcDiscount(coupon) == 10.0

    def test_calc_discount_with_expired_coupon(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2023, 12, 31), "123")
        coupon = Coupon("TestCoupon", "2022-12-30", 10.0)
        assert credit_card.calcDiscount(coupon) == 0.0

    def test_calc_final_payment_with_valid_coupon(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2023, 12, 30), "123")
        coupon = Coupon("TestCoupon", "2023-12-31", 10.0)
        assert credit_card.calcFinalPayment(coupon) == 45.0

    def test_calc_final_payment_with_expired_coupon(self):
        credit_card = CreditCard(50.0, "1234567890123456", "John Doe", datetime(2023, 12, 31), "123")
        coupon = Coupon("TestCoupon", "2022-12-30", 10.0)
        assert credit_card.calcFinalPayment(coupon) == 50.0

# Sample test cases for the DebitCard class 
class TestDebitCard:
    def test_debit_card_creation(self):
        debit_card = DebitCard(50.0, "1234567890", "Test Bank", "John Doe")
        assert debit_card is not None
        assert debit_card.amount == 50.0
        assert debit_card.cardNum == "1234567890"
        assert debit_card.bankName == "Test Bank"
        assert debit_card.nameOnCard == "John Doe"

# Sample test cases for the Cash class
class TestCash:
    def test_cash_creation(self):
        cash = Cash(50.0)
        assert cash is not None
        assert cash.amount == 50.0

# Sample test cases for the Coupon class
class TestCoupon:
    def test_coupon_creation(self):
        coupon = Coupon("TestCoupon", datetime(2023, 12, 31), 10.0)
        assert coupon is not None
        assert coupon.couponID == "TestCoupon"
        assert coupon.expiryDate == datetime(2023, 12, 31)
        assert coupon.discount == 10.0