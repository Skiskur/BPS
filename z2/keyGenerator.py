import random
import hashlib as hash

if __name__ == '__main__':

    password = input('pass: ')
    hash_pass = hash.md5(password.encode()).hexdigest()
    # keys = []
    # for i in range(0,10):
    #     keys.append(random.randrange(1,100))
    #
    # print(keys)
    print(hash_pass)