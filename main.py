import pandas as pd
import time



def add():
    a= input('Enter your vehicle type (for info, check the fare list): ')
    b= input('Enter your vehicle number: ')
    c= input('Enter your name: ')

    f = open('record.txt','a')
    f.write(a+ '  ' +b+ '  '+c+ '\n')
    f.close()
    
def payment(x):
    veh={'CAR':40,'BIKE':20,'SCOOTER':20,'TRUCK': 70,'TRUCKS(16 wheels)' : 90,'TRAILER TRUCK':120,'BUS':110,'BUS(VOLVO)':150,'TRACTOR':60,'COMMERCIAL_VEHICLES(> 4 wheels)':80}

    l = []
    
    for i in veh.keys():
        l.append(i)

    if x.upper() in l:
        print(f'Your parking charges is {veh.get(x.upper())} rupees')
    else:
        print('Data not found. Check your input')
    

def take():
    wel = input('please enter your name:')
    wel1 = input("Please enter your vehicle's number")

    file = open('record.txt','r')
    str= file.readlines()


    for i in str:

        if wel in i and wel1 in i:
            l = i.split()
            
            print('')
            print(f'Yes, You got a {l[0]} parked in the arena of registration number {l[1]}')
            payment(l[0])
            break

        elif wel1 not in i:
            print('Yours entered information does not match with any vehicle in database')

    new = []
    
    for j in str:
        if wel not in j.strip() and wel1 not in j.strip():
            new.append(j)
        
    f = open('record.txt','w')
    f.writelines(new)
    f.close()            
        

def available():
    file = open('record.txt', 'r')
    
    str= file.readlines()
    for i in str:
        print(i)
    file.close()
available()

def slot(x):
    with open(x, 'r') as fp:
        lines = len(fp.readlines())
        return lines
    

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
        print(f"total parking slots occupied: {slot('record.txt')} out of 100")
        
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
            take()
            
        
        elif ask == 'd':
            print('VEH_NAME VEH_NUMBER VEH_OWNER')
            print('')
            available()
            time.sleep(2)
        
        elif ask == 'e':
            print('Thank you for visiting....Have a safe drive!!')
            time.sleep(2)
        
        else:
            print('invalid input')
            time.sleep(2)
        