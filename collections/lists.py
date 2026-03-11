cars = ['BMW', 'Mercedes', 'Audi']
cars.append('Renault') # ավելացնում է տարր վերջում
print(cars)
# element[n:N] վերցնում է n-ից մինչև N-1 տարրերը
print(cars[1:3])
print(cars[::-1]) # շրջում է ցուցակը (reverse)

# tuple
local_host = ("localhost", 8080, "production") # ստեղծելուց հետո չի կարելի փոխել
print(local_host)

# Վարժություններ
#Հեշտ
linux_distros = ['Ubuntu', 'Debian', 'Fedora']
print(linux_distros[1])

my_tuple = (1, 2, 3)
print(my_tuple[-1])

#Միջին
prices = [120, 150, 130, 180, 200]
print(prices[0:3])
print(prices[::-1])

#Դժվար
raw_data = "Python|JS|HTML|CSS"
tech_list = raw_data.split("|")
tech_list.append("SQL")
print(tech_list)

#Ավելին
portfolio = ["Apple", "Tesla", "Google", "Amazon"]
portfolio[1] = "Microsoft"
portfolio.append("Nvidia")
print(portfolio)
print(portfolio[1:3])

# list մեթոդներ
# append
my_list = [1,2,3,4]
my_list.append(5) # ավելացնում է 5 վերջում
print(my_list)

# insert
my_list.insert(2, 'Bash') # ավելացնում է տարր կոնկրետ ինդեքսում
print(my_list)

# extend
second_list = ['Terminal', 'Powershell']
my_list.extend(second_list) # միացնում է 2 ցուցակ
print(my_list)

# remove
price_list = [150,150.3,150,168]
price_list.remove(150) # հեռացնում է առաջին հանդիպած 150-ը
print(price_list)

# pop
word_list = ['First Word', 'Second Word', 'Third Word']
word_list.pop(0) # հեռացնում է տարրը ըստ ինդեքսի, եթե ինդեքս չկա՝ վերջին տարրը
print(word_list)

# clear
word_list.clear() # ամբողջությամբ մաքրում է ցուցակը
print(word_list)

# index
votes = ["yes", "no", "yes", "no", "abstain"]
no_index = votes.index('no') # վերադարձնում է առաջին գտնված ինդեքսը
print(no_index)

# count
yes_count = votes.count('yes') # հաշվում է տարրերի քանակը
print(yes_count)

# sort
unsorted_list = ['Windows', 'Android', 'macOS', 'iOS']
unsorted_list.sort() # դասավորում է ցուցակը
print(unsorted_list)

# reverse
unsorted_list.reverse() # շրջում է ցուցակը
print(unsorted_list)