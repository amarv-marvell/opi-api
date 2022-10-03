# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend_nvme_tcp_pb2 as backend__nvme__tcp__pb2


class NVMfRemoteControllerServiceStub(object):
    """Back End (network-facing) APIs.

    NVMe/TCP and NVMe/RoCEv2

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NVMfRemoteControllerConnect = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerConnect',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerConnectRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerConnectResponse.FromString,
                )
        self.NVMfRemoteControllerDisconnect = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerDisconnect',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerDisconnectRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerDisconnectResponse.FromString,
                )
        self.NVMfRemoteControllerReset = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerReset',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerResetRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerResetResponse.FromString,
                )
        self.NVMfRemoteControllerList = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerList',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerListRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerListResponse.FromString,
                )
        self.NVMfRemoteControllerGet = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerGet',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerGetRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerGetResponse.FromString,
                )
        self.NVMfRemoteControllerStats = channel.unary_unary(
                '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerStats',
                request_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsRequest.SerializeToString,
                response_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsResponse.FromString,
                )


class NVMfRemoteControllerServiceServicer(object):
    """Back End (network-facing) APIs.

    NVMe/TCP and NVMe/RoCEv2

    """

    def NVMfRemoteControllerConnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerDisconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerReset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NVMfRemoteControllerStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NVMfRemoteControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NVMfRemoteControllerConnect': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerConnect,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerConnectRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerConnectResponse.SerializeToString,
            ),
            'NVMfRemoteControllerDisconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerDisconnect,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerDisconnectRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerDisconnectResponse.SerializeToString,
            ),
            'NVMfRemoteControllerReset': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerReset,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerResetRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerResetResponse.SerializeToString,
            ),
            'NVMfRemoteControllerList': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerList,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerListRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerListResponse.SerializeToString,
            ),
            'NVMfRemoteControllerGet': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerGet,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerGetRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerGetResponse.SerializeToString,
            ),
            'NVMfRemoteControllerStats': grpc.unary_unary_rpc_method_handler(
                    servicer.NVMfRemoteControllerStats,
                    request_deserializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsRequest.FromString,
                    response_serializer=backend__nvme__tcp__pb2.NVMfRemoteControllerStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'opi_api.storage.v1.NVMfRemoteControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NVMfRemoteControllerService(object):
    """Back End (network-facing) APIs.

    NVMe/TCP and NVMe/RoCEv2

    """

    @staticmethod
    def NVMfRemoteControllerConnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerConnect',
            backend__nvme__tcp__pb2.NVMfRemoteControllerConnectRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerDisconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerDisconnect',
            backend__nvme__tcp__pb2.NVMfRemoteControllerDisconnectRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerDisconnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerReset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerReset',
            backend__nvme__tcp__pb2.NVMfRemoteControllerResetRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerResetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerList',
            backend__nvme__tcp__pb2.NVMfRemoteControllerListRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerGet',
            backend__nvme__tcp__pb2.NVMfRemoteControllerGetRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NVMfRemoteControllerStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opi_api.storage.v1.NVMfRemoteControllerService/NVMfRemoteControllerStats',
            backend__nvme__tcp__pb2.NVMfRemoteControllerStatsRequest.SerializeToString,
            backend__nvme__tcp__pb2.NVMfRemoteControllerStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
