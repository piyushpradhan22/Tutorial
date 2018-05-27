with open("D:/Python/test.txt") as f:
    print(f.name)
    print(f.read())
    f.seek(0)
    print(f.readline(), end='')
    print(f.readline(), end='')
    sizetoread = 10
    fcon = f.read(sizetoread)
    while (len(fcon)) > 0:
        print(fcon, '*')
        fcon = f.read(sizetoread)
with open("D:/Python/test2.txt",'r+') as f:
    f.write("Hello! this is a test")
    f.seek(0)
    print(f.read())
