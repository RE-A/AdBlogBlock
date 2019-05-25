import sys
#sys.exit 사용 위함
def read_blogData(): #정확하게 할려면 readLine하고 'pic :'이란 형태가 나타나면 읽기를 그만 두는 것으로.( pic : 부터는 따로 데이터를 추출해서 저장하던가 하는 편이 완벽할 듯 하다.
    f = open('blogData.txt', 'r')
    blogData = f.read().split()
    print(blogData)
    i = 0
    temp= []
    while i < blogData.index('pics'):
        temp.append(blogData[i])
        i+=1
        
    return temp

def read_positiveDic():
    f =  open('positiveDic.txt', 'r')
    data = f.readlines()
    data_t = []
    for ii in data:
        data_t.append(ii[:-1])
    return data_t

def read_negativeDic():
    f = open('negativeDic.txt', 'r')
    data = f.readlines()
    data_t = []
    for ii in data:
        data_t.append(ii[:-1])
    return data_t

def read_advWordDic():
    f = open('advWordDic.txt', 'r')
    data = f.readlines()
    data_t = []
    for ii in data:
        data_t.append(ii[:-1])
    return data_t


"-----------------------------------------main함수 시작하는 곳-----------------------------------------------"


"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@데이터 정리하는 곳@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
"블로그데이터 가져와서 blogData에 넣기"
blogData = read_blogData()
print(blogData)
"긍정적 단어들 list에 쪼개서 넣기"
positiveWordLIst = read_positiveDic()
print(positiveWordLIst)

"부정적 단어들 list에 쪼개서 넣기"
negativeWordLIst = read_negativeDic()
print(negativeWordLIst)

"광고확실한 단어들 list에 쪼개서 넣기"
advWordList = read_advWordDic()
print(advWordList)

"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@단어 체크@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
"총단어 수 세기-> 전제: 블로그에 한 단어라도 있다"
totalWordNum = len(blogData)

"긍정적 단어 수 세기"
positiveNum = 0
for word in positiveWordLIst:
    if blogData[0].find(word) != -1:
        if word != '':
            positiveNum += blogData[0].count(word)
            "총 커서수(?)가 세어져서->글자수+1개를 세서 빼게 되었다."
    else:
        continue

"부정적 단어 수 세기"
negativeNum = 0
for word in negativeWordLIst:
    if blogData[0].find(word) != -1:
        if word != '':
            negativeNum += blogData[0].count(word)
            "총 커서수(?)가 세어져서->글자수+1개를 세서 빼게 되었다."
    else:
        continue

"광고확정 단어 수 세기"
advWordNum = 0
for word in advWordList:
    if blogData[0].find(word) != -1:
        if word != '':
            advWordNum += blogData[0].count(word)
            "총 커서수(?)가 세어져서->글자수+1개를 세서 빼게 되었다."
            break;
    else:
        continue


"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@각각의 단어 수 출력@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print("본문 속 총 단어 수는 ")
print(totalWordNum)
print("본문 속 긍정적 단어 수는 ")
print(positiveNum)
print("본문 속 부정적 단어 수는 ")
print(negativeNum)
print("본문 속 광고확정 단어 수는 ")
print(advWordNum)
print("\n\n")
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@이후 가중치 임의설정, 실험@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2"

try:
    ratio = positiveNum/negativeNum
except ZeroDivisionError:
    ratio = positiveNum



if advWordNum > 0:
    print("광고가 확실합니다\n")
    sys.exit()
if ratio > 6 or advWordNum > 0:

    print("긍정단어/부정단어")
    print(positiveNum/(negativeNum + 1))
    print("광고확정단어수")
    print(advWordNum)
    print("광고글일 확률이 높음")
else:
    print("긍정단어/부정단어")
    print(positiveNum / (negativeNum + 1))
    print("광고확정단어수")
    print(advWordNum)
    print("광고글일 확률이 낮음")