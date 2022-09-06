import csv
import hashlib


def get_input():
    name = str(input("meno:"))
    password = str(input("heslo:"))
    key = str(input("kluc:"))
    return name, password, key


def get_csv_reader():
    try:
        reader = csv.reader(open("hesla.csv", 'r'), delimiter=':')
        return reader
    except:
        print("Can't open file hesla.csv !")
        exit(2)


def get_csv_writer():
    try:
        writer = csv.writer(open("hesla.csv", 'w'), delimiter=':')
        return writer
    except:
        print("Can't open file hesla.csv !")
        exit(2)


def user_exists(data, name, hashed_password):
    counter = 0
    for col in data:
        if col[0] == name and col[1] == hashed_password:
            return counter
        counter += 1
    return -1


def main():
    name, password, key = get_input()
    hashed_password =  hashlib.md5(password.encode()).hexdigest()
    reader = get_csv_reader()
    data = []
    for row in reader:
        data.append(row)

    index = user_exists(data, name, hashed_password)
    if index < 0:
        print("chyba")
        exit(0)
    keys = data[index][2].replace(',', ' ').split()
    for dbKey in keys:
        if dbKey == key:
            keys.remove(key)
            for i in range(0, 8):
                keys[i] = keys[i] + ','
            keys_str = "".join(keys)
            data[index][2] = keys_str
            writer = get_csv_writer()
            writer.writerows(data)
            print("ok")
            exit(0)
    print("chyba")


main()
