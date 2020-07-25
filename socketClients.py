# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:00:41 2020

@author: asus
"""

from socket import *

def socketClients():
    IP = '192.168.2.111'#填写设备的网段，确认是否正确
    SERVER_PORT = 50000 #端口
    BUFLEN = 1024
        
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((IP,SERVER_PORT))
    
    def sendData(data):
        toSend = data.encode()
        dataSocket.send(soSend)
    
    def socketClosed():
        dataSocket.close()
        #True:
        #需要调用一个开关参数设定socket的开关，目前这个参数不确定 需要查看端侧设备的开关变量
        #recved = dataSocket.recv(BUFLEN)
        #if not recved: 
        #    break
        #data = recved.decode()#所有的数据
        #print(data)
        #processData(data)
    
if __name__ == "__main__":
    socketClients()
        