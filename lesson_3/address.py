class Address:

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def get_full_address(self) -> str:
        return (f"{self.index}, "
                f"{self.city}, "
                f"{self.street}, "
                f"{self.house} - "
                f"{self.apartment}")

