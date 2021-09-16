import re
import fileinput

# 파일을 읽으면서 수정하려고 할 때는 fileinput 사용
def convertToLowerCase():
    # inplace는 문제가 생길 경우에 대비해 백업 파일을 생성해주는 것
    with fileinput.FileInput('./replace_test_file', inplace=True) as f:
        for line in f:
            print (line.replace(line, line.lower()), end='')

def convertToUpperCaseWithRe():
    with fileinput.FileInput('./replace_test_file', inplace=True) as f:
        for line in f:
            print (line.replace(line, re.sub('sample', 'Sample', line)), end='')

def readFile():
    print ('======================')
    with open('./replace_test_file', 'r') as f:
        print (f.read())
    print ('======================')

def main():
    readFile()
    convertToLowerCase()
    readFile()
    convertToUpperCaseWithRe()
    readFile()

if __name__ == "__main__":
    main()