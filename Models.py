from abc import ABC, abstractmethod
from typing import List
from datetime import datetime, date

# Base class for all system users
class User(ABC):
    # The abstract user class
    def __init__(self, username: str, email: str, password: str) -> None:   
        self.username = username
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

    def resetPassword(self, newPassword:str) -> bool:      
        self._password = newPassword
        return True

    def makeBooking(self, booking: 'Booking') -> bool:
        self.__bookingList.append(booking)
        return True

    def cancelBooking(self, booking: 'Booking') -> bool:    
        if booking in self.__bookingList:
            self.__bookingList.remove(booking)
            return True
        return False

    def getBookingList(self) -> List['Booking']:
        return self.__bookingList

# Admin class inherit from User class  
class Admin(User):
  
    def __init__(self, username: str, email: str, password: str) -> None:      
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:    
        return self._email == email and self._password == password

    def logout(self) -> bool:     
        return True

    def resetPassword(self, newPassword:str) -> bool:      
        self._password = newPassword
        return True

    def addMovie(self, title: str, language: str, genre: str, releaseDate: datetime):      
        return Movie(title, language, genre, releaseDate)

    def addScreening(self, screeningDate: date, startTime: datetime, endTime: datetime, hall: 'CinemaHall') -> bool:    
        return Screening(screeningDate, startTime, endTime, hall)

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

    def logout(self) -> bool:     
        return True

    def resetPassword(self, newPassword: str) -> bool:
        self._password = newPassword
        return True

    def makeBooking(self, booking: 'Booking') -> bool:    
        pass

    def cancelBooking(self, booking: 'Booking') -> bool:     
        pass


# class for Guest
class Guest():
    def register(self, username: str, email: str, password: str):
        return Customer(username, email, password)   

class Movie:
    nextID = 1000
    def __init__(self, title: str, language: str, genre: str, releaseDate: datetime) -> None:
        self.__movieID = Movie.nextID
        self.__title = title
        self.__language = language
        self.__genre = genre
        self.__releaseDate = releaseDate
        self.__screeningList: List['Screening'] = []
        Movie.nextID += 1

    @property
    def movieID(self,):
        return self.__movieID

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
        return True
    
    
    def get_info(self) -> str:
        return f"Title: {self.__title}, Language: {self.__language}, Genre: {self.__genre}, Release Date: {self.__releaseDate}"

class Screening:
    nextID = 100
    def __init__(self, screeningDate: date, startTime: datetime, endTime: datetime, hall: 'CinemaHall') -> None:
        self.__screeningID = Screening.nextID
        self.__screeningDate = screeningDate
        self.__startTime = startTime
        self.__endTime = endTime
        self.__hall = hall
        Screening.nextID += 1

    @property
    def screeningID(self):
        return self.__screeningID

    @property
    def screeningDate(self):
        return self.__screeningDate
    
    @property
    def startTime(self):
        return self.__startTime
    
    @property
    def endTime(self):
        return self.__endTime
    
    def hall(self):
        return self.__hall

class CinemaHall:
    def __init__(self, name: str, totalSeats: int):
        self.__name = name
        self.__totalSeats = totalSeats
        self.__listOfSeats: List['ScreeningSeat'] = []

    @property
    def name(self):
        return self.__name
    
    @property
    def totalSeats(self):
        return self.__totalSeats
    
    def listOfSeats(self):
        return self.__listOfSeats
    
class ScreeningSeat():  
    def __init__(self, row: int, column: int, price: float, booked: bool = False) -> None:
        self.row = row
        self.column = column
        self.price = price
        self.booked = booked

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
    def __int__(self,  paymentID: int, amount: float, createdOn: datetime):
        self.__paymentID = paymentID
        self.__amount = amount
        self.__createdOn = createdOn
        

    # Abstract method for all user class
    @abstractmethod
    def calcDiscount(self) -> float:
        pass

    @abstractmethod
    def calcFinalPayment(self) -> float:
        pass
    
class CreditCard(Payment):
    def __init__(self, paymentID: int, amount: float, createdOn: datetime, creditCardNum: str, cardType: str, expiryDate: datetime, nameOnCard: str):
        super().__init__(paymentID, amount, createdOn)
        self.__creditCardNum = creditCardNum
        self.__cardType = cardType
        self.__expiryDate = expiryDate
        self.__nameOnCard = nameOnCard

    def calcDiscount(self) -> float:
        pass

    def calcFinalPayment(self) -> float:
        pass

class DebitCard(Payment):
    def __init__(self, paymentID: int, amount: float, createdOn: datetime, cardNum: str, bankName: str, nameOnCard: str):
        super().__init__(paymentID, amount, createdOn)
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
