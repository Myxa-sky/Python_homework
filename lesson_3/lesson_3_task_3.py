from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "20")

mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500.50,
    track="TR12345678"
)

print(mail.get_info())
