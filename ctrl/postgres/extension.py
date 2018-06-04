
from zope import component

from ctrl.core.extension import CtrlExtension
from ctrl.core.interfaces import (
    ICommandRunner, ICtrlExtension, IDatactl, ISubcommand)

from .client import PostgresClient
from .command import PostgresSubcommand


class CtrlPostgresExtension(CtrlExtension):

    @property
    def requires(self):
        return ['config', 'command']

    def register_adapters(self):
        component.provideAdapter(
            factory=PostgresSubcommand,
            adapts=[ICommandRunner],
            provides=ISubcommand,
            name='postgres')

    async def register_utilities(self):
        component.provideUtility(
            PostgresClient(),
            IDatactl,
            name='postgres')


# register the extension
component.provideUtility(
    CtrlPostgresExtension(),
    ICtrlExtension,
    'postgres')
