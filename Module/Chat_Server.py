import socket
import pyaudio
import threading

class Chat_Server():

    def __init__(self,setPort,setChunk, setChannels, setRate):
        self.Host = socket.gethostbyname(socket.gethostname())
        self.Port = setPort
        self.Address = f"{self.Host} : {self.Port}"
        self.audio = pyaudio.PyAudio()
        self.Chunk = setChunk
        self.Format = pyaudio.paInt16
        self.Channels = setChannels
        self.Rate = setRate
        self.Clients = []
        self.stream = self.audio.open(format=self.Format, channels=self.Channels, rate=self.Rate, input=True)
        self.StartServer()

    def Open(self,Host_Server):
        while True:
            try:
                connection , address = Host_Server.accept()
                Client_Thread = threading.Thread(target=self.Handle,args=(connection,address))
                Client_Thread.start()
                self.Clients.append(connection)
                print(self.Clients)
                print(f"Connect from {address[0]} : {str(address[1])}")
            except Exception as Errr:
                raise  Errr

    def Handle(self,Cleint,ClientAddress):
        Cleint.send(f"Connect to {self.Address}".encode("utf-8"))

    def StartServer(self):
        with socket.socket() as Server:
            try:
                Server.bind((self.Host,self.Port))
                Server.listen()
                print(f"Server hosted at [{self.Address}]")
                Listener_Thread = threading.Thread(target=self.Open,args=(Server,))
                Listener_Thread.start()
                print("Listener Client")
                while True:
                    MicrophoneInput = self.stream.read(self.Chunk)
                    for Client in self.Clients:
                        Client.send(MicrophoneInput)
            except Exception as Errr:
                raise Errr