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

# Sample test cases for the Controller class
class TestController:
    def test_register_customer(self):
        controller = Controller()
        assert controller.register("testuser", "testuser@example.com", "password123") == True

    def test_duplicate_customer_registration(self):
        controller = Controller()
        controller.register("testuser", "testuser@example.com", "password123")
        assert controller.register("testuser", "testuser@example.com", "password123") == False

    def test_customer_login(self):
        controller = Controller()
        assert controller.customer_login("brain@gmail.com", "111") != False

    def test_invalid_customer_login(self):
        controller = Controller()
        assert controller.customer_login("testuser@example.com", "wrongpassword") == False

    def test_admin_login(self):
        controller = Controller()
        assert controller.admin_login("amy@gmail.com", "111") != False

    def test_invalid_admin_login(self):
        controller = Controller()
        assert controller.admin_login("admin@example.com", "wrongpassword") == False

    def test_staff_login(self):
        controller = Controller()
        assert controller.staff_login("joe@gmail.com", "111") != False

    def test_invalid_staff_login(self):
        controller = Controller()
        assert controller.staff_login("staff@example.com", "wrongpassword") == False


# Run tests using pytest
# Command: pytest -v test_controller.py
