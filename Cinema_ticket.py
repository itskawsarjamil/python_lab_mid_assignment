class Star_Cinema:

    __hall_list = list()

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.__seats = dict()
        self.__show_list = list()
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = 'hall_0'+str(hall_no)
        self.__booked_seats = {}
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)

        seats = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append(f'({i},{j})')
            seats.append(row)
            # print(row)
        self.__seats[id] = seats


    def book_seats(self, customer_name, phone_number, show_id, seats):
        if show_id not in [show[0] for show in self.__show_list]:
            print("Invalid show ID")
            return
        seat_map = self.__seats[show_id]

        for seat in seats:
            row, col = seat
            if row < 1 or row > self.__rows or col < 1 or col > self.__cols:
                print("Invalid seat")
                return
            if seat_map[row-1][col-1] == 'B':
                print("Seat already booked")
                return
        for seat in seats:
            row, col = seat
            seat_map[row-1][col-1] = 'B'
            self.__booked_seats[(show_id, row, col)] = (
                customer_name, phone_number)
        print("Seats booked successfully!")
        print("Booked seats: ", self.__booked_seats)

    def view_available_seats(self, show_id):
        if show_id not in [show[0] for show in self.__show_list]:
            print("Invalid show ID")
            return
        seat_map = self.__seats[show_id]
        print("Available seats: ")


        for seat in seat_map:
            print(seat)

        # for i in range(self.__rows):
        #     row_seat = []
        #     for j in range(self.__cols):
        #         if seat_map[i][j] != 'B':
        #             row_seat.append(f'({i+1},{j+1})') 
        #     print(row_seat) 

    def view_show_list(self):
        for show in self.__show_list:
            print("ID: ", show[0])
            print("Movie name: ", show[1])
            print("Time: ", show[2])


Hall_No = 1
hall_obj = Hall(3, 4, Hall_No)
Hall_No += 1
hall_obj.entry_show(1, "Avengers: Endgame", "2:00 PM")
hall_obj.entry_show(2, "The Dark Knight", "6:00 PM")
hall_obj.entry_show(3, "Inception", "10:00 PM")

hall_obj.view_show_list()

hall_obj.book_seats("John Doe", "1234567890", 2, [(1, 2), (2, 2), (2, 3)])

hall_obj.view_available_seats(2)
