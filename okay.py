import socket

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err))

 
port = 443

for res in socket.getaddrinfo('www.example.com', port, socket.AF_INET, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s.connect(sa)
        print ("scientists discover the hi")
    except socket.error as msg:
        print("scientists did not discover the hi")
        s.close()
        s = None
        continue
    break

