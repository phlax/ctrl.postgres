
from zope import interface

from ctrl.core.interfaces import ISubcommand

from .client import PostgresClient


@interface.implementer(ISubcommand)
class PostgresSubcommand(object):

    def __init__(self, context):
        self.context = context

    async def handle(self, command, *args, loop=None):
        return await getattr(self, 'handle_%s' % command)(*args, loop=loop)

    async def handle_list(self, server_addr, command, *args, loop=None):
        client = PostgresClient(loop, server_addr)
        return await client.list_dbs(command, *args)
