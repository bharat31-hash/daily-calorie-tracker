#BHARAT GUPTA, 6Th OCT 2025 
#DAILY CALORIE TRACKER
print('Hello Users')
print('This is a Daily calorie tracker you can track your daily calorie intake with it.')

Meal=[]
Calories=[]
num=int(input('enter the no. of meals you had today:'))
for i in range(1,num+1):
    Mname=input('enter meal name:')
    Howcal=int(input('enter the number of calories in this meal:'))
    Meal.append(Mname)
    Calories.append(Howcal)
print(Meal)
print(Calories)

dailyin=int(input('enter your daily calorie intake limit:'))
totcal=sum(Calories)
print('your total calorie intake today is:',totcal)

if totcal>dailyin:
    print('WARNING! you have exceeded your daily calorie intake limit')
else:
    print('GOOD you are within your daily calorie intake limit')
avgcal=totcal/num
print('your average calorie intake per meal is:',avgcal)

print("MEAL\t\tCALORIES\tREVIEW")
print('-'*35)

for i,j in zip(Meal,Calories):
    if j>1000:
        print(f'{i}\t\t{j}\t\tNot Healthy')
    else:
        print(f'{i}\t\t{j}\t\thealthy')