def use_read():
    f = open('./test_file', 'r')
    print (f.read())
    f.close()

def use_readline():
    f = open('./test_file', 'r')
    while True:
        line = f.readline()

        if not line:
            break

        print (line)
    
    f.close()

def use_readlines():
    f = open('./test_file', 'r')
    print (f.readlines())
    f.close()

def use_write():
    f = open('./write_test', 'w')
    f.write('python3\n')
    f.write('write test\n')
    f.close()

def use_write_with_append():
    f = open('./write_test', 'a')
    f.write('appended line\n')
    f.close()

def main():
    use_read()
    print('=================')
    use_readline()
    print('=================')
    use_readlines()

    use_write()
    use_write_with_append()

if __name__ == '__main__':
    main()