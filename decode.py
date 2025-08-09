from encode import caeser_encode

def caeser_decode(encrypted_text,key):
    arr = caeser_encode(encrypted_text,-key)
    return arr 