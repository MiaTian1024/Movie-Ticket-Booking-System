from Models import Guest, Customer, Admin, FrontDeskStaff, Movie

class ReadFile():
    def __init__(self) -> None:
        self.__movieList = [] 
        self.__customerList = []
        self.__adminList = []
        self.__staffList = []

    def getMovieObj(self, file_path):
        # Open and read the movie file
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into values using a comma as the delimiter
                values = line.strip().split(', ')    
                self.__movieList.append(values)
        file.close()
        # create movie Object
        movieObj = []
        for record in self.__movieList:
            title, language, genre, releaseDate = record
            movie = Movie(title, language, genre, releaseDate)
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

