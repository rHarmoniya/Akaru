#այստեղ կրկնությունը հաշվի չի առնվում
my_set = {1,2,3,3,3,3,5,5,6,7,8,9,10}
print(my_set) #1,2,3,4,5,6,7,8,9,10

my_set = {1,2,3,3,3,3,5,5,6,7,8,9,10}
print(my_set) #1,2,3,4,5,6,7,8,9,10
print(type(my_set))

#Կարող ենք ավելացնել և հեռացնել էլեմենտներ
my_set.add(11)
print(my_set) #ավելացրեցինք 11-ը

my_set.remove(10)
print(my_set) #Ջնջեցինք 11-ը

#երբ մենք փորձում ենք ջնջել էլեմենտ, որը չկա մենք սխալ կստանանք, դրա համար օգտ․ discard
my_set.discard(10000)
print(my_set)

#ստուգում if-ի միջոցով
user_profile = {'online', 'male', 'premium'}
user_active_status = 'online'

if user_active_status in user_profile:
    print(f'user is {user_active_status}')

#նաև կարող ենք օգտագործել միավորման տրամաբանական օպերատորը(և)
backend_devs = {'Alice', 'Bob', 'Charlie'}
frontend_devs = {'Narek', 'Bob', 'Poxos'}

all_devs = backend_devs | frontend_devs
print(f'all devs: {all_devs}')

#or

all_devs_1 = backend_devs.union(frontend_devs)
print(f'all devs_1: {all_devs_1}')

#Հատումը .intersection()
fullstack_devs = backend_devs & frontend_devs
print(f'fullstack devs: {fullstack_devs}') # Bob

#Տարբերությունը .difference()
pure_backend = backend_devs - frontend_devs
print(f'pure_backend: {pure_backend}') #Alice and Charlie

raw_tags = ['python', 'django', 'python', 'rust', 'sql', 'django']
uniqe_tags = set(raw_tags)
print(uniqe_tags)
uniqe_tags.discard('sql')
print(uniqe_tags)

