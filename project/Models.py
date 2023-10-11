"""! Model class of User and Guest"""

from abc import ABC, abstractmethod
from typing import List

class Person(ABC):
    def __init__(self, name: str, address: str, email: str, phone: str) -> None:
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone

# Base class for all system users
class User(ABC):
    """! The Abstract User class"""
    def __init__(self, username: str, password: str) -> None:
        """! Initialize an abstrict User object with the provided details.
        @param name (str): The name of the user.
        @param email (str): The email address of the user.
        @param password (str): The password of the user.
        """
        ## This is the username of the user
        self._username = username
        ## This is the password of the user
        self._password = password

    # Abstract method for all user class
    @abstractmethod
    def login(self, email: str, password:str) -> bool:
        """! Abstract method for all users to login to the system
        @param email (str): The email address to login to the system.
        @param password (str): The password to login to the system.
        @return A boolean to indicate whether the user login was successful or not.
        """
        pass

    @abstractmethod
    def logout(self, email: str, password:str) -> bool:
        """! Abstract method for all users to login to the system
        @param email (str): The email address to login to the system.
        @param password (str): The password to login to the system.
        @return A boolean to indicate whether the user login was successful or not.
        """
        pass

    @abstractmethod
    def resetPassword(self, email: str, password:str) -> bool:
        """! Abstract method for all users to login to the system
        @param email (str): The email address to login to the system.
        @param password (str): The password to login to the system.
        @return A boolean to indicate whether the user login was successful or not.
        """
        pass


# Customer class inherit from User class
class Customer(User):
    """! The Customer class inherit from User class"""
    def __init__(self, username: str, email: str, password: str) -> None:
       
        super().__init__(username, email, password)
        self.__bookingList: List['Booking'] = []
        self.__notificationList: List['Notification'] =[]

    def login(self, email: str, password:str) -> bool:
       
        pass

    def logout(self, email: str, password:str) -> bool:
      
        pass

    def resetPassword(self, email: str, password:str) -> bool:
       
        pass

    def makeBooking(self, booking: 'Booking') -> bool:
        """!  Make a booking and add it to the customer's bookings.
        @param booking (Booking): The booking to make.
        @return A boolean to indicate whether the booking was successful made or not.
        """
        pass

    def cancelBooking(self, booking: 'Booking') -> bool:
        """! Cancel the customer's booking.
        @param booking (Booking): The booking to cancel.
        @return A boolean to indicate whether the booking was successful canceled or not.
        """
        # Logic for canceling a booking
        pass

    def getBookingList(self) -> List['Booking']:
        pass

# Admin class inherit from User class  
class Admin(User):
    """! The Admin class inherit from User class"""
    def __init__(self, username: str, email: str, password: str) -> None:
        """! Initialize an Admin object with the provided details.
        @param username (str): The username of the admin.
        @param email (str): The email address of the admin.
        @param password (str): The password of the admin.
        """
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:
        """! Login method for admin to login to the system
        @param email (str): The email address to login to the system.
        @param password (str): The password to login to the system.
        @return A boolean to indicate whether the admin login was successful or not.
        """
        pass

    def add_movie(self, movie: 'Movie') -> bool:
        """! Add a new movie to the system.
        @param movie (Movie): The movie to add.
        @return A boolean to indicate whether the movie was successful added or not.
        """
        # Logic for adding a new movie
        pass

    def add_screening(self, screening: 'Screening') -> bool:
        """! Add a screening for a movie.
        @param screening (Screening): The screening to add.
        @return A boolean to indicate whether the screening was successful added or not.
        """
        # Logic for adding a screening
        pass

    def cancel_movie(self, movie: 'Movie') -> bool:
        """! Cancel a movie from the system.
        @param movie (Movie): The movie to cancel.
        @return A boolean to indicate whether the movie was successful canceled or not.
        """
        # Logic for canceling a movie
        pass

    def cancel_screening(self, screening: 'Screening') -> bool:
        """! Cancel a screening for a movie.
        @param screening (Screening): The screening to cancel.
        @return A boolean to indicate whether the screening was successful canceled or not.
        """
        # Logic for canceling a screening
        pass


# FrontDeskStaff class inherit from User class
class FrontDeskStaff(User):
    """! The FrontDeskStaff class inherit from User class"""
    def __init__(self, username: str, email: str, password: str) -> None:
        """! Initialize a Front Desk Staff object with the provided details.
        @param username (str): The username of the staff.
        @param email (str): The email address of the staff.
        @param password (str): The password of the staff.
        """
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:
        """! Login method for staff to login to the system
        @param email (str): The email address to login to the system.
        @param password (str): The password to login to the system.
        @return A boolean to indicate whether the staff login was successful or not.
        """
        pass

    def make_booking(self, booking: 'Booking') -> bool:
        """! Make a booking on behalf of a customer.
        @param booking (Booking): The booking to make.
        @return A boolean to indicate whether the booking was successful made or not.
        """
        # Logic for making a booking
        pass

    def cancel_booking(self, booking: 'Booking') -> bool:
        """! Cancel a customer's booking.
        @param booking (Booking): The booking to cancel.
        @return A boolean to indicate whether the booking was successful canceled or not.
        """
        # Logic for canceling a booking
        pass


# class for Guest
class Guest():
    """! The Guest class"""
    def register(self, username: str, email: str, password: str) -> bool:
        """! Method for guest to register as a customer
        @param username (str): The username to register.
        @param email (str): The email address to register.
        @param password (str): The password to register.
        @return A boolean to indicate whether the register was successful or not.
        """
        pass


