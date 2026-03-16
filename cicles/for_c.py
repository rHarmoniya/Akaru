#python-ում for-ը ցիկլ է, որը կատարում է կոդի որոշակի մասը, քանի դեռ պայմանը ճիշտ է։
#python-ում for-ը հաշվիչով ցիկլ չէ, այն չի ստանում այս տեսքը՝ for (int i=0; i<10; i++)
# այն աշխատում է ցանկացած իտերացիայի վրա, օրինակ՝ ցանկացած տողի վրա, ցանկացած թվի վրա և այլն։

languages = ['python', 'java', 'c++', 'javascript']

for lang in languages:
    print(f'Ես սովորում եմ {lang}\n')

for i in range(10):
    print(i)

for i in range(10, 20, 2):
    print(i)

