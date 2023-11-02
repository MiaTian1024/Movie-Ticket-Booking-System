from abc import ABC, abstractmethod
from typing import List
from datetime import datetime, date

# Base class for all system users
class User(ABC):
    # The abstract user class
    def __init__(self, username: str, email: str, password: str) -> None:   
        self.__username = username  # Private username
        self.__email = email  # Private email
        self.__password = password  # Private password

    @property
    def username(self,):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def email(self,):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self,):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    # Abstract method for all user classes
    @abstractmethod
    def login(self, email: str, password:str) -> bool:
        return self.__email == email and self.__password == password

    @abstractmethod
    def logout(self) -> bool:
        return True

    @abstractmethod
    def resetPassword(self, newPassword:str) -> bool:
        self.__password = newPassword
        return True


# Customer class inherit from User class
class Customer(User):
    def __init__(self, username: str, email: str, password: str) -> None: 
        super().__init__(username, email, password)
        self.__bookingList: List['Booking'] = []    # Initialize an empty list to store bookings
        self.__notificationList: List['Notification'] =[]    # Initialize an empty list to store notifications

    @property
    def bookingList(self,):
        return self.__bookingList

    @bookingList.setter
    def bookingList(self, value):
        self.__bookingList = value

    @property
    def notificationList(self,):
        return self.__notificationList

    @notificationList.setter
    def notificationList(self, value):
        self.__notificationList = value

    def login(self, email: str, password:str) -> bool:  
        return self.email == email and self.password == password

    def logout(self) -> bool:     
        return True

    def resetPassword(self, newPassword:str) -> bool:      
        self.password = newPassword
        return True

    def makeBooking(self, booking: 'Booking') -> bool:
        if booking not in self.__bookingList:    # Check if the booking is in the list
            self.__bookingList.append(booking)    # Append the booking to the list
            return True    # Return True to indicate a successful booking
        return False    # Return False if the booking was already in the list

    def cancelBooking(self, booking: 'Booking') -> bool:    
        if booking in self.__bookingList:    # Check if the booking is in the list
            self.__bookingList.remove(booking)    # Remove the booking from the list
            return True    # Return True to indicate a successful cancellation
        return False    # Return False if the booking was not found in the list

    def getBookingList(self) -> List['Booking']:
        return self.__bookingList
    

# Admin class inherit from User class  
class Admin(User): 
    def __init__(self, username: str, email: str, password: str) -> None:      
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:    
        return self.email == email and self.password == password

    def logout(self) -> bool:     
        return True

    def resetPassword(self, newPassword:str) -> bool:      
        self.password = newPassword
        return True

    def addMovie(self, title: str, language: str, genre: str, releaseDate: datetime): 
        # addMovie logic in controller class     
        return Movie(title, language, genre, releaseDate)

    def addScreening(self, screeningDate: date, startTime: datetime, endTime: datetime, hall: 'CinemaHall'): 
        # addScreening logic in controller class   
        return Screening(screeningDate, startTime, endTime, hall)

    def cancelMovie(self, movie: 'Movie'): 
        # cancleMovie logic in controller class       
        return movie

    def cancelScreening(self, screening: 'Screening'):    
        # cancelScreening logic in controller class
        return screening


# FrontDeskStaff class inherit from User class
class FrontDeskStaff(User):
    def __init__(self, username: str, email: str, password: str) -> None:     
        super().__init__(username, email, password)

    def login(self, email: str, password:str) -> bool:    
        return self.email == email and self.password == password

    def logout(self) -> bool:     
        return True

    def resetPassword(self, newPassword: str) -> bool:
        self.password = newPassword
        return True

    def makeBooking(self, booking: 'Booking') -> bool:   
        # makeBooking logic in controller class 
        pass

    def cancelBooking(self, booking: 'Booking') -> bool:  
        # cancleBooking logic in controller class   
        pass


# class for Guest
class Guest():
    def register(self, username: str, email: str, password: str):
        return Customer(username, email, password)   


# Movie class represents a movie
class Movie:
    nextID = 1000  # Class variable to track the next available ID
    def __init__(self, title: str, language: str, genre: str, releaseDate: datetime) -> None:
        self.__movieID = Movie.nextID  # Assign a unique movie ID
        self.__title = title  # set the movie title
        self.__language = language # set the movie language
        self.__genre = genre  # set the movie genre
        self.__releaseDate = releaseDate  # set the movie release date
        self.__screeningList: List['Screening'] = []  # Initialize an empty list to store screenings
        Movie.nextID += 1  # Increment the next available ID for the next movie

    @property
    def movieID(self,):
        return self.__movieID
    
    @movieID.setter
    def movieID(self, value):
        self.__movieID = value

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
        # method of getting screening list for this movie
        return self.__screeningList
    
    def add_screening(self, screening: 'Screening') -> bool:
        # Check if the screening already exists in the list
        if screening in self.__screeningList:
            return False  # Return False to indicate that it's a duplicate and not added
        else:
            self.__screeningList.append(screening)  # Append the screening to the list
            return True  # Return True to indicate a successful addition
    
    def search_screening(self, screeningID):
        # method of searching screening by Id
        for screening in self.__screeningList:
            if screening.screeningID == screeningID:  # Check if the screening's ID matches the specified ID
                return screening  # Return the found screening
        return None  # Return None if the screening with the specified ID was not found
    

# Screening class represents a movie screening
class Screening:
    nextID = 100  # Class variable to track the next available ID
    def __init__(self, screeningDate: date, startTime: datetime, endTime: datetime, hall: 'CinemaHall') -> None:
        self.__screeningID = Screening.nextID  # Assign a unique screening ID
        self.__screeningDate = screeningDate  # Set the screening date
        self.__startTime = startTime   # Set the start time
        self.__endTime = endTime  # Set the end time
        self.__hall = hall  # Set the cinema hall for the screening
        Screening.nextID += 1  # Increment the next available ID for the next screening

    @property
    def screeningID(self):
        return self.__screeningID

    @property
    def screeningDate(self):
        return self.__screeningDate
    
    @screeningDate.setter
    def screeningDate(self, value):
        self.__screeningDate = value
    
    @property
    def startTime(self):
        return self.__startTime
    
    @startTime.setter
    def startTime(self, value):
        self.__startTime = value
    
    @property
    def endTime(self):
        return self.__endTime
    
    @endTime.setter
    def endTime(self, value):
        self.__endTime = value
    
    @property
    def hall(self):
        return self.__hall
    
    @hall.setter
    def hall(self, value):
        self.__hall = value


# CinemaHall class represents a cinema hall
class CinemaHall:
    def __init__(self, name: str, totalSeats: int):
        self.__name = name  # Set the name of the cinema hall
        self.__totalSeats = totalSeats   # Set the total number of seats
        self.__listOfSeats: List['ScreeningSeat'] = []  # Initialize a list to store screening seats in this hall

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def totalSeats(self):
        return self.__totalSeats
    
    @totalSeats.setter
    def totalSeats(self, value):
        self.__totalSeats = value
    
    @property
    def listOfSeats(self,):
        return self.__listOfSeats

    @listOfSeats.setter
    def listOfSeats(self, value):
        self.__listOfSeats = value


# ScreeningSeat class represents a seat in a cinema hall  
class ScreeningSeat():
    nextID = 100  # Class variable to track the next available seat ID
    def __init__(self, row: int, column: int, price: float, booked: bool = False) -> None:
        self.__seatID = ScreeningSeat.nextID  # Assign a unique seat ID
        self.__row = row  # Set the row number of the seat
        self.__column = column  # Set the column number of the seat
        self.__price = price   # Set the price of the seat
        self.__booked = booked  # Set the booking status of the seat
        ScreeningSeat.nextID += 1   # Increment the next available seat ID for the next seat

    @property
    def seatID(self,):
        return self.__seatID

    @property
    def row(self,):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value

    @property
    def column(self,):
        return self.__column

    @column.setter
    def column(self, value):
        self.__column = value

    @property
    def price(self,):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def booked(self,):
        return self.__booked

    @booked.setter
    def booked(self, value):
        self.__booked = value


# Booking class represents a booking made by a customer
class Booking:
    nextID = 10000   # Class variable to track the next available booking ID
    def __init__(self, customer: 'Customer', movie: 'Movie', screening: 'Screening', bookingSeats: List['ScreeningSeat'], payment: 'Payment', status: str = "Pending"):
        self.__bookingID = Booking.nextID  # Assign a unique booking ID
        self.__movie = movie  # Set the movie for the booking
        self.__customer = customer   # Set the customer making the booking
        self.__screening = screening  # Set the screening for the movie
        self.__bookingSeats = bookingSeats  # Set the booked seats
        self.__payment = payment  # Set the payment information
        self.__createdOn = datetime.now()   # Record the booking creation timestamp
        self.__status = status  # Set the status of the booking
        Booking.nextID += 1  # Increment the next available booking ID for the next booking

    @property
    def bookingID(self,):
        return self.__bookingID

    @property
    def movie(self,):
        return self.__movie

    @movie.setter
    def movie(self, value):
        self.__movie = value

    @property
    def screening(self,):
        return self.__screening

    @screening.setter
    def screening(self, value):
        self.__screening = value

    @property
    def customer(self,):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def bookingSeats(self,):
        return self.__bookingSeats

    @bookingSeats.setter
    def bookingSeats(self, value):
        self.__bookingSeats = value

    @property
    def payment(self,):
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    @property
    def status(self,):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def createdOn(self,):
        return self.__createdOn
 
    def sendAddBookingNotification(self) -> 'Notification':
        # Compose the content of the notification
        content = f"Booking details:\n Movie: {self.movie.title}\nScreening Date: {self.screening.screeningDate}\nCustomer: {self.customer.username}"
        return Notification(content)   # Create a new Notification instance with the content
    
    def sendCancelBookingNotification(self) -> 'Notification':
        # Compose the content of the notification
        content = f"Canceling details:\n Movie: {self.movie.title}\nScreening Date: {self.screening.screeningDate}\nCustomer: {self.customer.username}"
        return Notification(content)  # Create a new Notification instance with the content


# Notification class represents a notification sent to users
class Notification:
    nextID = 1000  # Class variable to track the next available notification ID
    def __init__(self, content: str):
        self.__notificationID = Notification.nextID  # Assign a unique notification ID
        self.__createdOn = datetime.now()  # Record the notification creation timestamp
        self.__content = content  # Set the content of the notification
        Notification.nextID += 1  # Increment the next available notification ID for the next notification

    @property
    def notificationID(self,):
        return self.__notificationID
    
    @notificationID.setter
    def notificationID(self, value):
        self.__notificationID = value

    @property
    def content(self,):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    @property
    def createdOn(self,):
        return self.__createdOn
    
    @createdOn.setter
    def createdOn(self, value):
        self.__createdOn = value


# Payment is an abstract base class for various payment methods
class Payment(ABC):
    nextID = 10000  # Class variable to track the next available payment ID
    def __init__(self, amount: float):   
        self.__paymentID = Screening.nextID  # Assign a unique payment ID
        self.__amount = float(amount)  # Set the payment amount
        self.__createdOn = datetime.now()  # Record the payment creation timestamp
        Screening.nextID += 1  # Increment the next available payment ID for the next payment

    @property
    def paymentID(self,):
        return self.__paymentID

    @property
    def amount(self,):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def createdOn(self,):
        return self.__createdOn
        
    # Abstract methods for calculating discounts and final payment
    @abstractmethod
    def calcDiscount(self, coupon:'Coupon') -> float:
        today = datetime.today().date()
        expiry_date = datetime.strptime(coupon.expiryDate, '%Y-%m-%d').date()
        if expiry_date > today:
            return coupon.discount  # Return the coupon's discount percentage
        else:
            return 0  # Coupon has no effect

    @abstractmethod
    def calcFinalPayment(self, coupon: 'Coupon' = None) -> float:
        if coupon:
            discount = self.calcDiscount(coupon)   # Calculate the discount using the calcDiscount method
            final_amount = float(self.amount) - (float(self.amount) * float(discount)) / 100   # Apply the discount
            return final_amount  # Return the final payment amount with the discount applied
        return self.amount   # If no coupon is provided, return the original payment amount


# CreditCard is a type of Payment
class CreditCard(Payment):
    def __init__(self, amount: float, creditCardNum: str, nameOnCard: str, expiryDate: datetime, cvv: str):
        super().__init__(amount)  # Call the constructor of the base class (Payment)
        self.__creditCardNum = creditCardNum     # Call the constructor of the base class (Payment)  
        self.__nameOnCard = nameOnCard  # Set the name on the credit card
        self.__expiryDate = expiryDate  # Set the credit card's expiry date
        self.__cvv = cvv  # Set the Card Verification Value (CVV) of the credit card

    @property
    def creditCardNum(self,):
        return self.__creditCardNum

    @creditCardNum.setter
    def creditCardNum(self, value):
        self.__creditCardNum = value

    @property
    def cvv(self,):
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    @property
    def expiryDate(self,):
        return self.__expiryDate

    @expiryDate.setter
    def expiryDate(self, value):
        self.__expiryDate = value

    @property
    def nameOnCard(self,):
        return self.__nameOnCard

    @nameOnCard.setter
    def nameOnCard(self, value):
        self.__nameOnCard = value

    def calcDiscount(self, coupon:'Coupon') -> float:
        if coupon:
            today = datetime.today().date()
            expiry_date = datetime.strptime(coupon.expiryDate, '%Y-%m-%d').date()
            if expiry_date > today:
                return coupon.discount  # Return the coupon's discount percentage
        return 0  # Coupon has no effect

    def calcFinalPayment(self, coupon: 'Coupon' = None) -> float:
        if coupon:
            discount = self.calcDiscount(coupon)
            final_amount = float(self.amount) - (float(self.amount) * float(discount)) / 100 
            return final_amount  # Return the final payment amount with the discount applied
        return self.amount # If no coupon is provided, return the original payment amount


# DebitCard is a type of Payment
class DebitCard(Payment):
    def __init__(self, amount: float, cardNum: str, bankName: str, nameOnCard: str):
        super().__init__(amount)  # Call the constructor of the base class (Payment)
        self.__cardNum = cardNum  # Set the debit card number
        self.__bankName = bankName  # Set the name of the bank associated with the debit card
        self.__nameOnCard = nameOnCard  # Set the name on the debit card

    @property
    def cardNum(self,):
        return self.__cardNum

    @cardNum.setter
    def cardNum(self, value):
        self.__cardNum = value

    @property
    def bankName(self,):
        return self.__bankName

    @bankName.setter
    def bankName(self, value):
        self.__bankName = value

    @property
    def nameOnCard(self,):
        return self.__nameOnCard

    @nameOnCard.setter
    def nameOnCard(self, value):
        self.__nameOnCard = value

    def calcDiscount(self, coupon:'Coupon') -> float:
        if coupon:
            today = datetime.today().date()
            expiry_date = datetime.strptime(coupon.expiryDate, '%Y-%m-%d').date()
            if expiry_date > today:
                return coupon.discount
        return 0  # Coupon has no effect

    def calcFinalPayment(self, coupon: 'Coupon' = None) -> float:
        if coupon:
            discount = self.calcDiscount(coupon)
            final_amount = float(self.amount) - (float(self.amount) * float(discount)) / 100 
            return final_amount
        return self.amount 


# Cash is a type of Payment
class Cash(Payment):
    def __init__(self, amount: float):
        super().__init__(amount)  # Call the constructor of the base class (Payment)

    def calcDiscount(self, coupon:'Coupon') -> float:
        if coupon:
            today = datetime.today().date()
            expiry_date = datetime.strptime(coupon.expiryDate, '%Y-%m-%d').date()
            if expiry_date > today:
                return coupon.discount
        return 0  # Coupon has no effect

    def calcFinalPayment(self, coupon: 'Coupon' = None) -> float:
        if coupon:
            discount = self.calcDiscount(coupon)
            final_amount = float(self.amount) - (float(self.amount) * float(discount)) / 100 
            return final_amount
        return self.amount 


# Coupon class represents a coupon added to a payment.
class Coupon:
    def __init__(self, couponID: str, expiryDate: datetime, discount: float):
        self.__couponID = couponID  # Set the unique identifier of the coupon
        self.__expiryDate = expiryDate  # Set the coupon's expiry date
        self.__discount = discount  # Set the discount percentage offered by the coupon

    @property
    def couponID(self,):
        return self.__couponID

    @couponID.setter
    def couponID(self, value):
        self.__couponID = value

    @property
    def expiryDate(self,):
        return self.__expiryDate

    @expiryDate.setter
    def expiryDate(self, value):
        self.__expiryDate = value

    @property
    def discount(self,):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value

    
