class Value:
    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value * (1 - obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission