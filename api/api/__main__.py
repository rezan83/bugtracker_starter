"""Application entry point to start the test API."""
import os

from ._api import run

HOST = os.environ.get('HOST', 'localhost')
PORT = int(os.environ.get('PORT', 8000))


if __name__ == '__main__':
    run(HOST, PORT)
