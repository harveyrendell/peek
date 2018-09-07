"""Peek at python code."""

import code
import inspect


def at():
    """Opens interactive console at the point of invocation."""
    code.interact(local=dict(
        inspect.stack()[1][0].f_globals,
        **inspect.stack()[1][0].f_locals
    ))
