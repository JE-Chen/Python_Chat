import socket

from Module.Chat_Client import Chat_Client

Client = Chat_Client(1024*2,2,44100)

Client.Open(socket.gethostbyname(socket.gethostname()),5555)