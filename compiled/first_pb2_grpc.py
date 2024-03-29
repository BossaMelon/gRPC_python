# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import first_pb2 as first__pb2


class FirstGreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/proto.FirstGreeter/SayHello',
        request_serializer=first__pb2.HelloRequest.SerializeToString,
        response_deserializer=first__pb2.HelloReply.FromString,
        )
    self.SayNum = channel.unary_unary(
        '/proto.FirstGreeter/SayNum',
        request_serializer=first__pb2.NumRequest.SerializeToString,
        response_deserializer=first__pb2.HelloNum.FromString,
        )


class FirstGreeterServicer(object):
  """The greeting service definition.
  """

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayNum(self, request, context):
    """Another one
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FirstGreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=first__pb2.HelloRequest.FromString,
          response_serializer=first__pb2.HelloReply.SerializeToString,
      ),
      'SayNum': grpc.unary_unary_rpc_method_handler(
          servicer.SayNum,
          request_deserializer=first__pb2.NumRequest.FromString,
          response_serializer=first__pb2.HelloNum.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.FirstGreeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
