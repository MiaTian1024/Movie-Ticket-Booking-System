from Models import Guest, Customer, Admin, FrontDeskStaff, Movie

class ReadFile():
    def __init__(self) -> None:
        self.__movieList = [] 
        self.__customerList = []
        self.__adminList = []
        self.__staffList = []

    def getMovieList(self, file_path):
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
            movie = Customer(title, language, genre, releaseDate)
            movieObj.append(movie)
        return movieObj
    
    def getCustomerList(self, file_path):
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







# admin_list = []        
# # Open and read the admin file
# with open("file/admin.txt", 'r') as file:
#     for line in file:
#         # Split the line into values using a comma as the delimiter
#         values = line.strip().split(', ')    
#         admin_list.append(values)
# file.close()
# # create customer Object
# customer_obj = []
# for record in customer_list:
#     username, email, password = record
#     customer = Customer(username, email, password)
#     customer_obj.append(customer)

# staff_list = []        
# # Open and read the staff file
# with open("file/staff.txt", 'r') as file:
#     for line in file:
#         # Split the line into values using a comma as the delimiter
#         values = line.strip().split(', ')    
#         staff_list.append(values)
# file.close()
