from csv import DictReader, DictWriter 
from os.path import exists # exists - это проверка на существование файла


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
        


def get_info():
    flag = False
    while not flag:
        try:
            first_name = input("Имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое Имя")
            second_name = input("Введите фамилию: ")
            if len(second_name) < 5:
                raise NameError("Слишком короткая фамилия ")
            phone_numbers = input("Введите номер телефона: ")
            if len(phone_numbers) < 11:
                raise NameError("Слишком короткий номер")
        except NameError as err:
            print(err)
        else:
            flag = True        
    return[first_name, second_name,phone_numbers]



def creat_file(file_name):
    with open(file_name, "w", encoding="utf-8", newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name1', 'second_name', 'phone_numbers'])
        f_w.writeheader()



def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    new_obj = {"first_name": user_data[0], "second_name": user_data[1], "phone_numbers": user_data[2]}
    res.append(new_obj)
    standar_write(file_name,res)



def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_r=DictReader(data)
        return list(f_r) #Ящик со словарями 


def delet(file_name2):
     res = read_file(file_name2)
     if len(res) != 0:
         res.clear()
         standar_write(file_name2,res)
     else:
         print("Файл уже был очищен или был пустой..")     
     
     



def remove_row(file_name):
    search = int(input("Введите номер строки для удаления: "))
    res = read_file(file_name)     
    if search <= len(res):
        res.pop(search - 1)
        print("Файл удален")
        standar_write(file_name,res)
    else:
        print("Введен неверный номер строки")      


def Size(file_name):
    res = read_file(file_name) 
    return len(res)
    


def standar_write(file_name,res): 
    with open(file_name, "w", encoding="utf-8", newline='') as data:
          f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_numbers'])
          f_w.writeheader()
          f_w.writerows(res)      


file_name = "phone.csw"
file_name2 = "phone2.csw"


def copy_data(file_name):
    search = int(input("Введите номер строки для копирования  "))
    res = read_file(file_name)
    res2 = read_file(file_name2)
    if len(res) != 0:
        res2.append(res[search - 1])
        standar_write(file_name2, res2)
    else:
        print("В данном файле нет контактов")
   
    

def main():
    while True:
        command = input("\n Команда (q) - выйти. \n Команда (r) - просмотр телефонной книжки. \n Команда (w) - добавление абонента И.Ф.Тел. \n Команда (с) - копирование  номер строки тел. книжки. \n Команда (r.c) - просмотр копированных контактов \n Команда (d.c) - удаление всех скопированных контактов \n Команда (d) - удаления добавленого контакта \n Введите команду: ")
        if command =="q":
            break
        elif command == "w":
            if not exists(file_name):
                creat_file(file_name)
            write_file(file_name)
        elif command == "r":
            if not exists(file_name):
                print("Файл отсутствует, пожалуйста создайте его! ")
                continue
            elif Size(file_name) == 0:
                print("Файл пустой, нужно его заполнить!")
                continue
            print(*read_file(file_name))   
        elif command == "d":
            if not exists(file_name):
                print("Файл отсутствует, пожалуйста создайте его! ")
                continue
            remove_row(file_name)
        elif command == "c":
            copy_data(file_name)
            print("Вы удачно скопировали файл... ")
        elif command == "r.c":
            if not exists(file_name2):
                print("Файл отсутствует!!! ")
                continue
            elif Size(file_name2) == 0:
                print("Файл пустой!!!")
                continue
            print(*read_file(file_name2)) 
        elif command == "d.c":
            delet(file_name2)
            print("Файл очищен....")
                
                

            

              
main()
