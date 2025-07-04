from smartphone import Smartphone

catalog = [
    Smartphone("Tecno", "NavoX", "+79081033525"),
    Smartphone("Vivo", "Y71", "+79021351258"),
    Smartphone("Xiaomi", "Redmi 6", "+79503695147"),
    Smartphone("Oppo", "A3x", "+79133272568"),
    Smartphone("Realmi", "Note6X", "+79601235489")
    ]


for phone in catalog:
    print(phone.phone_info())
