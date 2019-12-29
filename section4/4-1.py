import pickle #(객체 , 테스트) 직렬화, 역직렬화


# 파일 이름과 데이터
bfilename = '/Users/dkkim/Documents/section4/test.bin'
tfilename = '/Users/dkkim/Documents/section4/test.txt'

data1 = 77
data2 = "Hello world"
data3 = ["car","apple","house"]

#바이너리 쓰기
with open(bfilename,'wb') as f:
    pickle.dump(data1,f)  #dump는 객체를 바이너리화 (직렬화) #dumps 는 문자열을 직렬화
    pickle.dump(data2,f)
    pickle.dump(data3,f)

#텍스트 쓰기
with open(tfilename, 'wt') as f: #wt write text
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')  #write 는 텍스트형태만 쓸수 있다
    f.writelines('\n'.join(data3))   #문자열 쓸땐 그냥 data3만 쓰면 carapplehouse 이런식으로 나와서 \n을 조인해줌


#바이너리 읽기
with open(bfilename,'rb') as f:   #rb read binary
    #load는 객체를 역직렬화 #loads 는 문자열읽어옴
    b = pickle.load(f)
    print(type(b), ' Binary Read1 |',b)
    b = pickle.load(f)
    print(type(b), ' Binary Read2 |' ,b)
    b = pickle.load(f)
    print(type(b), 'Binary Read3 |', b)

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i,line in enumerate(f,1):
        print(type(line),'Text Read' + str(i) + '  |   ',line)
