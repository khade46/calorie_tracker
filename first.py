h = input('Height in cm: ')
h = float(h)
a = input('age in years: ')
a = float(a)
w = input('weight in kg: ')
w = float(w)
while True:
    sex = input('type M for male and F for female: ')
    if sex.lower() not in ['m', 'f']:
        print('wrong input! please try again')
        continue
    else:
        break
amr = input('level of activity - little, moderate or hard?')
if sex == 'M' :
    bmr = 66.47 + (13.75*w) + (5.003*h) - (1.755*a)
    if amr=='little':
        amr = 1.2
    elif amr=='moderate':
        amr = 1.5
    elif amr=='hard':
        amr = 1.8
    cal = bmr*amr
    print('required calories', cal)
elif sex == 'F':
    bmr = 655.1 + (9.563*w) + (1.85*h) - (4.676*a)
    if amr=='little':
        amr = 1.2
    elif amr=='moderate':
        amr = 1.5
    elif amr=='hard':
        amr = 1.8
    cal = bmr*amr
    print('required calories', cal)
itemarr = ['sweets', 'rice', 'chapati', 'milk,', 'veggies', 'alcohol', 'fruits']
calarr = [100, 102, 50, 75, 100, 103, 90]
for i in range(len(itemarr)):
    print(i, '=>', itemarr[i] )
take_input = True
strarr = []
while take_input == True:
    food1 = int(input('type the no. associated with food item: '))
    if food1 in strarr:
        print('same input! please try some other value')
        continue
    else:
        strarr.append(food1)
    cont = input('type y to add more food items else type n')
    if cont == 'y':
        take_input = True
    else:
        take_input = False
print(strarr)
total_cal = 0
for i in strarr:
    print(itemarr[i])
    qnt = int(input('enter the no. of servings: '))
    total_cal = total_cal + calarr[i]*qnt
print('total calories consumed: ', total_cal)
