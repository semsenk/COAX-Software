import hashlib

s = "Python Bootcamp"
#hashing string using hash()
def hash_data(data):
    hashed_data = hash(data)
    return hashed_data

print(hash_data(s))

#hashing string using MD5 algorithm
def md5_func(data):
    hashed_data = hashlib.md5(data.encode())
    return hashed_data.hexdigest()

print(md5_func(s))

 
