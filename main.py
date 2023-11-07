import pandas as pd
import time



def add():
    a= input('Enter your vehicle type (for info, check the fare list): ')
    b= input('Enter your vehicle number: ')
    c= input('Enter your name: ')

    f = open('record.txt','a')
    f.write(a+ '  ' +b+ '  '+c+ '\n')
    f.close()
    


def take():
    pass

def available():
    pass

def fare(x):
    read = pd.read_csv(x)
    print(read)

if __name__ == '__main__':

    print('')
    print('WELCOME TO OUR VEHICLE PARKING ARENA ')
    print('')
    print('This area is under CCTV survelliance.\n'
          'It is requested for all the drivers to park your vehicle properly')
    print('')
    
    while True:
        ask = input("\n"
                    ">> To check vehicle parking charges/day, PRESS 'c' \n"
                    ">> To add your vehicle into the parking arena, PRESS 'a' \n"
                    ">> To take your vehicle out of parking arena, PRESS 't' \n"
                    ">> To check details of vehicle available, PRESS 'd' \n"
                    ">> To exit out of this system , PRESS 'e' \n"
                    ">>>>>")
        
        if ask == 'c':
            fare('fare.csv')
            time.sleep(4)
        
        elif ask == 'a':
            add()
            print('\n')
            print('Your vehicle is successfully registered in the arena')
            time.sleep(2)

        elif ask == 't':
            fare('fare.csv')
        
        elif ask == 'd':
            fare('fare.csv')
        
        elif ask == 'e':
            print('Thank you for visiting....Have a safe drive!!')
            time.sleep(2)
        
        else:
            print('invalid input')
            time.sleep(2)
        