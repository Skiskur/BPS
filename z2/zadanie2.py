import hashlib as hash
import csv


if __name__ == '__main__':

    name_pass = False
    password_pass = False
    key_pass = False

    name = input('meno: ')
    password = input('heslo: ')
    key = input('overovaci kluc: ')

    hash_pass = hash.md5(password.encode()).hexdigest()

    data = []

    with open('hesla.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
        for row in spamreader:
            if len(row) >= 3:
                if row[0] == name:
                    name_pass = True
                    if row[1] == hash_pass:
                        password_pass = True
                        keys = row[2].split(",")
                        if key in keys:
                            key_pass = True
                            keys.remove(key)
                            row[2] = ','.join(keys)
                data.append(row)

    if name_pass and password_pass and key_pass:
        with open('hesla.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=':')
            writer.writerows(data)
        print('ok')
    else:
        print('chyba')
