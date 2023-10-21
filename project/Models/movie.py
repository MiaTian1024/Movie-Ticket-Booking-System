# Model class of Movie and Screening

from typing import List
from datetime import datetime, date
from cinema import Hall, ScreeningSeat


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
        """! Get the list of screening seats.
        @return A list of screenig seats for this screening
        """
        return self._screening_seats
    
    def get_booked_seats(self) -> List['ScreeningSeat']:
        """! Get the list of booked seats.
        @return A list of booked screenig seats for this screening
        """
        return self._booked_seats
    
    def get_available_seats(self) -> List['ScreeningSeat']:
        """! Get the list of available seats.
        @return A list of available screenig seats for this screening
        """
        pass
