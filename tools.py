import matplotlib.pyplot as plt 

def frequency_analyser(s):
    s = s.upper()
    arr = [0]*26
    for i in s:
        if(i.isalpha()):
            key = ord(i)-ord('A')
            arr[key]+=1
    return arr

def frequency_analyser(s,num):
    a = []
    s = s.upper()
    arr = [0]*26
    for i in s:
        if(i.isalpha()):
            key = ord(i)-ord('A')
            arr[key]+=1
    for i in range(num):
        m1 = max(arr)
        index = arr.index(m1)
        a.append(index)
        arr[index] = 0 
    return a


def plot(x,y,x_label,y_label):
    plt.plot(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
