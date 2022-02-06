import grpc

from client.service import protocol_pb2, protocol_pb2_grpc
from client import config


class Client:
    def __init__(self):
        self.insecure_channel = grpc.insecure_channel(config.GRPC_URL)
        self.auth_stamp = protocol_pb2_grpc.AuthStub(self.insecure_channel)
        self.message_stamp = protocol_pb2_grpc.MessengerStub(self.insecure_channel)

    def auth(self, login: str, password: str) -> str:
        response = self.auth_stamp.Auth(protocol_pb2.AuthRequest(username=login, password=password))
        return response.token

    def register(self, login: str, password: str) -> str:
        response = self.auth_stamp.Register(protocol_pb2.RegisterRequest(username=login, password=password))
        return response.token

    def send_message(self, token: str, message: str) -> str:
        metadata = (('Authorization', 'Bearer' + token),)
        response = self.message_stamp.PingRequest(protocol_pb2.Ping(message=message), metadata=metadata)
        return response.message
