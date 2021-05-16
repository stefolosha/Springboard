import collections
def letter_idx(dic):
    dic = str(dic).lower()
    diction = collections.defaultdict(list)
    lis = []
    for letter, i in enumerate(dic):
        if i in ['a' , 'e', 'i', 'o', 'u', 'y']:
            lis.append([i,letter])
    for item in lis:
        diction[item[0]].append(item[1])
    print(dict(diction))

letter_idx('hallu duaer')