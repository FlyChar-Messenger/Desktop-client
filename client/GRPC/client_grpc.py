import grpc

from client.service import protocol_pb2, protocol_pb2_grpc


class Client:
    def __init__(self):
        self.insecure_channel = grpc.insecure_channel('platun0v.ru:49578')
        self.auth_stamp = protocol_pb2_grpc.AuthStub(self.insecure_channel)
        self.message_stamp = protocol_pb2_grpc.MessengerStub(self.insecure_channel)
        self.token = ""

    def auth(self, login, password):
        response = self.auth_stamp.Auth(protocol_pb2.AuthRequest(username=login, password=password))
        self.token = response.token
        print(self.token)
        return 0

    def register(self, login, password):
        response = self.auth_stamp.Register(protocol_pb2.RegisterRequest(username=login, password=password))
        self.token = response.token
        return 0

    def send_message(self, message):
        metadata = (('Authorization', 'Bearer' + self.token))
        response = self.message_stamp.PingRequest(protocol_pb2.Ping(message=message), metadata=metadata)
        return response.message