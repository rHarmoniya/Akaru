# #variables
# #հիմնական փոփոխականների տեսակներ: int, float, str, bool, None
#
# #ամբողջ թվի և տասնորդական թվի տարբերությունը
# integer_var = 1
# float_var = 1.5
#
# #տողի (string) 2 տեսակ
# string_var = "Hello World"
# second_str_var = 'Hello Guys'
#
# #տրամաբանական տիպեր (bool)
# true_bool_var = True
# false_bool_var = False
#
# #None տիպ
# none_var = None
#
# #Վարժություններ
# #Հեշտ
# company_name = "Starbucks"
# current_price = 3.0
# volume = 5
#
# #Միջին
# price = 100.0
# quantity = 6
# total_revenue = price * quantity
# print(total_revenue)
#
# data = 100
# data = "Сто"
# print(data)
#
# #Դժվար
# old_price = 120.0
# new_price = 150.0
#
# price_difference = new_price - old_price
# print(f"your price difference is {price_difference}")
# percent_difference = (price_difference / old_price) * 100
# print(f"your percent difference is {percent_difference}")
#
# #Ավելին
# start_price = 100.0
# demand = 15
# total_income = start_price * demand
# subsidy = None
#
# print(start_price)
# print(demand)
# print(total_income)
# print(subsidy)

# #ամբողջ և տասնորդական թվեր
# a = 15
# b = 2
# print(a//b)
# print(a%b)
# print(a**b)
#
# #string մեթոդներ
#
# text1 = 'Hello World'
# text2 = text1.strip()  # հեռացնում է բացատները սկզբից և վերջից
# print(text2)
# text3 = text2.upper()  # դարձնում է մեծատառ
# print(text3)
# text4 = text3.lower()  # դարձնում է փոքրատառ
# print(text4)
# text5 = text2.replace(' ','-')  # փոխարինում է բացատները "-"
# print(text5)
# text6 = text2.split(sep='_')  # բաժանում է "_" նշանով
# print(text6)
#
# #None-ը միշտ համարվում է False
# #Վարժություններ
# number = 25
# print(number**0.5)
#
# messy_string = "    Python is awesome!"
# print(messy_string.strip().upper())
#
# my_num = 42
# print(my_num%2)
#
# #Միջին
# x = 0.1
# y = 0.2
# print(x+y)
# print(round(x+y,1))
#
# secret_key = None
# print(secret_key is None)
#
# #Դժվար
# db_record = "user_email@GMAIL.com \n"
# clean_record = db_record.strip().lower()
# print(clean_record)
#
# #Ավելին
# file_name = "   RePort_2026.TXT"
# file_size = 1048576
# file_name_fix = file_name.strip().lower().replace(".txt",".md")
# file_size_gb = file_size//(1024**2)
# print(f"File {file_name_fix} has {file_size_gb} GB")

# Collections(list, tuple, slicing)
# 1 list և list մեթոդներ
# cars = ['BMW', 'Mercedess', 'Audi']
# cars.append('Reno') # ավելացնում է տարր վերջում
# print(cars)
# # element[n:N] վերցնում է n-ից մինչև N-1 տարրերը
# print(cars[1:3])
# print(cars[::-1]) # շրջում է ցուցակը (reverse)
#
# # tuple
# local_host = ("localhost", 8080, "production") # ստեղծելուց հետո չի կարելի փոխել
# print(local_host)

# Վարժություններ
# #Հեշտ
# linux_distros = ['Ubuntu', 'Debian', 'Fedora']
# print(linux_distros[1])
#
# my_tuple = (1, 2, 3)
# print(my_tuple[-1])
#
# #Միջին
# prices = [120, 150, 130, 180, 200]
# print(prices[0:3])
# print(prices[::-1])
#
# #Դժվար
# raw_data = "Python|JS|HTML|CSS"
# tech_list = raw_data.split("|")
# tech_list.append("SQL")
# print(tech_list)
#
# #Ավելին
# portfolio = ["Apple", "Tesla", "Google", "Amazon"]
# portfolio[1] = "Microsoft"
# portfolio.append("Nvidia")
# print(portfolio)
# print(portfolio[1:3])
#
# list մեթոդներ
# append
# my_list = [1,2,3,4]
# my_list.append(5) # ավելացնում է 5 վերջում
# print(my_list)
#
# insert
# my_list.insert(5, 'Bash') # ավելացնում է տարր կոնկրետ ինդեքսում
# print(my_list)
#
# extend
# second_list = ['Terminal', 'Powershell']
# my_list.extend(second_list) # միացնում է 2 ցուցակ
# print(my_list)
#
# remove
# price_list = [150,150.3,150,168]
# price_list.remove(150) # հեռացնում է առաջին հանդիպած 150-ը
# print(price_list)
#
# pop
# word_list = ['First Word', 'Second Word', 'Third Word']
# word_list.pop(0) # հեռացնում է տարրը ըստ ինդեքսի, եթե ինդեքս չկա՝ վերջին տարրը
# print(word_list)
#
# clear
# word_list.clear() # ամբողջությամբ մաքրում է ցուցակը
# print(word_list)
#
# index
# votes = ["yes", "no", "yes", "no", "abstain"]
# no_index = votes.index('no') # վերադարձնում է առաջին գտնված ինդեքսը
# print(no_index)
#
# count
# yes_count = votes.count('yes') # հաշվում է տարրերի քանակը
# print(yes_count)
#
# sort
# unsorted_list = ['BingOS', 'Android', 'Google', 'Ios']
# unsorted_list.sort() # դասավորում է ցուցակը
# print(unsorted_list)
#
# reverse
# unsorted_list.reverse() # շրջում է ցուցակը
# print(unsorted_list)
#dict տվայլների կառուցվածք է, որն իր մեջ պահպանում է զույգեր բանալի-արժեք

# server_config = {
#     "host": "localhost", #host-key localhost-value
#     "port": 8080,
#     "user": "root",
#     "admin": True
# }
#
# #տվյալներ կարող ենք ստանալ օրինակ print-ով
# print(server_config["host"]) #localhost
#
# #կարևոր մեթոդներից է get-ը,
# # երբ մենք պահանջում ենք բանալի, որը չկա,
# # get-ը ավելացնում է այն և տալիս է նրան defaoult արժեք
#
# user_online_status = server_config.get("user_online_status", False)
# print(user_online_status) #False
#
# #Մենք կարող ենք ավելացնել կամ թարմացնել բանալի և արժեք
# server_config["admin"] = False #փոխեցինք արժեքը
#
# server_config["user_age"] = 18 #ավելացրինք բանալին և արժեքը
#
# print(server_config) #{'host': 'localhost', 'port': 8080, 'user': 'root', 'admin': False, 'user_age': 18}
#
# #կարևոր մեթոդներից է pop-ը, որը ջնջում է բանալին և վերադարձնում նրա արժեքը
# removed_key = server_config.pop("admin")
# print(f"մենք ջնջել ենք {removed_key} արժեքը")
#
# print(f"բառարանի տեսքն է՝ {server_config}")
#
# #setdefault
# #եթե բանալի չկա այս մեթոդը ստեղծում է բանալի, մեր տրված արժեքով
# user_ip = server_config.setdefault("user_ip", "127.0.0.1")
# print(user_ip)
#
# #update-ը միավորում է երկու բառարանները
# enhanced_config = {
#     "port": 5500,
#     "secret_key": "12345"
# }
# server_config.update(enhanced_config)
# print(server_config) #{'host': 'localhost', 'port': 5500, 'user': 'root', 'user_age': 18, 'user_ip': '127.0.0.1', 'secret_key': '12345'}
#
# #մեթոդներ ինֆորմացիա ստանալու համար
# print(server_config.keys()) #(['host', 'port', 'user', 'user_age'])
# print(server_config.values()) #(['localhost', 8080, 'root', 18])
# print(server_config.items()) #([('host', 'localhost'), ('port', 8080), ('user', 'root'), ('user_age', 18)])
#
# #Practic
# user_profile = {
#     "username": "Name",
#     "access_level": 1
# }
#
# user_email = user_profile.get("email", "no_email")
# print(user_email)
#
# enhanced_user_profile = {
#     "access_level": 5,
#     "is_active": True
# }
#
# user_profile.update(enhanced_user_profile)
# print(user_profile)

#Set բազմություններ, տարրերի չկարգավորված հավաքածու է

#այստեղ կրկնությունը հաշվի չի առնվում
my_set = {1,2,3,3,3,3,5,5,6,7,8,9,10}
print(my_set) #1,2,3,4,5,6,7,8,9,10