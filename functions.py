#Ֆունկցիաները կոդի բլոկներ են, որոնք մեզ թույլ են տալիս բազմիցս օգտագործել նույն կոդը։Սա լիարժեք օբյեկտ է, որը ստեղծվում է անմիջապես ծրագրի կատարման ընթացքում։

# Ֆունկցիայի ստեղծում
def greet(name):
    print(f"Hello, {name}!")

greet("Arthur")

#return-ը ամենակարևով արգումենտներից է։ Print-ը ընդհամենը արդյունքը արտածում է, իսկ return-ը, բացի արտածելը մեզ է վերադարձնում ստացված արժեքը։
def print_func(a, b):
    print(a + b)

print_res = print_func(1, 2)
print(print_res) #կվերադարձնի None։

def return_func(a, b):
    return a + b

return_res = return_func(1, 2)
print(return_res) #կվերադարձնի արգումենտների գումարը։

#արգումենտների անոտացիան թույլ է տալիս ներկայացնել արգումենտների տիպերը և նշել թե ինչ տիպ է վերադարձնելու
def add(x: int, y: int) -> int:
    return x + y

print(add(1, 2))

#Practic
def calculate_discount(price: float, discount_percent: float) -> float:
    result = price - (price * (discount_percent / 100))
    return result

print(calculate_discount(100.0, 20.0))
