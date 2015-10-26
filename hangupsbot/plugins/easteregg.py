import random
import asyncio

import plugins


def _initialise(bot):
    plugins.register_user_command(["easteregg"])


def easteregg(bot, event, easteregg, eggcount=1, period=0.5, *args):
    """starts hangouts easter egg combos.
    supply three parameters: easter egg trigger name, number of times, period (in seconds).
    supported easter egg trigger name: ponies , pitchforks , bikeshed , shydino
    """

    for i in range(int(eggcount)):
        yield from bot._client.sendeasteregg(event.conv_id, easteregg)
        if int(eggcount) > 1:
            yield from asyncio.sleep(float(period) + random.uniform(-0.1, 0.1))
