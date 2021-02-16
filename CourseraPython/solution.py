import csv
from os.path import splitext


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        if splitext(photo_file_name)[1] and splitext(photo_file_name)[0] and photo_file_name.count(".") == 1\
                and splitext(photo_file_name)[1] != "." and float(carrying) > 0.0:
            self.photo_file_name = photo_file_name
            self.carrying = float(carrying)
        else:
            raise ValueError
    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]



class Car(CarBase):
    car_type = "car"
    passenger_seats_count = 0
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = "truck"
    body_length = 0.0
    body_width = 0.0
    body_height = 0.0
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        lst = body_whl.split("x")
        while len(lst) < 3:
            lst.append("")
        for x in lst:
            try:
                if float(x) <= 0 or len(lst) > 3:
                    self.body_length = self.body_width = self.body_height = 0.0
                    break
                else:
                    self.body_length = float(lst[0])
                    self.body_width = float(lst[1])
                    self.body_height = float(lst[2])
            except ValueError:
                self.body_length = self.body_width = self.body_height = 0.0
                continue
    def get_body_volume(self):
        volume = self.body_length * self.body_width * self.body_height
        return volume


class SpecMachine(CarBase):
    car_type = "spec_machine"
    extra = ""
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            name = row[0]
            if row[1] and row[3]:
                try:
                    if name == "car":
                        if int(row[2]) > 0:
                            temp = Car(row[1], row[3], row[5], row[2])
                            car_list.append(temp)
                    elif name == "truck":
                        temp = Truck(row[1], row[3], row[5], row[4])
                        car_list.append(temp)
                    elif name == "spec_machine":
                        if row[6]:
                            temp = SpecMachine(row[1], row[3], row[5], row[6])
                            car_list.append(temp)
                except ValueError:
                    continue
    return car_list