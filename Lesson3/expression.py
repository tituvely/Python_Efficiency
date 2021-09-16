import re
def main():
    # 탐색
    expr = 'Regular'
    value = 'Regular expression test.'

    ## match는 문자열의 처음과 찾으려는 표현식의 처음이 일치할 때 true를 반환
    print (bool(re.match(expr, value)))
    print (bool(re.search(expr, value)))

    expr = 'test'
    print (bool(re.match(expr, value)))
    print (bool(re.search(expr, value)))

    print (re.findall('te', value))
    print (re.findall('es', value))

    # 구분자 
    expr = '[,; ]+'
    value = 'red blue,green;black'
    print (re.split(expr, value))

    expr = '[,; ]+'
    value = 'red blue,green;;black'
    print (re.split(expr, value))

    expr = '[,; ]'
    value = 'red blue,green;;black'
    print (re.split(expr, value)) 

    # 특정 형식으로 출력
    value = 'red blue,green;black'
    print (re.sub(r'[,; ]', ', ', value))

    value = 'Tel : 010-0000-1234'
    print (re.sub(r'\b(\d{3}-\d{4}-\d{4})\b', r'(\1)', value))

    value = 'Tel : 010-0000-1234'
    print (re.sub(r'\b(?P<phone>\d{3}-\d{4}-\d{4})\b', r'(\g<phone>)', value))

    # 그룹 메소드
    value = 'Test string for testing regular expressions.'
    c = re.compile('test')
    print (c.findall(value))

    c = re.compile('test', re.I)
    print (c.findall(value))

    value = '010-0000-1234'
    c = re.compile(r'(\d{2,3})-(\d{3,4})-(\d{4})')
    print (c.match(value).groups())

    value = '02-000-1234'
    print (c.match(value).groups())



if __name__ == '__main__':
    main()