import datetime

# greet the user based on time

user_name = input('please enter your name? ')

# print(dir(datetime.datetime))
hour = datetime.datetime.now().hour
if hour < 12:
    print(f"Hello {user_name}, Good Morning")
elif hour < 18:
    print(f"Hello {user_name}, Good Afternoon")
else:
    print(f"Hello {user_name}, Good Night.")
