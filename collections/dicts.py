# dict տվայլների կառուցվածք է, որն իր մեջ պահպանում է զույգեր բանալի-արժեք
server_config = {
    "host": "localhost", #host-key localhost-value
    "port": 8080,
    "user": "root",
    "admin": True
}

#տվյալներ կարող ենք ստանալ օրինակ print-ով
print(server_config["host"]) #localhost

#կարևոր մեթոդներից է get-ը,
# երբ մենք պահանջում ենք բանալի, որը չկա,
# get-ը ավելացնում է այն և տալիս է նրան defaoult արժեք

user_online_status = server_config.get("user_online_status", False)
print(user_online_status) #False

#Մենք կարող ենք ավելացնել կամ թարմացնել բանալի և արժեք
server_config["admin"] = False #փոխեցինք արժեքը

server_config["user_age"] = 18 #ավելացրինք բանալին և արժեքը

print(server_config) #{'host': 'localhost', 'port': 8080, 'user': 'root', 'admin': False, 'user_age': 18}

#կարևոր մեթոդներից է pop-ը, որը ջնջում է բանալին և վերադարձնում նրա արժեքը
removed_key = server_config.pop("admin")
print(f"մենք ջնջել ենք {removed_key} արժեքը")

print(f"բառարանի տեսքն է՝ {server_config}")

#setdefault
#եթե բանալի չկա այս մեթոդը ստեղծում է բանալի, մեր տրված արժեքով
user_ip = server_config.setdefault("user_ip", "127.0.0.1")
print(user_ip)

#update-ը միավորում է երկու բառարանները
enhanced_config = {
    "port": 5500,
    "secret_key": "12345"
}
server_config.update(enhanced_config)
print(server_config) #{'host': 'localhost', 'port': 5500, 'user': 'root', 'user_age': 18, 'user_ip': '127.0.0.1', 'secret_key': '12345'}

#մեթոդներ ինֆորմացիա ստանալու համար
print(server_config.keys()) #(['host', 'port', 'user', 'user_age'])
print(server_config.values()) #(['localhost', 8080, 'root', 18])
print(server_config.items()) #([('host', 'localhost'), ('port', 8080), ('user', 'root'), ('user_age', 18)])

#Practic
user_profile = {
    "username": "Name",
    "access_level": 1
}

user_email = user_profile.get("email", "no_email")
print(user_email)

enhanced_user_profile = {
    "access_level": 5,
    "is_active": True
}

user_profile.update(enhanced_user_profile)
print(user_profile)
