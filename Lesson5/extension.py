# 특정 확장자를 가진 파일 검출하기
import os
import glob

def main():
    path = './extension'
    for filename in glob.glob(os.path.join(path, '*.txt')):
        print(filename)

if __name__ == '__main__':
    main()