def use_read():
    with open('./test_file', 'r') as f:
        print (f.read())

def use_readline():
    with open('./test_file', 'r') as f:
        while True:
            line = f.readline()

            if not line:
                break

            print (line)

def use_readlines():
    with open('./test_file', 'r') as f:
        print (f.readlines())

def use_write():
    with open('./write_test', 'w') as f:
        f.write('python3\n')
        f.write('write test\n')

def use_write_with_append():
    with open('./write_test', 'a') as f:
        f.write('appended line\n')

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