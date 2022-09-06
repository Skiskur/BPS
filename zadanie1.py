import sys


class Encryptor:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.result = ""
        self.keyM = []

    def set_key(self, key):
        self.key = key

    #get data from some file
    def get_data_from_file(self, file):
        try:
            fh = open(file, "r")
            self.set_data(fh.read())
        except IOError:
            print("Error: can\'t find file or read data")

    def set_data(self, data):
        self.data = data

    def print_result(self):
        print(self.result)

    def print_data(self):
        print(self.data)

    #generate matriks 5x19, the pass on start, next: anouthe unusable sibols
    def generate_keyM(self):
        for i in self.key:
            if i not in self.keyM:
                self.keyM.append(i)
        for i in range(32, 127):
            if chr(i) not in self.keyM:
                self.keyM.append(chr(i))

    #return true if two sibols in same collum in matriks
    def in_same_collum(self, first, second):
        first_position = self.keyM.index(first)
        second_position = self.keyM.index(second)

        if first_position % 5 == second_position % 5:
            return True
        else:
            return False

    #return true if two simbols in same row in matriks
    def in_same_row(self, first, second):
        first_position = self.keyM.index(first)
        second_position = self.keyM.index(second)

        if int(first_position / 5) == int(second_position / 5):
            return True
        else:
            return False

    #encryption algoritm
    #if simbols in same row +1
    #if simbols in same collum +6
    #if nothing above index 1 + index 2 + 127
    def encryption(self):
        self.result = ""
        if self.data == "":
            return
        hlam = self.keyM.index(self.data[0])

        if self.data[0] != self.key[0]:
            if self.in_same_row(self.data[0], self.key[0]):
                hlam += 1
                if hlam % 5 == 0:
                    hlam -= 5
                self.result += self.keyM[hlam]
            else:
                if self.in_same_collum(self.data[0], self.key[0]):
                    hlam += 5
                    if hlam > 94:
                        hlam -= 94
                    self.result += self.keyM[hlam]
                else:
                    first = self.keyM.index(self.data[0])
                    second = self.keyM.index(self.key[0])
                    self.result += chr(first + second + 127)
        else:
            self.result += self.keyM[hlam]

        for i in range(1, len(self.data)):
            hlam = self.keyM.index(self.data[i])
            if self.data[i] != self.data[i-1]:
                if self.in_same_row(self.data[i], self.data[i-1]):
                    hlam += 1
                    if hlam % 5 == 0:
                        hlam -= 5
                    self.result += self.keyM[hlam]
                else:
                    if self.in_same_collum(self.data[i], self.data[i-1]):
                        hlam += 5
                        if hlam > 94:
                            hlam -= 94
                        self.result += self.keyM[hlam]
                    else:
                        first = self.keyM.index(self.data[i])
                        second = self.keyM.index(self.data[i-1])
                        self.result += chr(first + second + 127)
            else:
                self.result += self.keyM[hlam]

    #decryption algoritm
    def decryption(self):
        self.result = ""
        if self.data == "":
            return
        try:
            hlam = self.keyM.index(self.data[0])
            if self.data[0] != self.key[0]:
                if self.in_same_row(self.data[0], self.key[0]):
                    hlam -= 1
                    if hlam < 0 or hlam % 5 == 4:
                        hlam += 5

                else:
                    if self.in_same_collum(self.data[0], self.key[0]):
                        hlam -= 5
                        if hlam < 0:
                            hlam += 94
        except:
            hlam = ord(self.data[0])-127-self.keyM.index(self.key[0])

        self.result += self.keyM[hlam]

        for i in range(1, len(self.data)):
            try:
                hlam = self.keyM.index(self.data[i])

                if self.data[i] != self.result[len(self.result) - 1]:
                    if self.in_same_row(self.data[i], self.result[len(self.result) - 1]):
                        hlam -= 1
                        if hlam < 0 or hlam % 5 == 4:
                            hlam += 5

                    else:
                        if self.in_same_collum(self.data[i], self.result[len(self.result) - 1]):
                            hlam -= 5
                            if hlam < 0:
                                hlam += 94
            except:
                hlam = ord(self.data[i])-127-self.keyM.index(self.result[len(self.result) - 1])

            self.result += self.keyM[hlam]


if __name__ == "__main__":

    start = True

    list_of_arguments = sys.argv

    en = Encryptor("", "")

    if "-s" in list_of_arguments and "-d" in list_of_arguments:
        print("Error: -s and -d flags together")
        start = False
    if "-p" not in list_of_arguments:
        print("Error: No password")
        start = False
    if "-s" not in list_of_arguments and "-d" not in list_of_arguments:
        print("Error: No flags")
        start = False

    try:
        for i in range(0, len(list_of_arguments)):
            if list_of_arguments[i] == "-p":
                #set pass
                en.set_key(list_of_arguments.pop(i + 1))
                break
    except:
        print("Error: Something went wrong!!")
        start = False

    #get data from file
    en.get_data_from_file(list_of_arguments[len(list_of_arguments)-1])

    if start:
        # generate Matriks
        en.generate_keyM()

        if "-s" in list_of_arguments:
            en.encryption()
        if "-d" in list_of_arguments:
            en.decryption()

        # for i in range(0, 95, 5):
        #     print(en.keyM[i:i+5])
        # en.print_data()

        en.print_result()
        e = input()