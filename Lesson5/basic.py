# 파일 이름 변경하기
import os

def main():
    if os.path.isfile('./sample'):
        os.rename('./sample', './SAMPLE')

if __name__ == '__main__':
    main()