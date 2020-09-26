import socket
import pyaudio


class Chat_Client():

    def __init__(self,setChunk, setChannels, setRate):
        self.audio = pyaudio.PyAudio()
        self.Chunk = setChunk
        self.Format = pyaudio.paInt16
        self.Channels = setChannels
        self.Rate = setRate

    def Open(self,address,port):
        self.Chat = self.audio.open(format=self.Format, channels=self.Channels, rate=self.Rate, output=True)
        with socket.socket() as Client:
            Client.connect((address,port))
            print(Client.recv(2048).decode('utf-8'))
            while True:
                data = Client.recv(self.Chunk)
                self.Chat.write(data)
