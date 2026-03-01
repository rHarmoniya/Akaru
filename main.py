# #variables
# #base variables: int, float, str, bool, None
#
# #integer and float differences
# integer_var = 1
# float_var = 1.5
#
# #2 types of string
# string_var = "Hello World"
# second_str_var = 'Hello Guys'
#
# #logical types(bools)
# true_bool_var = True
# false_bool_var = False
#
# #None type
# none_var = None
#
# #PRACTIC
# #Easy
# company_name = "Starbucks"
# current_price = 3.0
# volume = 5
#
# #Medium
# price = 100.0
# quantity = 6
# total_revenue = price * quantity
# print(total_revenue)
#
# data = 100
# data = "Сто"
# print(data)
#
# #Hard
# old_price = 120.0
# new_price = 150.0
#
# price_difference = new_price - old_price
# print(f"your price difference is {price_difference}")
# percent_difference = (price_difference / old_price) * 100
# print(f"your percent difference is {percent_difference}")
#
# #More
# start_price = 100.0
# demand = 15
# total_income = start_price * demand
# subsidy = None
#
# print(start_price)
# print(demand)
# print(total_income)
# print(subsidy)

# #integer and float
# a = 15
# b = 2
# print(a//b)
# print(a%b)
# print(a**b)
#
# #string methods
#
# text1 = 'Hello World'
# text2 = text1.strip()
# print(text2)
# text3 = text2.upper()
# print(text3)
# text4 = text3.lower()
# print(text4)
# text5 = text2.replace(' ','-')
# print(text5)
# text6 = text2.split(sep='_')
# print(text6)
#
# #None always = false
# #Practics
# number = 25
# print(number**0.5)
#
# messy_string = "    Python is awesome!"
# print(messy_string.strip().upper())
#
# my_num = 42
# print(my_num%2)
#
# #Medium
# x = 0.1
# y = 0.2
# print(x+y)
# print(round(x+y,1))
#
# secret_key = None
# print(secret_key is None)
#
# #Hard
# db_record = "user_email@GMAIL.com \n"
# clean_record = db_record.strip().lower()
# print(clean_record)
#
# #More
# file_name = "   RePort_2026.TXT"
# file_size = 1048576
# file_name_fix = file_name.strip().lower().replace(".txt",".md")
# file_size_gb = file_size//(1024**2)
# print(f"File {file_name_fix} has {file_size_gb} GB")

#Collections(list, tuple, slicing)
#1 list and list methods
# cars = ['BMW', 'Mercedess', 'Audi']
# cars.append('Reno') #ADD element to the end
# print(cars)
# #element[n:N] take frome n to N-1 elements
# print(cars[1:3])
# print(cars[::-1]) #::-1 reverse list
#
# #tuple
# local_host = ("localhost", 8080, "production") #we can`t change something after creation
# print(local_host)

#PRACTICS
# #Easy
# linux_distros = ['Ubuntu', 'Debian', 'Fedora']
# print(linux_distros[1])
#
# my_tuple = (1, 2, 3)
# print(my_tuple[-1])
#
# #Medium
# prices = [120, 150, 130, 180, 200]
# print(prices[0:3])
# print(prices[::-1])
#
# #Hard
# raw_data = "Python|JS|HTML|CSS"
# tech_list = raw_data.split("|")
# tech_list.append("SQL")
# print(tech_list)
#
# #More
# portfolio = ["Apple", "Tesla", "Google", "Amazon"]
# portfolio[1] = "Microsoft"
# portfolio.append("Nvidia")
# print(portfolio)
# print(portfolio[1:3])
#

1
