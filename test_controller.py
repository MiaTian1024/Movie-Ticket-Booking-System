# Author: Mia Tian (ID: 1154238)
# Login information for demonstration purposes only:
# - Admin: Email: amy@gmail.com, Password: 111
# - Front Desk Staff: Email: joe@gmail.com, Password: 111
# - Customer: Email: brain@gmail.com, Password: 111


from Controller import Controller
from datetime import datetime, date
from Models import Movie, Customer, Admin, FrontDeskStaff, Screening, CinemaHall, CreditCard, DebitCard, Cash, ScreeningSeat, Coupon, Payment, Booking
from ReadFile import ReadFile

# Create an instance of ReadFile to read data from files
file = ReadFile()

# Read data from files and store it in respective objects
customer_obj = file.getCustomerObj("file/customer.txt")
movie_obj = file.getMovieObj("file/movies.txt")
admin_obj = file.getAdminObj("file/admin.txt")
staff_obj = file.getStaffObj("file/staff.txt")
hall_obj = file.getHallObj("file/hall.txt")
screening_obj = file.getScreeningObj("file/screening.txt")
coupon_obj = file.getCouponObj("file/coupon.txt")

controller = Controller()
# Sample test cases for the Controller class
class TestController:
    def test_register_customer(self):
        assert controller.register("testuser", "testuser@example.com", "password123") == True

    def test_duplicate_customer_registration(self):
        controller.register("testuser", "testuser@example.com", "password123")
        assert controller.register("testuser", "testuser@example.com", "password123") == False

    def test_customer_login(self):
        assert controller.customer_login("brain@gmail.com", "111") != False

    def test_invalid_customer_login(self):
        assert controller.customer_login("testuser@example.com", "wrongpassword") == False

    def test_admin_login(self):
        assert controller.admin_login("amy@gmail.com", "111") != False

    def test_invalid_admin_login(self):
        controller = Controller()
        assert controller.admin_login("admin@example.com", "wrongpassword") == False

    def test_staff_login(self):
        assert controller.staff_login("joe@gmail.com", "111") != False

    def test_search_movie_by_id(self):
        # Search for a movie by its ID (1000)
        found_movie = controller.search_movie_by_id(1000)
        assert found_movie is not None
        # Search for a non-existent movie
        not_found_movie = controller.search_movie_by_id(9999)
        assert not_found_movie is None

    def test_search_movie_by_title(self):
        # Search for movies by title
        results = controller.search_movie_by_title("Spiderman")
        assert len(results) == 1
        results = controller.search_movie_by_title("Movie 3")  # No such movie
        assert len(results) == 0

    def test_search_movie_by_lang(self):
        # Search for movies by lang
        results = controller.search_movie_by_lang("English")
        assert len(results) == 4
        results = controller.search_movie_by_lang("Movie 3")  # No movie in this genre
        assert len(results) == 0

    def test_search_movie_by_genre(self):
        # Search for movies by genre
        results = controller.search_movie_by_genre("Action")
        assert len(results) == 2
        results = controller.search_movie_by_genre("Movie 3")  # No movie in this genre
        assert len(results) == 0

    def test_search_movie_by_date(self):
        # Search for movies by date
        results = controller.search_movie_by_date("2020-02-10")
        assert len(results) == 1
        results = controller.search_movie_by_date("2024-01-01")  # No movie in this date
        assert len(results) == 0

    def test_search_customer(self):
        found_customer = controller.search_customer("brain@gmail.com")
        # Check if the correct customer is found
        assert found_customer is not None
        # Try searching for a customer that does not exist
        not_found_customer = controller.search_customer("nonexistent@example.com")
        # Check that no customer is found
        assert not_found_customer is None

    def test_search_hall(self):
        # Search for the hall by name
        found_hall = controller.search_hall("Hall-1")
        # Check if the correct hall is found
        assert found_hall is not None
        # Try searching for a hall that does not exist
        not_found_hall = controller.search_hall("Nonexistent Hall")
        # Check that no hall is found
        assert not_found_hall is None

    def test_search_screening_by_id(self):
        movie = Movie("Movie Title", "English", "Action", "2023-10-30")
        hall = CinemaHall("Hall A", 100)
        screening = Screening("2023-10-30", "13:00", "15:30", hall)
        movie.add_screening(screening)
        # Search for the screening by ID
        found_screening = controller.search_screening_by_id(movie, screening.screeningID)
        # Check if the correct screening is found
        assert found_screening is not None
        assert found_screening == screening
        # Try searching for a screening that does not exist
        not_found_screening = controller.search_screening_by_id(movie, 9999)
        # Check that no screening is found
        assert not_found_screening is None

    def test_make_booking(self):
        customer = Customer("customer1", "customer1@example.com", "password")
        movie = Movie("Movie 1", "English", "Action", datetime(2023, 10, 30))
        hall = None
        screening = Screening(date(2023, 10, 30), datetime(2023, 10, 30, 15, 0), datetime(2023, 10, 30, 17, 0), hall)
        seat1 = ScreeningSeat(1, 1, 10.0)
        seat2 = ScreeningSeat(1, 2, 10.0)
        payment = DebitCard(50.0, "1234567890", "Test Bank", "John Doe")
        # Make a booking
        booking = controller.make_booking(customer, movie, screening, [seat1, seat2], payment)
        assert booking is not None
        assert booking.customer == customer
        assert booking.movie == movie
        assert booking.screening == screening
        assert booking.bookingSeats == [seat1, seat2]
        assert booking.payment == payment
        assert booking.status == "Pending"
        assert customer.bookingList == [booking]

    def test_cancel_booking(self):
        customer = Customer("customer1", "customer1@example.com", "password")
        movie = Movie("Movie 1", "English", "Action", datetime(2023, 10, 30))
        hall = None
        screening = Screening(date(2023, 10, 30), datetime(2023, 10, 30, 15, 0), datetime(2023, 10, 30, 17, 0), hall)
        seat1 = ScreeningSeat(1, 1, 10.0)
        seat2 = ScreeningSeat(1, 2, 10.0)
        payment = DebitCard(50.0, "1234567890", "Test Bank", "John Doe")
        # Make a booking
        booking = controller.make_booking(customer, movie, screening, [seat1, seat2], payment)
        # Cancel the booking
        result = controller.cancel_booking(booking)
        assert result is True  # Booking should be successfully canceled
        assert booking.status == "Canceled"
        for seat in booking.bookingSeats:
            assert seat.booked is False

    def test_add_movie(self):
        admin = Admin("admin1", "admin1@example.com", "password")
        title = "Test Movie"
        language = "English"
        genre = "Action"
        release_date = datetime(2023, 11, 15)
        # Add a movie
        result = controller.add_movie(admin, title, language, genre, release_date)
        assert result is True  # Movie should be added successfully

    def test_add_screening(self):
        admin = Admin("admin1", "admin1@example.com", "password")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 11, 15))
        hall = CinemaHall("Hall A", 100)
        screening_date = date(2023, 11, 20)
        start_time = datetime(2023, 11, 20, 15, 0)
        end_time = datetime(2023, 11, 20, 17, 0)
        # Add a screening
        result = controller.add_screening(admin, movie, screening_date, start_time, end_time, hall)
        assert result is True  # Screening should be added successfully

    def test_cancel_movie(self):
        admin = Admin("admin1", "admin1@example.com", "password")
        movie = controller.search_movie_by_id(1000)   
        # Cancel a movie
        result = controller.cancel_movie(admin, movie)
        assert result is True  # Movie should be canceled successfully

    def test_cancel_screening(self):
        admin = Admin("admin1", "admin1@example.com", "password")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 11, 15))
        hall = CinemaHall("Hall A", 100)
        screening_date = date(2023, 11, 20)
        start_time = datetime(2023, 11, 20, 15, 0)
        end_time = datetime(2023, 11, 20, 17, 0)
        screening = Screening(screening_date, start_time, end_time, hall)
        movie.add_screening(screening)
        # Cancel a screening
        result = controller.cancel_screening(admin, movie, screening)
        assert result is True  # Screening should be canceled successfully
        assert screening not in movie.getScreeningList()

    def test_get_coupon_list(self):
        # Get the list of coupons
        coupon_list = controller.get_coupon_list()
        # Check if the correct coupons are in the list
        assert len(coupon_list) == 3

    def test_search_coupon(self):
        # Search for an existing coupon by couponID
        found_coupon = controller.search_coupon("COUPON001")
        # Check if the correct coupon is found
        assert found_coupon is not None
        # Search for a coupon that does not exist
        not_found_coupon = controller.search_coupon("9999")
        # Check that no coupon is found
        assert not_found_coupon is None

    def test_add_credit_card_payment(self):
        amount = 50.0
        credit_card_num = "1234567890123456"
        name_on_card = "John Doe"
        expiry_date = datetime(2023, 12, 31)
        cvv = "123"
        # Add a credit card payment
        credit_card_payment = controller.add_credit_card_payment(amount, credit_card_num, name_on_card, expiry_date, cvv)
        assert credit_card_payment is not None
        assert credit_card_payment.amount == amount
        assert credit_card_payment.creditCardNum == credit_card_num
        assert credit_card_payment.nameOnCard == name_on_card
        assert credit_card_payment.expiryDate == expiry_date
        assert credit_card_payment.cvv == cvv

    def test_add_debit_card_payment(self):
        amount = 50.0
        card_num = "9876543210123456"
        bank_name = "Sample Bank"
        name_on_card = "Jane Doe"
        # Add a debit card payment
        debit_card_payment = controller.add_debit_card_payment(amount, card_num, bank_name, name_on_card)
        assert debit_card_payment is not None
        assert debit_card_payment.amount == amount
        assert debit_card_payment.cardNum == card_num
        assert debit_card_payment.bankName == bank_name
        assert debit_card_payment.nameOnCard == name_on_card

    def test_add_cash_payment(self):
        amount = 100.0
        # Add a cash payment
        cash_payment = controller.add_cash_payment(amount)
        assert cash_payment is not None
        assert cash_payment.amount == amount

    def test_issue_refund(self):
        booking = Booking(None, None, None, None, None)
        booking.status = "Canceled"
        # Issue a refund for a canceled booking
        result = controller.issue_refund(booking)
        assert result is True
        assert booking.status == "Refunded"
        # Try to issue a refund for an already refunded booking
        result = controller.issue_refund(booking)
        assert result is False
        assert booking.status == "Refunded"

    def test_send_add_booking_notification(self):
        customer = Customer("user1", "user1@example.com", "password1")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 11, 15))
        screening = Screening(date(2023, 10, 30), datetime(2023, 10, 30, 15, 0), datetime(2023, 10, 30, 17, 0), None)
        booking = Booking(customer, movie, screening, [], None)
        # Send an "Add Booking" notification
        notification = controller.send_add_booking_notification(booking)
        # Check if the notification is added to the customer's notification list
        assert notification in customer.notificationList
        assert notification is not None

    def test_send_cancel_booking_notification(self):
        customer = Customer("user1", "user1@example.com", "password1")
        movie = Movie("Test Movie", "English", "Action", datetime(2023, 11, 15))
        screening = Screening(date(2023, 10, 30), datetime(2023, 10, 30, 15, 0), datetime(2023, 10, 30, 17, 0), None)
        booking = Booking(customer, movie, screening, [], None)
        # Send a "Cancel Booking" notification
        notification = controller.send_cancel_booking_notification(booking)
        # Check if the notification is added to the customer's notification list
        assert notification in customer.notificationList
        assert notification is not None
