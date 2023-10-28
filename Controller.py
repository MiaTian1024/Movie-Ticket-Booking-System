
# Import
from typing import List
from datetime import datetime, date
from Models import Guest, Customer, Admin, FrontDeskStaff, Movie, Screening, CinemaHall, Coupon, CreditCard, Payment, Booking, ScreeningSeat
from ReadFile import ReadFile

# Read files
file = ReadFile()
customer_obj = file.getCustomerObj("file/customer.txt")
movie_obj = file.getMovieObj("file/movies.txt")
admin_obj = file.getAdminObj("file/admin.txt")
staff_obj = file.getStaffObj("file/staff.txt")
hall_obj = file.getHallObj("file/hall.txt")
screening_obj = file.getScreeningObj("file/screening.txt")
coupon_obj = file.getCouponObj("file/coupon.txt")

# Get Hall 

# MovieTicketSystemController class handles user interactions and system operations.
class Controller:
    def __init__(self) -> None:
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
        if any(cust.__email == email for cust in self.__customers):
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
        # Logic for customer login
        for staff in self.__staffs:
            if staff.login(email, password):
                return staff
        return False
    
    def search_movie_by_id(self, id):
        for movie in self.__movies:
            if movie.movieID == id:
                return movie       
        return None
        
    def search_movie_by_title(self, title):
        results = []
        for movie in self.__movies:
            if movie.title == title:
                results.append(movie)
        return results
    
    def search_movie_by_lang(self, lang):
        results = []
        for movie in self.__movies:
            if movie.language == lang:
                results.append(movie)
        return results
    
    def search_movie_by_genre(self, genre):
        results = []
        for movie in self.__movies:
            if movie.genre == genre:
                results.append(movie)
        return results

    def search_movie_by_date(self, date):
        results = []
        for movie in self.__movies:
            if movie.releaseDate == date:
                results.append(movie)
        return results
    
    def get_movie_list(self):
        return self.__movies
    
    def get_customer_list(self):
        return self.__customers
    
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
        if movie.search_screening(screeningID):
            return movie.search_screening(screeningID)        
        return None

    def make_booking(self, customer: 'Customer', movie: 'Movie', screening: 'Screening', bookingSeats: List['ScreeningSeat'], payment: 'Payment', status: str = "Pending"):
        new_booking = Booking(customer, movie, screening, bookingSeats, payment)
        self.__bookings.append(new_booking)
        return new_booking

    def cancel_booking(self, booking: 'Booking') -> bool:
        if booking in self.__bookings:
            booking.status = "Canceled"
            for seat in booking.bookingSeats:
                seat.booked = False
            return True  # Booking canceled successfully
        else:
            return False  # Booking not found or already canceled

    def get_booking_list(self, customer: 'Customer'):
        booking_list = []
        for booking in self.__bookings:
            if booking.customer.email == customer.email:
                booking_list.append(booking)
        return booking_list
    
    def search_booking(self, bookingID: int):
        for booking in self.__bookings:
            if booking.bookingID == bookingID:
                return booking
        return None

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

    def cancel_movie(self, movie: 'Movie') -> bool:

        # Logic for canceling a movie
        pass

    def cancel_screening(self, screening: 'Screening') -> bool:
 
        # Logic for canceling a screening
        pass

    def search_seat(self, screening:'Screening', seatID):
        screening_hall = screening.hall
        list_of_seats = screening_hall.listOfSeats
        for seat in list_of_seats:
            if seat.seatID == seatID:
                return seat      
        return None

    def get_coupon_list(self) -> List['Coupon']:
        return self.__coupons
    
    def search_coupon(self, couponID):
        for coupon in self.__coupons:
            if coupon.couponID == couponID:
                return coupon      
        return None

    def add_credit_card_payment(self, amount: float, creditCardNum: str, nameOnCard: str, expiryDate: datetime, cvv: str):
        credit_card_payment = CreditCard(amount, creditCardNum, nameOnCard, expiryDate, cvv)
        self.__payments.append(credit_card_payment)
        return credit_card_payment

    def issue_refund(self, amount: float, refund_type: str) -> bool:
        #Method to issue a refund.
     
        pass

    def send_new_movie_notification(self, new_movie_notification: 'NewMovieNotification') -> bool:
        # Method to send a new movie notification.
     
        pass

    def send_new_booking_notification(self, new_booking_notification: 'NewBookingNotification') -> bool:
        # Method to send a new booking notification.
        
        pass

    def send_cancel_booking_notification(self, cancel_booking_notification: 'CancelBookingNotification') -> bool:
        # Method to send a cancel booking notification.
      
        pass

    


if __name__ == '__main__':
    controller = Controller()
    result = controller.register("hi","hi@gmail.com", "111")
    halls = controller.halls()
    screenings = controller.screenings()
    print(screenings)
    movie = controller.search_movie_by_id(1000)
    print(movie)
    screenings=movie.getScreeningList
    print(screenings)
    screening = controller.search_screening_by_id(100)
    print(screening)
 