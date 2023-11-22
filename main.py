import pandas as pd
import time
import mysql.connector


def fare_chart(): 
    mydb = mysql.connector.connect(host = 'localhost',user='root',password = '123456', database = 'fare')

    mycursor = mydb.cursor()

    mycursor.execute('create table info(ID varchar(60), VEHICLE_TYPE varchar(60), amount int) ')
    mycursor.execute("insert into test values( '0001C', 'CAR', 40)")
    mycursor.execute("insert into test values( '0002B', 'TWO_WHEELERS', 20)")
    mycursor.execute("insert into test values( '0006V', 'TRUCKS(10 wheels)', 70)")
    mycursor.execute("insert into test values( '0007V', 'TRUCKS(16 wheels)', 90)")
    mycursor.execute("insert into test values( '0008V', 'TRAILER TRUCK', 120)")
    mycursor.execute("insert into test values( '0005G', 'BUS', 110)")
    mycursor.execute("insert into test values( '0006G', 'BUS(VOLVO)', 150)")
    mycursor.execute("insert into test values( '0003E', 'TRACTOR', 60)")
    mycursor.execute("insert into test values( '0003E', 'COMMERCIAL_VEHICLES(> 4 wheels)', 80)")
    mycursor.execute("insert into test values( '0004H', 'CONSTRUCTION_VEHICLES', 180)")

    mycursor.execute("select * from test into outfile 'E:\\\\PYTHON PROJECTS\\\\school_work\\\\fare.csv' fields terminated by ',' lines terminated by '\n' ")

    mydb.commit()


def add():
    a= input('Enter your vehicle type (for info, check the fare list): ')
    b= input('Enter your vehicle number: ')
    c= input('Enter your name: ')

    f = open('record.txt','a')
    f.write(a+ '  ' +b+ '  '+c+ '\n')
    f.close()
    
def payment(x):
    veh={'CAR':40,'BIKE':20,'SCOOTER':20,'TRUCK': 70,'TRUCKS(16 wheels)' : 90,'TRAILER TRUCK':120,'BUS':110,'BUS(VOLVO)':150,'TRACTOR':60,'COMMERCIAL_VEHICLES(> 4 wheels)':80}
    inp=True
    amt=0
    while inp==True:
        hr=int(input(f"\tEnter No. of Hours {x.upper()} Parked - "))
        
        if hr == 0 and x.upper() == 'CAR':
            amt=40
            inp=not True
        elif hr == 0 and x.upper() == 'BIKE':
            amt=20
            inp= not True

        elif hr == 0 and x.upper() == 'SCOOTER':
            amt=20
            inp=not True
        elif hr == 0 and x.upper() == 'TRUCK':
            amt=70
            inp=not True
        elif hr == 0 and x.upper() == 'TRUCKS(16 wheels)':
            amt=90
            inp=not True
        elif hr == 0 and x.upper() == 'TRAILER TRUCK':
            amt=120
            inp=not True
        elif hr == 0 and x.upper() == 'BUS':
            amt=110
            inp=not True
        elif hr == 0 and x.upper() == 'BUS(VOLVO)':
            amt=150
            inp=not True
        elif hr == 0 and x.upper() == 'TRACTOR':
            amt=60
            inp=not True
        elif hr == 0 and x.upper() == 'COMMERCIAL_VEHICLES(> 4 wheels)':
            amt=80
            inp=not True

        elif hr>=1:
        
            if x.upper() == 'CAR':
                amt=int(hr)*int(40)
                inp=not True
            elif x.upper() == 'BIKE':
                amt=int(hr)*int(20)
                inp=not True
            elif x.upper() == 'SCOOTER':
                amt=int(hr)*int(20)
                inp=not True
            elif x.upper() == 'TRUCK':
                amt=int(hr)*int(70)
                inp=not True
            elif x.upper() == 'TRUCKS(16 wheels)':
                amt=int(hr)*int(90)
                inp=not True
            elif x.upper() == 'TRAILER TRUCK':
                amt=int(hr)*int(120)
                inp=not True
            elif x.upper() == 'BUS':
                amt=int(hr)*int(110)
                inp=not True
            elif x.upper() == 'BUS(VOLVO)':
                amt=int(hr)*int(150)
                inp=not True
            elif  x.upper() == 'TRACTOR':
                amt=int(hr)*int(60)
                inp=not True
            elif x.upper() == 'COMMERCIAL_VEHICLES(> 4 wheels)':
                amt=int(hr)*int(80)
                inp=not True


    print("\t Parking Charge - ",amt)
    ac=18/100*int(amt)
    print("\tAdd. charge 18 % - ",ac)

    print(f"\tTotal payable amount is - {int(amt)+int(ac)}")
    
    print(".................................Thank you for using our service.............................")
    print('')
    print('')
    

    l = []
    
    for i in veh.keys():
        l.append(i)
    

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
                    ">> To check vehicle parking charges/hour, PRESS 'c' \n"
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
            print("---------------------------------------------------------------------------------------------------")
            print("\t\t\t\tParked Vehicle")
            print("---------------------------------------------------------------------------------------------------")
            print("Vehicle Type  Vehicle Number  Owner Name ")
            print('')
            available()
            print("----------------------------------------------------------------------------------------------------")

            print("-------- Total parked vehicle - ",slot('record.txt'),"----------------------------------------")
            print("----------------------------------------------------------------------------------------------")
            print('')
            
            time.sleep(2)
        
        elif ask == 'e':
            print('Thank you for visiting....Have a safe drive!!')
            break
        
        else:
            print('invalid input')
            time.sleep(2)
        