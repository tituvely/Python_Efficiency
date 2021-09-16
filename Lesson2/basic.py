from optparse import OptionParser

def main():
    # %prog 는 실행한 파일의 이름으로 대치됨
    option = OptionParser(usage="%prog", version="%prog 1.0")

    (option, args) = option.parse_args()

if __name__ == '__main__':
    main()