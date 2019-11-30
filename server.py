import grpc
import first_pb2_grpc
import first_pb2
from concurrent import futures


# service名字影响父类名字
class Greeter(first_pb2_grpc.FirstGreeterServicer):
    # override父类方法
    # 定义每个service功能的具体实现

    def SayHello(self, request, context):
        # 输入参数主要是第二个,此函数在proto定义中有的request只有name字段

        result = "Fuck you " + request.name
        # 处理输入的name字段
        print("来了老弟")
        return first_pb2.HelloReply(message=result)
        # 返回结果

    def SayNum(self, request, context):
        print("嘿嘿")
        return first_pb2.HelloNum(num=int(request.length)-5)


def serve():
    # 建立server对象
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册service对象
    first_pb2_grpc.add_FirstGreeterServicer_to_server(Greeter(), server)
    # 指定监听ip+port
    server.add_insecure_port('localhost:50051')
    server.start()
    print("Waiting for client...")
    server.wait_for_termination()
    # animation.waiting_animation(0.5)


if __name__ == '__main__':
    serve()
