from base64 import encode
from email import message
import socket
import random
from cryptography.fernet import Fernet
import hashlib
import pickle
import hmac
from pyparsing import ExceptionWordUnicode
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 1234))
l=[]
done = False

while not done:
    msg = (client.recv(1024))
    msg = pickle.loads(msg)
    key = Fernet(msg[0])
    enc = msg[1]
    sha = msg[2]
    salt = msg[3]
    hmac1 = msg[4]
    decrypt = (key.decrypt(enc)).decode('utf-8')
    inp = hashlib.sha512(decrypt.encode())
    inp = inp.hexdigest()
    rec_hmac=hmac1
    h = hmac.new(key=salt.encode(),msg=decrypt.encode(),digestmod="sha512")
    h = h.hexdigest()
    if msg == 'quit':
        done = True
    else:
        print(decrypt)
    message = input("Message:")
    d="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    key = Fernet.generate_key()
    l.append(key)
    fernet_obj = Fernet(key)
    encrypted_message = fernet_obj.encrypt(message.encode())
    l.append(encrypted_message)
    res = hashlib.sha512(message.encode())
    res = res.hexdigest()
    l.append(res)
    s=[]
    for i in range(12):
        s.append(random.choice(d))
    app_salt=(''.join(salt))
    l.append(app_salt)
    h = hmac.new(key=app_salt.encode(),msg=message.encode(),digestmod="sha512")
    h=h.hexdigest()
    l.append(h)
    d = pickle.dumps(l)
    client.send(d)

    
client.close()