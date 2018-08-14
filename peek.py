"""Pry into python code."""

import code


def peek():
    """Opens interactive console at the point of invocation."""
    code.interact(local=dict(globals(), **locals()))
