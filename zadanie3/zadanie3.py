class Directory:
    def __init__(self, owner, name, path='', dirs=[], files=[], previus=None, mode=7):
        self.previus = previus
        self.mode = mode
        self.dirs = dirs
        self.files = files
        self.owner = owner
        self.name = name
        self.path = path+name+'\\'


class File:
    def __init__(self, owner, name, mode=7):
        self.mode = mode
        self.owner = owner
        self.name = name


def transformMode(mode: int):
    m = ''

    if mode >= 4:
        m += 'r'
        mode -= 4
    else:
        m +='-'
    if mode >= 2:
        m += 'w'
        mode -= 2
    else:
        m +='-'
    if mode >= 1:
        m += 'x'
        mode -= 1
    else:
        m +='-'

    return m


# ready
def ls(dir: Directory, file=None):
    if dir.mode-4 >= 0:
        if file:
            for node in dir.dirs:
                if node.name == file:
                    print(transformMode(node.mode))
                    return  dir
            for node in dir.files:
                if node.name == file:
                    print(transformMode(node.mode))
                    return dir
            print("Chyba")
        else:
            for node in dir.dirs:
                mode = transformMode(node.mode)
                print(node.name + ' ' + node.owner + ' ' + mode)
            for node in dir.files:
                mode = transformMode(node.mode)
                print(node.name + ' ' + node.owner + ' ' + mode)
    else:
        print("Chyba")


# ready
def touch(dir: Directory, name: str):
    directori = dir
    try:
        path = name.split('/')
        for i in range(0, len(path)):
            if i == len(path) -1:
                t = directori.mode
                if t >= 4:
                    t -= 4
                if t-2 >= 0:
                    for d in directori.files:
                        if d.name == path[i]:
                            print("Chyba")
                            return dir
                    directori.files.append(
                        File(dir.owner, path[i])
                    )
                else:
                    print("Chyba")
            else:
               directori = cd(dir, path[i])
    except:
        print("Chyba")
    return dir


# ready
def mkdir(dir: Directory, name: str):
    directori = dir
    try:
        path = name.split('/')
        for i in range(0, len(path)):
            if i == len(path) - 1:
                t = directori.mode
                if t >= 4:
                    t -= 4
                if t - 2 >= 0:
                    for d in directori.dirs:
                        if d.name == path[i]:
                            print("Chyba")
                            return dir
                    directori.dirs.append(
                        Directory(dir.owner, path[i], directori.path, dirs=[], files=[], previus=directori)
                    )
                else:
                    print("Chyba")
            else:
                directori = cd(dir, path[i])
    except:
        print("Chyba")
    return dir


# ready
def rm(dir: Directory, name_of_file: str):
    try:
        t = dir.mode
        if t >= 4:
            t -= 4
        if t - 2 >= 0:
            for node in dir.dirs:
                if node.name == name_of_file:
                    dir.dirs.remove(node)
                    return dir
            for node in dir.files:
                if node.name == name_of_file:
                    dir.files.remove(node)
                    return dir
        else:
            print("Chyba")
    except:
        print('Chyba')
    return dir


def vypis(dir: Directory, name_of_file: str):
    try:
        for node in dir.dirs:
            if node.name == name_of_file:
                if node.mode >= 4:
                    print('ok')
                else:
                    print('Chyba')
                return dir
        for node in dir.files:
            if node.name == name_of_file:
                if node.mode >= 4:
                    print('ok')
                else:
                    print('Chyba')
                return dir
    except:
        print('Chyba')
    return dir


def spusti(dir: Directory, name_of_file: str):
    try:
        for node in dir.dirs:
            if node.name == name_of_file:
                m = node.mode
                if m >= 4:
                    m -= 4
                if m >= 2:
                    m -= 2
                if m >= 1:
                    print('ok')
                else:
                    print('Chyba')
                return dir
        for node in dir.files:
            if node.name == name_of_file:
                m = node.mode
                if m >= 4:
                    m -= 4
                if m >= 2:
                    m -= 2
                if m >= 1:
                    print('ok')
                else:
                    print('Chyba')
        return dir
    except:
        print('Chyba')
    return dir


# ready
def cd(dir: Directory , way: str):
    try:
        if way == '..':
            if dir.previus:
                return  dir.previus
            else:
                return dir
        for node in dir.dirs:
            if node.name == way:
                return node
    except:
        print('Chyba')
    return dir


def zapis(dir: Directory, name_of_file: str):
    try:
        for node in dir.dirs:
            if node.name == name_of_file:
                m = node.mode
                if m >= 4:
                    m -= 4
                if m >= 2:
                    print('ok')
                else:
                    print('Chyba')
                return dir
        for node in dir.files:
            if node.name == name_of_file:
                m = node.mode
                if m >= 4:
                    m -= 4
                if m >= 2:
                    print('ok')
                else:
                    print('Chyba')
                return dir
    except:
        print('Chyba')
    return dir


def chmod(dir: Directory, name_of_file: str, mode: int):
    try:
        for node in dir.dirs:
            if node.name == name_of_file:
                node.mode = mode
                return dir
        for node in dir.files:
            if node.name == name_of_file:
                node.mode = mode
                return dir
    except:
        print('Chyba')
    return dir


def chown(dir: Directory, name_of_file: str, owner_name: str):
    try:
        for node in dir.dirs:
            if node.name == name_of_file:
                node.owner = owner_name
                return dir
        for node in dir.files:
            if node.name == name_of_file:
                node.owner = owner_name
                return dir
    except:
        print('Chyba')
    return dir


if __name__ == '__main__':

    dir = Directory('Skiskur', 'Skiskur')
    while True:
        s = input(dir.path+'>>>')
        arg = s.split(' ')
        if arg[0]:
            if arg[0] == 'quit':
                break

            elif arg[0] == 'ls':
                try:
                    ls(dir, arg[1])
                except:
                    ls(dir)
            elif arg[0] == 'touch':
                try:
                    touch(dir, arg[1])
                except:
                    print('Chyba')
            elif arg[0] == 'mkdir':
                try:
                    mkdir(dir, arg[1])
                except:
                    print('Chyba')
            elif arg[0] == 'rm':
                try:
                    rm(dir, arg[1])
                except:
                    print('Chyba')
            elif arg[0] == 'vypis':
                try:
                    vypis(dir, arg[1])
                except:
                    print('No name!!!')
            elif arg[0] == 'spusti':
                try:
                    spusti(dir, arg[1])
                except:
                    print('Chyba')
            elif arg[0] == 'cd':
                try:
                    dir = cd(dir, arg[1])
                except:
                    print('Chyba')
            elif arg[0] == 'zapis':
                try:
                    zapis(dir, arg[1])
                except:
                    print('Chyba')
            elif arg[0] == 'chmod':
                try:
                    i = int(arg[1])
                    dir = chmod(dir, arg[2], i)
                except:
                    print('Chyba')
            elif arg[0] == 'chown':
                try:
                    dir = chown(dir, arg[2], arg[1])
                except:
                    print('Chyba')
            else:
                print('Chyba')
