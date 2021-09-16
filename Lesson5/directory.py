# 폴더의 이름과 위치 변경하기
import os

def main():
    if os.path.isdir('./sample_dir'):
        os.rename('./sample_dir', './SAMPLE_DIR')

if __name__ == '__main__':
    main()