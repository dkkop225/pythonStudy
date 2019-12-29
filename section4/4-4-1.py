import simplejson as json

#Dict(json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'liverpool'
})
data['people'].append({
    'name':'jeon',
    'website':'daum.com',
    'from':'london'
})

#print(data)
#{'people': [{'from': 'Seoul', 'website': 'naver.com', 'name': 'Kim'}, {'from': 'liverpool', 'website': 'google.com', 'name': 'park'}, {'from': 'london', 'website': 'daum.com', 'name': 'jeon'}]}

#Dict(json) ->str

e = json.dumps(data, indent=4) #문자열로 변경  인덴트 - 들여쓰기 숫자에 따라 달라짐
#print(type(e))

#str ->Dict(json)
d = json.loads(e)
#print(type(d))


with open('/Users/dkkim/Documents/section4/member.json','w') as outfile:
    outfile.write(e)

with open('/Users/dkkim/Documents/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    print("=========")
    print(type(r))
    print(r)

    for p in r['people']:
        print('Name:   ' + p['name'])
        print('web:   ' + p['website'])
        print('from:   ' + p['from'])
        print('   ')
