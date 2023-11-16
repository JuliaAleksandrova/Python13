import datetime
def your_age(birthdate):
    birthdate = (datetime.datetime.strptime(birthdate, '%Y-%m-%d'))
    today = datetime.datetime.now()
    age = today - birthdate
    years = age.days//365
    months = (age.days % 365)//30
    days = (age.days % 365) % 30
    return years, months, days
birthdate = input('Please enter Your birthdate(YYYY-MM-DD): ')
result = your_age(birthdate)
print(f'You are {result[0]} years, {result[1]} months, {result[2]} days old')