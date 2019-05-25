
def read_blogData():
    f = open('blogData.txt', 'r')
    blogData = f.readlines()
    f.close()
    return blogData

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
totalWordNum = blogData[0].count(' ') + 1

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

if positiveNum/(negativeNum + 1) > 6 or advWordNum > 0:
    "negativeNum이 0개일 경우에 대비하여 +1하였음"
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