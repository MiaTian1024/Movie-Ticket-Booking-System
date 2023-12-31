# Author: Mia Tian (ID: 1154238)
# Login information for demonstration purposes only:
# - Admin: Email: amy@gmail.com, Password: 111
# - Front Desk Staff: Email: joe@gmail.com, Password: 111
# - Customer: Email: brain@gmail.com, Password: 111


# Import necessary modules
from typing import List
from datetime import datetime, date
from Models import Guest, Customer, Admin, FrontDeskStaff, Movie, Screening, CinemaHall, Coupon, CreditCard, Payment, Booking, ScreeningSeat, DebitCard, Cash
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


# Controller class handles user interactions and system operations.
class Controller:
    def __init__(self) -> None:
        # Initialize the system with data read from files
        self.__halls: List['CinemaHall'] = hall_obj
        self.__screenings: List['Screening'] = screening_obj
        self.__movies: List['Movie'] = movie_obj
        self.__customers: List['Customer'] = customer_obj
        self.__admins: List['Admin'] = admin_obj
        self.__staffs: List['FrontDeskStaff'] = staff_obj
        self.__coupons: List['Coupon'] = coupon_obj
        self.__payments: List['Payment'] = []
        self.__bookings: List['Booking'] = []
              
    def register(self, username: str, email: str, password: str) -> bool:
        # Check if the email is already in use
        if any(cust.email == email for cust in self.__customers):
            return False  # Email is already registered
        # If the email is not in use, create a new customer and add it to the list of customers
        guest = Guest()
        new_customer = guest.register(username, email, password)
        self.__customers.append(new_customer)
        return True

    def customer_login(self, email: str, password:str): 
        # Logic for customer login
        for customer in self.__customers:
            if customer.login(email, password):
                return customer
        return False
    
    def admin_login(self, email: str, password:str) -> bool: 
        # Logic for admin login
        for admin in self.__admins:
            if admin.login(email, password):
                return admin
        return False
    
    def staff_login(self, email: str, password:str) -> bool: 
        # Logic for staff login
        for staff in self.__staffs:
            if staff.login(email, password):
                return staff
        return False
    
    # Methods for searching movies
    def search_movie_by_id(self, id):
        for movie in self.__movies:
            if movie.movieID == id:
                return movie       
        return None
        
    def search_movie_by_title(self, title):
        results = []  # Initialize an empty list to store matching movies
        for movie in self.__movies:  
            if movie.title == title:   # Check if the movie's title matches the specified title
                results.append(movie)  # Add the matching movie to the results list
        return results   # Return the list of matching movies
    
    def search_movie_by_lang(self, lang):
        results = []  # Initialize an empty list to store matching movies
        for movie in self.__movies:
            if movie.language == lang:  # Check if the movie's title matches the specified language
                results.append(movie)  # Add the matching movie to the results list
        return results  # Return the list of matching movies
    
    def search_movie_by_genre(self, genre):
        results = []
        for movie in self.__movies:
            if movie.genre == genre:  # Check if the movie's title matches the specified genre
                results.append(movie)  # Add the matching movie to the results list
        return results  # Return the list of matching movies

    def search_movie_by_date(self, date):
        results = []
        for movie in self.__movies:
            if movie.releaseDate == date:   # Check if the movie's title matches the specified date
                results.append(movie)  # Add the matching movie to the results list
        return results  # Return the list of matching movies
    
    def get_movie_list(self):
        return self.__movies
    
    def get_customer_list(self):
        return self.__customers
    
    def get_booking_list(self):
        return self.__bookings
    
    def search_customer(self, customerEmail):
        for customer in self.__customers:
            if customer.email == customerEmail:
                return customer      
        return None
    
    def search_hall(self, hallName):
        for hall in self.__halls:
            if hall.name == hallName:
                return hall      
        return None
    
    def search_screening_by_id(self, movie: 'Movie', screeningID):
         # Check if the specified movie has a screening with the given ID
        if movie.search_screening(screeningID):   
            return movie.search_screening(screeningID)   # Return the matching screening   
        return None  # Return None if the screening is not found in the specified movie

    # Methods for creating bookings, canceling bookings, and handling notifications
    def make_booking(self, customer: 'Customer', movie: 'Movie', screening: 'Screening', bookingSeats: List['ScreeningSeat'], payment: 'Payment', status: str = "Pending"):
        new_booking = Booking(customer, movie, screening, bookingSeats, payment)  # Create a new booking
        self.__bookings.append(new_booking)  # Add the booking to the system's list of bookings
        customer.bookingList.append(new_booking)   # Add the booking to the customer's booking list
        return new_booking  # Return the newly created booking

    def cancel_booking(self, booking: 'Booking') -> bool:
        if booking in self.__bookings:  # Check if the booking is in the system's list of bookings
            booking.status = "Canceled"   # Set the status of the booking to "Canceled"
            for seat in booking.bookingSeats:
                seat.booked = False     # Mark the booked seats as available
            return True  # Booking canceled successfully
        else:
            return False   # Booking not found or already canceled; cancellation failed

    def get_booking_list_for_customer(self, customer: 'Customer'):
        booking_list = []  # Initialize an empty list to store bookings
        for booking in self.__bookings:
            if booking.customer.email == customer.email:
                 # Check if the booking's customer email matches the specified customer's email
                booking_list.append(booking)  # Add the booking to the list
        return booking_list  # Return the list of bookings for the customer
    
    def search_booking(self, bookingID: int):
        for booking in self.__bookings:  
            if booking.bookingID == bookingID:  # Check if the booking's ID matches the specified ID
                return booking  # Return the matching booking
        return None  # Return None if the booking is not found

    def add_movie(self, admin: 'Admin', title: str, language: str, genre: str, releaseDate: datetime) -> bool:  
        new_movie = admin.addMovie(title, language, genre, releaseDate)
        if new_movie not in self.__movies:
            self.__movies.append(new_movie)
            return True
        return False # Movie already exists
       
    def add_screening(self, admin: 'Admin', movie: 'Movie', screeningDate: date, startTime: datetime, endTime: datetime, hall: 'CinemaHall') -> bool:
        new_screening = admin.addScreening(screeningDate, startTime, endTime, hall)
        self.__screenings.append(new_screening)
        if new_screening not in movie.getScreeningList():
            movie.add_screening(new_screening)
            return True
        return False # Screening already exists

    def cancel_movie(self, admin: 'Admin', movie: 'Movie') -> bool:
        canceled_movie = admin.cancelMovie(movie)  # Cancel the specified movie
        if canceled_movie in self.__movies:  # Check if the canceled movie is in the system's list of movies
            self.__movies.remove(canceled_movie)  # Remove the canceled movie from the system
            return True
        return False  # Movie not found in the system

    def cancel_screening(self, admin: 'Admin', movie: 'Movie', screening: 'Screening') -> bool:
        canceled_screening = admin.cancelScreening(screening)  # Cancel the specified screening
        screeningList = movie.getScreeningList()   # Get the list of screenings for the specified movie
        if canceled_screening in screeningList:  # Check if the canceled screening is in the movie's list of screenings
            screeningList.remove(canceled_screening)   # Remove the canceled screening from the movie
            return True
        return False   # Screening not found for the movie

    def search_seat(self, screening:'Screening', seatID):
        screening_hall = screening.hall  # Get the cinema hall associated with the screening
        list_of_seats = screening_hall.listOfSeats  # Get the list of seats in the cinema hall
        for seat in list_of_seats:
            if seat.seatID == seatID:  # Check if the seat's ID matches the specified seatID
                return seat       # Return the matching seat 
        return None   # Return None if the seat is not found in the screening

    def get_coupon_list(self) -> List['Coupon']:
        return self.__coupons
    
    def search_coupon(self, couponID):
        for coupon in self.__coupons:
            if coupon.couponID == couponID:
                return coupon      
        return None

    def add_credit_card_payment(self, amount: float, creditCardNum: str, nameOnCard: str, expiryDate: datetime, cvv: str):
        # Create a Credit Card payment
        credit_card_payment = CreditCard(amount, creditCardNum, nameOnCard, expiryDate, cvv)
        self.__payments.append(credit_card_payment)  # Add the payment to the system's list of payments
        return credit_card_payment  # Return the newly added Credit Card payment
    
    def add_debit_card_payment(self, amount: float, cardNum: str, bankName: str, nameOnCard: str):
        # Create a Debit Card payment
        debit_card_payment = DebitCard(amount, cardNum, bankName, nameOnCard)
        self.__payments.append(debit_card_payment)
        return debit_card_payment  # Return the newly added Debit Card payment
    
    def add_cash_payment(self, amount: float):
        # Create a Cash payment
        cash_payment = Cash(amount)
        self.__payments.append(cash_payment)
        return cash_payment   # Return the newly added Cash payment

    def issue_refund(self, booking: ['Booking']) -> bool:
        # Check if the booking is canceled and has not been refunded yet
        if booking.status == 'Canceled' and not booking.status == 'Refunded':
            booking.status = 'Refunded'    # Set the booking status to 'Refunded'
            return True     # Refund issued successfully
        else:
            return False    # Refund not issued, as the booking doesn't meet the refund criteria

    def send_add_booking_notification(self, booking: 'Booking'):
        notification = booking.sendAddBookingNotification()  # Create an 'Add Booking' notification
        notification_list = booking.customer.notificationList  # Get the customer's notification list
        if notification not in notification_list: 
            notification_list.append(notification)
            return notification    # Return the sent notification
        else:
            return None     # Notification already exists in the customer's list
    
    def send_cancel_booking_notification(self, booking: 'Booking'):
        notification = booking.sendCancelBookingNotification()    # Create a 'Cancel Booking' notification
        notification_list = booking.customer.notificationList    # Get the customer's notification list
        if notification not in notification_list:
            notification_list.append(notification)
            return notification    # Return the sent notification
        else:
            return None    # Notification already exists in the customer's list
     

 