from Models import Guest, Customer, Admin, FrontDeskStaff, Movie, CinemaHall, Screening, ScreeningSeat, Coupon

class ReadFile():
    def __init__(self) -> None:
        self.__movieList = [] 
        self.__customerList = []
        self.__adminList = []
        self.__staffList = []
        self.__hallList = []
        self.__screeningList = []
        self.__couponList = []

    def getMovieObj(self, file_path):
        # Open and read the movie file
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')    
                self.__movieList.append(values)
        file.close()
        screening_obj = self.getScreeningObj("file/screening.txt")
        # create movie Object
        movieObj = []
        for i, record in enumerate(self.__movieList):
            title, language, genre, releaseDate = record
            screening_1 = screening_obj[i % len(screening_obj)]
            screening_2 = screening_obj[(i+1) % len(screening_obj)]
            screening_3 = screening_obj[(i+2) % len(screening_obj)]
            movie = Movie(title, language, genre, releaseDate)
            movie.add_screening(screening_1)
            movie.add_screening(screening_2)
            movie.add_screening(screening_3)
            movieObj.append(movie)
        return movieObj
    
    def getCustomerObj(self, file_path):
        # Open and read the customer file
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')  
                self.__customerList.append(values)
        file.close()
        # create customer Object
        customerObj = []
        for record in self.__customerList:
            username, email, password = record
            customer = Customer(username, email, password)
            customerObj.append(customer)
        return customerObj
    
    def getAdminObj(self, file_path):
        # Open and read the customer file
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')  
                self.__adminList.append(values)
        file.close()
        # create customer Object
        adminObj = []
        for record in self.__adminList:
            username, email, password = record
            admin = Admin(username, email, password)
            adminObj.append(admin)
        return adminObj
    
    def getStaffObj(self, file_path):
        # Open and read the customer file
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')  
                self.__staffList.append(values)
        file.close()
        # create customer Object
        staffObj = []
        for record in self.__staffList:
            username, email, password = record
            staff = FrontDeskStaff(username, email, password)
            staffObj.append(staff)
        return staffObj
    
    def getSeatObj(self, file_path):
        screening_seats = []
        with open(file_path, 'r') as file:
            for row, line in enumerate(file, start=1):
                for column, char in enumerate(line.strip(), start=1):
                    if char == 'X':
                        seat = ScreeningSeat(row, column, 10)  # Adjust the price as needed
                        screening_seats.append(seat)
        file.close()
        return screening_seats
    
    def getHallObj(self, file_path):
        # Open and read the movie file
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')    
                self.__hallList.append(values)
        file.close()
        hall_1_seat = self.getSeatObj("file/hall-1-seats.txt")
        hall_2_seat = self.getSeatObj("file/hall-2-seats.txt")
        hall_3_seat = self.getSeatObj("file/hall-3-seats.txt")
        hall_4_seat = self.getSeatObj("file/hall-4-seats.txt")
        # create movie Object
        hallObj = []
        for record in self.__hallList:
            name, totalSeats = record
            hall = CinemaHall(name, totalSeats)
            # Assign seat data based on hall name
            if name == "Hall-1":
                hall.listOfSeats = hall_1_seat
            elif name == "Hall-2":
                hall.listOfSeats = hall_2_seat
            elif name == "Hall-3":
                hall.listOfSeats = hall_3_seat
            elif name == "Hall-4":
                hall.listOfSeats = hall_4_seat
            hallObj.append(hall)
        return hallObj
    
    def getScreeningObj(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')    
                self.__screeningList.append(values)
        file.close()
        hall_obj = self.getHallObj("file/hall.txt")
        screeningObj = []
        for i, record in enumerate(self.__screeningList):
            screeningDate, startTime, endTime = record
            hall = hall_obj[i % len(hall_obj)]  # Cyclically repeat halls
            screening = Screening(screeningDate, startTime, endTime, hall)
            screeningObj.append(screening)
        return screeningObj
    
    def getCouponObj(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')    
                self.__couponList.append(values)
        file.close()
        couponObj = []
        for record in self.__couponList:
            couponID, expiryDate, discount = record
            coupon = Coupon(couponID, expiryDate, discount)
            couponObj.append(coupon)
        return couponObj
    
    

