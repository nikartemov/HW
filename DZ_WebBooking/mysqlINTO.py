import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset = "utf8"
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Flight:

    def __init__(self, db_connection, flight_number, airlines, image_url, description, airplane, departure_airport, arrival_airport, cost):
        self.db_connection = db_connection.connection
        self.flight_number = flight_number
        self.airlines = airlines
        self.image_url = image_url
        self.description = description
        self.airplane = airplane
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.cost = cost

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO flights (flight_number, airlines, image_url, description, airplane, departure_airport, arrival_airport, cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                  (self.flight_number, self.airlines, self.image_url, self.description, self.airplane, self.departure_airport, self.arrival_airport, self.cost))
        self.db_connection.commit()
        c.close()


con = Connection("alex", "123", "WebBooking_db")

with con:
    flight1 = Flight(con, 'SU6634', "Aeroflot", "img/Aeroflot_logo.png", "Москва - Казань", "Boeing777-200", "DME", "KZN", "34000 рублей")
    flight2 = Flight(con, 'S7 48', "S7", "img/S7_logo.png", "Москва - Ставрополь", "Airbus A319-100", "DME", "STV", "20000 рублей")
    flight1.save()
    flight2.save()