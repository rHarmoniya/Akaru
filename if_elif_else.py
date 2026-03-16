# if-ը elif-ը և else-ը պայմանական օպերատորներ են։
# ըստ պայմանի կատարում է կոդի որոշակի մասը։

user_age = int(input('Մուտքագրեք ձեր տարիքը: '))

if user_age == 18: # հավասար է
    print('Դուք չափահաս եք')
elif user_age < 18: # փոքր է
    print('Դուք երեխա եք')
else: # մեծ է
    print('Դուք բավականին մեծ եք')

# Մենք կարող ենք նաև օգտագործել not, and, or օպերատորները։

user_weigth = int(input('Մուտքագրեք ձեր քաշը։ '))
user_height = int(input('Մուտքագրեք ձեր հասակը։ '))

if user_weigth and user_height:
    print(f'Ձեր քաշը {user_weigth} է, իսկ հասակը {user_height} է։')
elif user_weigth or user_height:
    print(f'Ձեր քաշը {user_weigth} է, կամ հասակը {user_height} է։')
else:
    print('Դուք ոչ քաշ եք մուտքագրել, ոչ էլ հասակ։')