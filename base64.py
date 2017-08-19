import os.path                                                                  # os.path module을 사용하기 위함 (경로 지정)
import sys                                                                      # sys.argv 리스트 생성을 위함
import base64                                                                   # base64 encoding, decoding을 위함

# help
def usage():
    print("./FilenNme.py [Option(-e:encode,-d:decode)] Inputfile Outputfile")

# 경로 지정
def abs_path():
    path = os.path.dirname(os.path.abspath(__file__))                           #__file__ == 현재실행하고있는 파일이다.
    return (path)                                                               # 지역 변수가 스텍에 사용된다. 함수에서도 똑같이 스택프레임에서만 사용 가능하다.
                                                                                # 절때 함수 밖에서 사용이 불가능하다. 즉, 함수에서 구한 값을 밖에서 사용하고 싶을 때 return값을 사용한다.
                                                                                # path( 파일을 업로드하기 위한 경로값에 들어있는 변수)를 밖에서 사용하기 위해 return (path)를 사용한다.
# encoding
def encoded_text(path):
    encoded = base64.b64encode(path)                                            # base64 encodiong을 하기 위함
    return (encoded)                                                            # 위에 return (path)설명과 동일하다.

# decoding    
def decoded_text(path):
    decoded = base64.b64decode(path)                                            # base64 decodiong을 하기 위함
    return (decoded)                                                            # 위에 return (path)설명과 동일하다.

# 출력 파일 내용쓰기
def output_write(output_f,text):
    output_f.write(text)                                                         # text file에 내용을 쓰기 위함

# main
if __name__=="__main__":
    option = sys.argv[1]                                                        # path.py이라는 명령을 다음을 기준으로 sys.argv리스트 요소를 사용하여 path.py 다음에 옵션을 사용할 수 있도록 사용한다.
    input_text = sys.argv[2]                                                    # 위의 sys.argv 설명과 동일하며, 옵션 다음의 리스트 사용.
    output_flag = sys.argv[3]                                                   # 위의 sys.argv 설명과 동일하며, 입력받는 text파일 다음의 리스트 사용.
    if output_flag == "-o":                                                     # 파일 출력을 위해 "-o"라는 문자열 인식
        output_text = sys.argv[4]                                               # 위의 sys.argv 설명과 동일하며, 입력받는 text파일 다음 출력값 저장을 위한 text 생성
        output_path = os.path.join(abs_path(), output_text)                     # 출력파일의 저장을 위한 저장경로를 설정하기 위함
        with open (input_text, 'rb') as input_t:                                # encoding하고자 하는 text파일을 불러옴
            with open(output_text, 'wb') as output_t:                           # encoding한 결과값을 text파일에 저장
                if option == "-e":                                              # encoding을 위해"-e" 라는 문자열 인식
                    output_write(output_t, encoded_text(input_t.read()))        # encoded_text()함수를 이용하여 path경로에 저장된 text파일에 encoding된 내용을 작성
                elif option == "-d":                                            # "-d" 라는 문자열 인식
                    output_write(output_t, decoded_text(input_t.read()))        # encoded_text()함수를 이용하여 path경로에 저장된 text파일에 decoding된 내용을 작성
                else:
                    print ("Error")                                             # 다른 문자열 입력시 "Error" 메시지 출력
    else:
        usage()                                                                 # 프로그램 사용 방법이 틀릴 시 사용법 출력하는 에러제어
        sys.exit(1)                                                             # 강제로 스크립트 종료 (ctrl+z or ctrl+D를 눌러서 대화형 인터프리터를 종료하는 것과 같은 기능), # 프로그램 잘못 사용시 종료
                                                                                

                    
'''
# <base64 encoding & decoding program 작성 과정 및 실패사례>

# 1. 경로 설정 test과정
def join_basename():
    path1 = os.path.join(os.path.basename("C:\\Users\\00whd\\Desktop\\BoB\\python"), "plain.txt")
    print (path1)
    
def lasttest():
    path3 = os.path.join(os.path.basename(os.path.abspath("python")), "plain.txt")
    print (path3)

    # 해당 과제를 수행하기 위해 os.path.join, os.path.basename, os.path.abspath의 출력값을 테스트하였다.
    # 테스트 후 해당 결과값을 확인하고 abs_path()에 사용된 path2, path에 활용된 내용을 도출하였다.

path = os.path.join(abs_path(), "plain.txt")
path3 = os.path.join(abs_path(), "encode.txt")
'''
    
'''
# 2. 파일 불러오고 쓰기 위한 과정(실패사례)
def output_encode(output):
    output = sys.argv[2]
    if output == "plain.txt":
        output.write(encoded)
        return output
    else:
        print("Error")

def output_decode(output):
    output = sys.argv[2]
    if output == "encode.txt":
        output.write(decoded)
        return output
    else:
        print("Error")

# Reference
[1] os.path module
http://devanix.tistory.com/298
[2] sys module
https://wikidocs.net/29
[3] 외장함수
https://wikidocs.net/33
'''
