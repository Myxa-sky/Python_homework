def month_to_season(n):
    if not isinstance(n, int) or n < 1 or n > 12:
        return "Ошибка: введите число от 1 до 12"
    if n in (12, 1, 2):
        return "Зима"
    elif n in (3, 4, 5):
        return "Весна"
    elif n in (6, 7, 8):
        return "Лето"
    elif n in (9, 10, 11):
        return "Осень"


print(month_to_season(4))
