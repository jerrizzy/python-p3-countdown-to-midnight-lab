from time import sleep

def countdown(seconds):
    while seconds:
        print(f'{seconds} SECOND(S)!')
        seconds -= 1
    print("HAPPY NEW YEAR!")

print(countdown(5))

def countdown_with_sleep(number):
    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
        sleep(1)
    print("HAPPY NEW YEAR!")

print(countdown_with_sleep(5))