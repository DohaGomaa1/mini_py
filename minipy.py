
def customized_find (sentaces,character):
    return [x for x ,j in list (enumerate(sentaces)) if j==character]

def customized_split (sentence,character):
    lst=customized_find(sentence,character)
    string=''
    final=[]
     #lst.remove('b')
        
    string=sentence[:lst[0]]
    final.append(string)
    for x in range(len(lst)-1):
        string=sentence[lst[x]+1:lst[x+1]]
        final.append(string)
    string=sentence[lst[-1]+1:]
    final.append(string)
    
    return final
