from address import Address

class Mailing:

    def __init__(self, to_address: Address, from_address: Address,
                 cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def get_info(self) -> str:
        return (f"Отправление {self.track} из "
                f"{self.from_address.get_full_address()} "
                f"в {self.to_address.get_full_address()}. "
                f"Стоимость {self.cost} рублей.")
