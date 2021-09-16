def main():

    # 대소문자
    print ('=====================')
    test_str = 'Test String 1234 !@#$'
    print ('plain: %s' % test_str)
    print ('upper: %s' % test_str.upper())
    print ('lower: %s' % test_str.lower())
    print ('lower with capitalize: %s' % test_str.lower().capitalize())
    print ('lower with title: %s' % test_str.lower().title())
    print ('=====================')

    # 개수, 인덱스
    print ('\n=====================')
    print ('count "t": %s' % test_str.count('t'))
    print ('index "t": %s' % test_str.index('t'))
    print ('=====================')

    # 문자열 속성
    print ('\n=====================')
    space_str = '   '
    str_str = 'TestString'
    str_with_space_str = 'Test String'
    int_str = '123'
    float_str = '123.45'
    print ('plain: %s' % str_str)
    print ('isspace: %s' % str_str.isspace())
    print ('isalpha: %s' % str_str.isalpha())
    print ('isalnum: %s' % str_str.isalnum())
    print ('')
    print ('plain: %s' % str_with_space_str)
    print ('isspace: %s' % str_with_space_str.isspace())
    print ('isalpha: %s' % str_with_space_str.isalpha())
    print ('isalnum: %s' % str_with_space_str.isalnum())
    print ('')
    print ('plain: %s' % space_str)
    print ('isspace: %s' % space_str.isspace())
    print ('isalnum: %s' % space_str.isalnum())
    print ('')
    print ('plain: %s' % int_str)
    print ('isdigit: %s' % int_str.isdigit())
    print ('isdeciaml: %s' % int_str.isdecimal())
    print ('isalnum: %s' % int_str.isalnum())
    print ('')
    print ('plain: %s' % float_str)
    print ('isdigit: %s' % float_str.isdigit())
    print ('isdeciaml: %s' % float_str.isdecimal())
    print ('isalnum: %s' % float_str.isalnum())
    print ('=====================')

    # 문자열 다듬기
    print ('\n=====================')
    test_str = ' Test String 1234 !@#$ '
    print ('plain: %s' % test_str)
    print ('lstrip: %s' % test_str.lstrip())
    print ('rstrip: %s' % test_str.rstrip())
    print ('strip %s' % test_str.strip())
    print ('=====================')

    # 문자열 분리
    print ('\n=====================')
    test_str = ' Test String 1234 !@#$ '
    print ('plain: %s' % test_str)
    print ('split: %s' % test_str.split(' '))

    test_str = '''
        1st test world
        2nd test world
    '''
    print ('plain: %s' % test_str)
    print ('splitlines: %s' % test_str.splitlines())
    print ('=====================')

    # 문자열 변경
    print ('\n=====================')
    test_str = ' red blue black yellow '
    print ('plain: %s' % test_str)
    print ('replace: %s' % test_str.replace('black', 'green'))
    print ('replace: %s' % test_str.replace('yellow', ''))
    
    test_str = ' Test String 1234 !@#$ '
    print ('plain: %s' % test_str)
    print ('replace: %s' % test_str.replace(' ', ''))
    print ('=====================')

if __name__ == '__main__':
    main()