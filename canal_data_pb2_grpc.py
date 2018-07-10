# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import canal_data_pb2 as canal__data__pb2


class SendingImageDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sendImageData = channel.unary_unary(
        '/imageviewer.SendingImageData/sendImageData',
        request_serializer=canal__data__pb2.ImageDataMessage.SerializeToString,
        response_deserializer=canal__data__pb2.ServerConfirmation.FromString,
        )


class SendingImageDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sendImageData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SendingImageDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sendImageData': grpc.unary_unary_rpc_method_handler(
          servicer.sendImageData,
          request_deserializer=canal__data__pb2.ImageDataMessage.FromString,
          response_serializer=canal__data__pb2.ServerConfirmation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'imageviewer.SendingImageData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SendingMouseDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sendMouseData = channel.unary_unary(
        '/imageviewer.SendingMouseData/sendMouseData',
        request_serializer=canal__data__pb2.MouseMessage.SerializeToString,
        response_deserializer=canal__data__pb2.ServerConfirmation.FromString,
        )


class SendingMouseDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sendMouseData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SendingMouseDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sendMouseData': grpc.unary_unary_rpc_method_handler(
          servicer.sendMouseData,
          request_deserializer=canal__data__pb2.MouseMessage.FromString,
          response_serializer=canal__data__pb2.ServerConfirmation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'imageviewer.SendingMouseData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SendingQuakeEventStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sendQuakeEventData = channel.unary_unary(
        '/imageviewer.SendingQuakeEvent/sendQuakeEventData',
        request_serializer=canal__data__pb2.QuakeEventMessage.SerializeToString,
        response_deserializer=canal__data__pb2.ServerConfirmation.FromString,
        )
    self.sendInjuryData = channel.unary_unary(
        '/imageviewer.SendingQuakeEvent/sendInjuryData',
        request_serializer=canal__data__pb2.InjuryDataMessage.SerializeToString,
        response_deserializer=canal__data__pb2.ServerConfirmation.FromString,
        )


class SendingQuakeEventServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sendQuakeEventData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendInjuryData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SendingQuakeEventServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sendQuakeEventData': grpc.unary_unary_rpc_method_handler(
          servicer.sendQuakeEventData,
          request_deserializer=canal__data__pb2.QuakeEventMessage.FromString,
          response_serializer=canal__data__pb2.ServerConfirmation.SerializeToString,
      ),
      'sendInjuryData': grpc.unary_unary_rpc_method_handler(
          servicer.sendInjuryData,
          request_deserializer=canal__data__pb2.InjuryDataMessage.FromString,
          response_serializer=canal__data__pb2.ServerConfirmation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'imageviewer.SendingQuakeEvent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
