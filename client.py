from __future__ import print_function
import grpc
import first_pb2
import first_pb2_grpc
import time
from util import ipcheck
import dependency


def run():
    # ip = ipcheck.get_host_ip()
    ip = "localhost"
    port: str = "50051"
    socket = ip+":"+port
    channel = grpc.insecure_channel(socket)
    # 设定发送ip和port

    stub = first_pb2_grpc.FirstGreeterStub(channel)
    # 新建client对象

    while True:
        response = stub.SayHello(first_pb2.HelloRequest(name=' you'))
        # 对象.service对应功能(message文件.对应message(字段赋值))
        # 类似调用service的函数
        response2 = stub.SayNum(first_pb2.NumRequest(length="15"))

        print("received: " + response.message)
        print("Length= : " + str(response2.num))

        time.sleep(1)


if __name__ == '__main__':
    run()
