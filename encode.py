def caeser_encode(s,key):
    a = ""
    s = s.upper()
    for i in range(len(s)):
        if s[i].isalpha():
            a += chr((ord(s[i])-ord('A')+key)%26 + ord('A'))
        else:
            a += s[i]
    return a