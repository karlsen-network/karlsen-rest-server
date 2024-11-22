# encoding: utf-8
import asyncio

from karlsend.KarlsendClient import KarlsendClient
# pipenv run python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/rpc.proto ./protos/messages.proto
from karlsend.KarlsendThread import KarlsendCommunicationError


class KarlsendMultiClient(object):
    def __init__(self, hosts: list[str]):
        self.karlsends = [KarlsendClient(*h.split(":")) for h in hosts]

    def __get_karlsend(self):
        for k in self.karlsends:
            if k.is_utxo_indexed and k.is_synced:
                return k

    async def initialize_all(self):
        tasks = [asyncio.create_task(k.ping()) for k in self.karlsends]

        for t in tasks:
            await t

    async def request(self, command, params=None, timeout=5):
        try:
            return await self.__get_karlsend().request(command, params, timeout=timeout)
        except KarlsendCommunicationError:
            await self.initialize_all()
            return await self.__get_karlsend().request(command, params, timeout=timeout)

    async def notify(self, command, params, callback):
        return await self.__get_karlsend().notify(command, params, callback)
