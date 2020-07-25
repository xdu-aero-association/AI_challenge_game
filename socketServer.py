# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:37:10 2020

@author: asus
"""

from socket import *


    IP = '127.0.0.1'
    PORT = 50000
    BUFLEN = 1024 # 一次从socket缓冲区最多读入1024个字节数据
    
    #
    listenSocket = socket(AF_INET, SOCK_STREAM)
    listenSocker.bind((IP,PORT))
    
    #开启监听
    listenSocket.listen(2)
    print('服务端成功启动，等待连接...')
    
    #进行连接
    dataSocket,address = listenSocket.accept()
    print('接受一个客户端的连接：', address)
    
    while True:
        recved = dataSocket.recv(BUFLEN)
        if not recved:
            break
       info = recved.decode()
        print(f'收到信息：{info}')
        #toSend = self.data.encode()
        #dataSocket.send(soSend)
    
    dataSocket.close()
    listenSocket.close()
