import matplotlib.pyplot as plt 
def number_array(initial,final):
    arr = []
    for i in range(initial,final+1):
        arr.append(i)
    return arr
def zero_array(initial,final):
    arr =[]
    for i in range(initial,final+1):
        arr.append(0)
    return arr
def ascii_converter(x):
    arr=[]
    for i in x:
        arr.append(chr(i))
    return arr

para = input("Enter the paragraph: ")
x = number_array(65,90)
y = zero_array(1,26)
para= para.upper()
for letter in para:
    i=0
    while i<26:
        if ord(letter) == x[i]:
            y[i]+=1
        i+=1
x_new = ascii_converter(x)
plt.plot(x_new,y)
plt.show()