# 파일 입출력
#f = open("a\\test.txt" , "w") #역슬레시 쓸라면 두번\\써야함. 역슬레시 기능때문
# open(A,B)
# A 경로를 포함한 파일이름
# B 권한

# 절대경로 : 드라이브로 부터의 경로 ( c:\  d:\  e:\ )
# 상대경로 : 현재경로를 기준으로 하는 경로

# testa 폴더 안에 a.png 생성, testb 폴더 안에 b.mp3 ,
# testc 폴더 안에 c.avi 생성

# f = open("testa/a.png",'w')
# f = open("testa/testb/b.mp3",'w')
# f = open("C:/Users/KGITBank/OneDrive/바탕 화면/python이건/testa/testb/testc/c.avi",'w') #절대경로로 만들어봄, \는 /로 바꿈. 파이선에서 읽기 어려운 역슬레시이기에

# # open(A,B)
# # 권한 별 주의사항
# # r(ead)   읽기 > 있는파일읽으세요..!  (경로문제때문에!!)
# f = open("testa/testb/b.mp3", "r")
# # w(rite) 새로쓰기 > 없는파일이름 지정(생성) 있는파일이름 지정(갱신)
# f = open("kgitbank.txt", "w")
# # a(ppend)

# w!
# f=open("test.txt","w")
# f.write("hello") 

# for i in range(100):
#     f=open("test.txt",'w')
#     f.write("hello\n")  #위아래 차이는? hello 한번입력.계속 새로 저장되니

# f=open("test.txt","w")
# for i in range(100):
#     f.write("hello\n") #이건 파일을 만들고 i를 돌리니 hello가 100번 써짐.

# ----------------------------------------------------------------------------------------------------
# 구구단폴더 생성! 코드 실행시 구구단 폴더아래
#2단.txt ~ 9단.txt 생성되어야 하며
#각각의 파일에는 구구단이 출력되어야함


for i in range(2,10):
    f = open(f"99dan/{i}단.txt","w")
    for j in range(1,10):
        f.write(f"{i}x{j} = {i*j}\n")
