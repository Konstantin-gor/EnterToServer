import os
import sys
import dictionary
import sqlite3

#Test on MAC or IP
def GetAdress():
    print(":")
    hostAdr = input()
    if hostAdr[2] == ":":
            hostAdr = hostAdr.replace(":","") + ".vd.is74.ru"
    elif hostAdr.isalpha():
            hostAdr = hostAdr + ".vd.is74.ru"
    return hostAdr
def NewAdress():
    print("Введите адрес нового подключения, если оставить пустым, то будет запрашиваться каждый раз при подключении :")
    adress = GetAdress()
    print("Введите логин нового подключения, если оставить пустым, то будет запрашиваться каждый раз при подключении :")
    login = input()
    print("Введите пароль нового подключения, если оставить пустым, то будет запрашиваться каждый раз при подключении :")
    password = input()
    print("Введите название подключения")
    name = input()
    dictionary.execute_query(connect, dictionary.addHost(adress, login, password, name))
def DelAdress():
    print("Для удаления нам нужно понимать о каком адресе речь. Введите Id адреса :")
    dictionary.execute_query(connect, dictionary.deleteRecord(input()))

def FieldIsEmptyTest(lineNumber, columnNumber):
    ans = hosts[lineNumber][columnNumber]
    if  not hosts[lineNumber][columnNumber] or hosts[lineNumber][columnNumber] == "":
        print(f"Введите значение поля {columnNames[columnNumber][0]}")
        # newValue = dictionary.updateField(columnNames[columnNumber], input(), hosts[text][0])
        # dictionary.execute_query(newValue)
        ans = GetAdress()
        return ans 
    return ans
def DefinionInput(text):
    text = str(text)
    if(str.isnumeric(text)):
        text = int(text)
        os.system(f'/home/gorkostya/scripts/EnterToSshSipAdapter.sh  {FieldIsEmptyTest(text,2)} {FieldIsEmptyTest(text,3)} {FieldIsEmptyTest(text, 1)}')
    elif(text.lower() == 'n'):
        NewAdress()
    elif(text.lower() == 'd'):
        DelAdress()
    else: print("Вы ввели что-то непонятное.")

#Вывод текстового файла и поиск нужной команды
#
# text = open('menu.txt')
# for line in text:
#     sys.stdout.write(line)F
# sys.stdout.write(":")
# number = input()

counter = 0
connect = dictionary.create_connection('/home/gorkostya/scripts/hosts.sqlite')
hosts = dictionary.execute_read_query(connect, dictionary.selectHosts())
columnNames = connect.execute(dictionary.selectHosts()).description

#Progr
print("Выберите требуемый сервер (указать его номер (№) для входа:")
for host in hosts:
    print(f" №:{counter}, Name:{host[4]}, Adress:{host[1]} ID:{host[0]}")
    counter += 1


 

print("Также можно указать:")
print("N - для создания нового подключения")
print("D - для удаления какого-либо из существующих.")
DefinionInput(input())