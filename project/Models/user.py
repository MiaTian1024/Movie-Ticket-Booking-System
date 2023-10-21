from abc import ABC, abstractmethod
from typing import List


# Base class for all system users
class User(ABC):
    # The abstract user class
    def __init__(self, username: str, email: str, password: str) -> None:   
        self._username = username
        self._email = email
        self._password = password

    # Abstract method for all user class
    @abstractmethod
    def login(self, email: str, password:str) -> bool:
        return self._email == email and self._password == password

    @abstractmethod
    def logout(self) -> bool:
        return True

    @abstractmethod
    def resetPassword(self, newPassword:str) -> bool:
        self._password = newPassword
        return True

# Customer class inherit from User class
class Customer(User):
    def __init__(self, username: str, email: str, password: str) -> None: 
        super().__init__(username, email, password)
        self.__bookingList: List['Booking'] = []
        self.__notificationList: List['Notification'] =[]

    def login(self, email: str, password:str) -> bool:  
        return self._email == email and self._password == password

    def logout(self, email: str, password:str) -> bool:     
        return True

    def resetPassword(self, email: str, password:str) -> bool:      
        pass

    def makeBooking(self, booking: 'Booking') -> bool:
        pass

    def cancelBooking(self, booking: 'Booking') -> bool:    
        pass

    def getBookingList(self) -> List['Booking']:
        pass

# Admin class inherit from User class  
class Admin(User):
  
    def __init__(self, username: str, email: str, password: str) -> None:      
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:    
        return self._email == email and self._password == password

    def logout(self, email: str, password:str) -> bool:     
        return True

    def resetPassword(self, email: str, password:str) -> bool:      
        pass

    def addMovie(self, movie: 'Movie') -> bool:      
        pass

    def addScreening(self, screening: 'Screening') -> bool:    
        pass

    def cancelMovie(self, movie: 'Movie') -> bool:        
        pass

    def cancelScreening(self, screening: 'Screening') -> bool:    
        pass


# FrontDeskStaff class inherit from User class
class FrontDeskStaff(User):
    def __init__(self, username: str, email: str, password: str) -> None:     
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:    
        return self._email == email and self._password == password

    def logout(self, email: str, password:str) -> bool:     
        return True

    def resetPassword(self, email: str, password:str) -> bool:      
        pass

    def makeBooking(self, booking: 'Booking') -> bool:    
        pass

    def cancelBooking(self, booking: 'Booking') -> bool:     
        pass


# class for Guest
class Guest():
    def __init__(self):
        self.__customers: List['Customer'] = []

    def register(self, username: str, email: str, password: str) -> bool:
        # Check if the email is already in use
        if any(cust._email == email for cust in self.__customers):
            return False  # Email is already registered

        # If the email is not in use, create a new customer and add it to the list of customers
        customer = Customer(username, email, password)
        self.__customers.append(customer)
        return True  # Registration successful


