#variables
#հիմնական փոփոխականների տեսակներ: int, float, str, bool, None

#ամբողջ թվի և տասնորդական թվի տարբերությունը
integer_var = 1
float_var = 1.5

a = 15
b = 2
print(a//b)
print(a%b)
print(a**b)

#տողի (string) 2 տեսակ
string_var = "Hello World"
second_str_var = 'Hello Guys'

#None-ը միշտ համարվում է False
#Վարժություններ
number = 25
print(number**0.5)

messy_string = "    Python is awesome!"
print(messy_string.strip().upper())

my_num = 42
print(my_num%2)

#Միջին
x = 0.1
y = 0.2
print(x+y)
print(round(x+y,1))

secret_key = None
print(secret_key is None)

#Դժվար
db_record = "user_email@GMAIL.com \n"
clean_record = db_record.strip().lower()
print(clean_record)

#Ավելին
file_name = "   RePort_2026.TXT"
file_size = 1048576
file_name_fix = file_name.strip().lower().replace(".txt",".md")
file_size_gb = file_size//(1024**2)
print(f"File {file_name_fix} has {file_size_gb} GB")


#տրամաբանական տիպեր (bool)
true_bool_var = True
false_bool_var = False

#None տիպ
none_var = None

#Վարժություններ
#Հեշտ
company_name = "Starbucks"
current_price = 3.0
volume = 5

#Միջին
price = 100.0
quantity = 6
total_revenue = price * quantity
print(total_revenue)

data = 100
data = "Сто"
print(data)

#Դժվար
old_price = 120.0
new_price = 150.0

price_difference = new_price - old_price
print(f"your price difference is {price_difference}")
percent_difference = (price_difference / old_price) * 100
print(f"your percent difference is {percent_difference}")

#Ավելին
start_price = 100.0
demand = 15
total_income = start_price * demand
subsidy = None

print(start_price)
print(demand)
print(total_income)
print(subsidy)