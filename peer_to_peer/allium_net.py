import asyncio
import socket

def get_ip():
    """Return the IP of the user as string"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.google.com', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

class Client() :
    
    def __init__(self):
        pass
    async def tcp_echo_client(self, message, loop, server_IP):
        reader, writer = await asyncio.open_connection(server_IP, 8888, loop = loop)
    
        writer.write(message.encode())

        data = await reader.read(100)

        writer.close()

class Server() :

    def __init__(self):
         
        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(the_server.handle_echo, '', 8888, loop = loop)
        server = loop.run_until_complete(coro)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

    async def handle_echo(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        writer.write(data)
        await writer.drain()

        writer.close()

role = int(input("Welcome to the echo server. Choose 1 for Client or 2 for Server"))

if role == 2 :
    the_server = Server()
if role == 1 :
    the_client    = Client()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(the_client.tcp_echo_client(input("Please provide input\n"),loop))
    loop.close()
