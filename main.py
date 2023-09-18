from time import sleep
from multiprocessing import Process

print('''
Hello Dear User!
This program will-
sort the words or numbers in order of:
Lowest to Highest or Highest to Lowest.''')
choice = input('(N)for number and (W) for word: ')
if choice.lower() == 'n':
    user = input('>>> ')
    backward = input('[(Y)for yes and (N)for no]\n\tReverse? ')
    if backward.lower() == 'y':
        user = user.split(' ')
        res = sorted(user, key=int, reverse=True)
        for i in res:
            print(i, end=' ')
    else:
        user = user.split(' ')
        res = sorted(user, key=int, reverse=False)
        for i in res:
            print(i, end=' ')
elif choice.lower() == 'w':
    user = input('>>> ')
    backward = input('[(Y)for yes and (N)for no]\nReverse? ')
    if backward.lower() == 'y':
        user = user.split(' ')
        user = sorted(user, key=str, reverse=True)
        for i in user:
            print(i, end=' ')
    else:
        user = user.split(' ')
        user = sorted(user, key=str, reverse=False)
        for i in user:
            print(i, end=' ')
else:
    print('ERROR!')


def task():
    sleep(1)


if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    process.join()
    process2 = Process(target=task)
    process2.start()
    process2.join()
