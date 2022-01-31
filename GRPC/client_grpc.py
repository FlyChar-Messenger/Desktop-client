import grpc

from service import service_pb2_grpc
from service import service_pb2


class Client:
    def __init__(self):
        self.insecure_channel = grpc.insecure_channel('platun0v.ru:49578')
        self.auth_stamp = service_pb2_grpc.AuthStub(self.insecure_channel)

    def auth(self, login, password):
        response = self.auth_stamp.Auth(service_pb2.AuthRequest(username=login, password=password))
        print(response.token)
        return response.status, response.token

    def register(self, login, password):
        response = self.auth_stamp.Register(service_pb2.RegisterRequest(username=login, password=password))
        return response.status, response.token
