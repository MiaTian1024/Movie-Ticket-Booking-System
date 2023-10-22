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

    @property
    def title(self,):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def language(self,):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    @property
    def genre(self,):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def releaseDate(self,):
        return self.__releaseDate

    @releaseDate.setter
    def releaseDate(self, value):
        self.__releaseDate = value

    def getScreeningList(self) -> List['Screening']:
        return self.__screeningList
    
    def add_screening(self, screening: 'Screening') -> bool:
        self.__screeningList.append(screening)
        pass
    
    def get_info(self) -> str:
        return f"Title: {self.__title}, Language: {self.__language}, Genre: {self.__genre}, Release Date: {self.__releaseDate}"

class Screening:
    def __init__(self, screeningDate: date, startTime: datetime, endTime: datetime, hall: 'CinemaHall') -> None:
        self.__screeningDate = screeningDate
        self.__startTime = startTime
        self.__endTime = endTime
        self.__hall = hall

class Cinema:
    def __init__(self, name: str, total_halls: int) -> None:
        self._name = name
        self._total_halls = total_halls

class CinemaHall:
    def __init__(self, name: str, totalSeats: int):
        self.__name = name
        self.__totalSeats = totalSeats
        self.__listOfSeats: List['ScreeningSeat'] = []

class Seat(ABC):
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

class ScreeningSeat(Seat):  
    def __init__(self, row: int, column: int, price: float, booked: bool = False) -> None:
        super().__init__(row, column)
        self._price = price
        self._booked = booked

class Booking:
    def __init__(self, bookingNum: str, customer: 'Customer', numberOfSeats: int, createdOn: date, status: int, 
                 screening: 'Screening', screeningSeats: List['ScreeningSeat'], orderTotal: float, payment: 'Payment'):
        self.__bookingNum = bookingNum
        self.__customer = customer
        self.__numberOfSeats = numberOfSeats
        self.__createdOn = createdOn
        self.__status = status
        self.__screening = screening
        self.__screeningSeats = screeningSeats
        self.__orderTotal = orderTotal
        self.__payment = payment

    def sendNotification(self) -> 'Notification':
        pass

class Notification:
    def __init__(self, notificationID: int, createdOn: date, content: str):
        self.__notificationID = notificationID
        self.__createdOn = createdOn
        self.__content = content

class Payment(ABC):
    def __int__(self, amount: float, createdOn: datetime, paymentID: int):
        self.__amount = amount
        self.__createdOn = createdOn
        self.__paymentID = paymentID

    # Abstract method for all user class
    @abstractmethod
    def calcDiscount(self) -> float:
        pass

    @abstractmethod
    def calcFinalPayment(self) -> float:
        pass
    
class CreditCard(Payment):
    def __init__(self, amount: float, createdOn: datetime, paymentID: int, creditCardNum: str, cardType: str, expiryDate: datetime, nameOnCard: str):
        super().__init__(amount, createdOn, paymentID)
        self.__creditCardNum = creditCardNum
        self.__cardType = cardType
        self.__expiryDate = expiryDate
        self.__nameOnCard = nameOnCard

    def calcDiscount(self) -> float:
        pass

    def calcFinalPayment(self) -> float:
        pass

class DebitCard(Payment):
    def __init__(self, amount: float, createdOn: datetime, paymentID: int, cardNum: str, bankName: str, nameOnCard: str):
        super().__init__(amount, createdOn, paymentID)
        self.__cardNum = cardNum
        self.__bankName = bankName
        self.__nameOnCard = nameOnCard

    def calcDiscount(self) -> float:
        pass

    def calcFinalPayment(self) -> float:
        pass

class Coupon:
    def __init__(self, couponID: str, expiryDate: datetime, discount: float):
        self.__couponID = couponID
        self.__expiryDate = expiryDate
        self.__discount = discount
