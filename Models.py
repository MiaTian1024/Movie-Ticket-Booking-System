from abc import ABC, abstractmethod
from typing import List
from datetime import datetime, date

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
    def register(self, username: str, email: str, password: str):
        new_customer = Customer(username, email, password)  
        return new_customer  

class Movie:
    def __init__(self, title: str, language: str, genre: str, releaseDate: datetime) -> None:
        self.__title = title
        self.__language = language
        self.__genre = genre
        self.__releaseDate = releaseDate
        self.__screeningList: List['Screening'] = []

    def getScreeningList(self) -> List['Screening']:
        return self.__screeningList
    
    def add_screening(self, screening: 'Screening') -> bool:
        self.__screeningList.append(screening)
        pass
    
    def get_info(self) -> str:
        return f"Title: {self.__title}, Language: {self.__language}, Genre: {self.__genre}, Release Date: {self.__releaseDate}"

class Screening:
    def __init__(self, id: int, hall: 'Hall', date: date, startTime: datetime, endTime: datetime, screening_seats: List['ScreeningSeat']) -> None:
        self._id = id
        self._hall = hall
        self._date = date
        self._startTime = startTime
        self._endTime = endTime
        self._screening_seats = screening_seats
        self._booked_seats = List['ScreeningSeat'] =[]

    def get_screening_seats(self) -> List['ScreeningSeat']:
  
        return self._screening_seats
    
    def get_booked_seats(self) -> List['ScreeningSeat']:

        return self._booked_seats
    
    def get_available_seats(self) -> List['ScreeningSeat']:

        pass
