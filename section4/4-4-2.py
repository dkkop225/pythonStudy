import simplejson as json

#Dict(json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul',
    'grade':[95,77,66,55,44]
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'liverpool',
    'grade':[124,34,33,22,11]
})
data['people'].append({
    'name':'jeon',
    'website':'daum.com',
    'from':'london',
    'grade':[134,32,23,24,12]
})

#print(data)

#json 파일쓰기(dump)

with open('/Users/dkkim/Documents/section4/member.json','w') as outfile:
    json.dump(data,outfile)


with open('/Users/dkkim/Documents/section4/member.json','r') as infile:
    r= json.load(infile)
    #print(type(r))
    #print(r)
    print("=====================")

    for p in r['people']:
        print('Name:   ' + p['name'])
        print('web:   ' + p['website'])
        print('from:   ' + p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
        print('grade:',grade.lstrip())
        print('')
