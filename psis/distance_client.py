import grpc
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson
import json

class Client:
    def __init__(self, a,b,c,d,distUnit):
        self.longitudOrigen = a
        self.latitudOrigen = b
        self.longitudDestino = c
        self.latitudDestino = d
        self.unidadMedida = distUnit
        self.distancia = None

    def ask_distance(self):
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = pb2_grpc.DistanceServiceStub(channel)

            # a SourceDest contains two Position: source and destination
            message = pb2.SourceDest(
                source=pb2.Position(
                    latitude=self.latitudOrigen, longitude=self.longitudOrigen
                ),
                destination=pb2.Position(
                    latitude=self.latitudDestino, longitude=self.longitudDestino
                ),
                unit=self.unidadMedida
            )

            print(f"Message sent:\n{MessageToJson(message)}\n")

            # call remote method
            response = stub.geodesic_distance(message)

            # Imprimir la respuesta completa para depuración
            response_json = MessageToJson(response)
            print(f"Respuesta completa del servidor: {response_json}")

            # call remote method
            response = stub.geodesic_distance(message)
            try:
                self.distancia = json.loads(MessageToJson(response))["distance"]
                print("-----Response-----")
                print("Distance:", json.loads(MessageToJson(response))["distance"])
                print("Method:", json.loads(MessageToJson(response))["method"])
                print("Distance unit:", json.loads(MessageToJson(response))["unit"])
            except KeyError:
                print("One or more key are missing!")