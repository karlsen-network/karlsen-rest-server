# encoding: utf-8

from karlsend.KarlsendThread import KarlsendThread


# pipenv run python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/rpc.proto ./protos/messages.proto

class KarlsendClient(object):
    def __init__(self, karlsend_host, karlsend_port):
        self.karlsend_host = karlsend_host
        self.karlsend_port = karlsend_port
        self.server_version = None
        self.is_utxo_indexed = None
        self.is_synced = None
        self.p2p_id = None

    async def ping(self):
        try:
            info = await self.request("getInfoRequest")
            self.server_version = info["getInfoResponse"]["serverVersion"]
            self.is_utxo_indexed = info["getInfoResponse"]["isUtxoIndexed"]
            self.is_synced = info["getInfoResponse"]["isSynced"]
            self.p2p_id = info["getInfoResponse"]["p2pId"]
            return info

        except Exception as exc:
            return False

    async def request(self, command, params=None, timeout=5):
        with KarlsendThread(self.karlsend_host, self.karlsend_port) as t:
            return await t.request(command, params, wait_for_response=True, timeout=timeout)

    async def notify(self, command, params, callback):
        t = KarlsendThread(self.karlsend_host, self.karlsend_port, async_thread=True)
        return await t.notify(command, params, callback)
