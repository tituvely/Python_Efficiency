# 파일 이름 변경하기
import os

def main():
    path = './batch_rename'
    for filename in os.listdir(path):
        if filename.startswith('python_') == False:
            os.rename(os.path.join(path, filename), os.path.join(path, 'python_%s' % filename))

if __name__ == '__main__':
    main()