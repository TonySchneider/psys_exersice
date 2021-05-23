#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__licence__ = 'GPL'
__version__ = '0.0.1'
__author__ = 'Tony Schneider'
__email__ = 'tonysch05@gmail.com'

import requests
import sys
import logging

logging.basicConfig (level=logging.INFO, format='%(asctime)s | %(levelname)-10s | %(message)s', stream=sys.stdout)


def ping(ip: str, port: str) -> bool:
    res_bool = False
    try:
        response = requests.get(
            url=f"http://{ip}:{port}",
        )
        response.raise_for_status()
        if response.status_code == 200:
            res_bool = True
    except Exception as e:
        logging.error(e.__str__())

    return res_bool


def main(*args, **kwargs) -> int:
    try:
        logging.info('Starting bot... Press CTRL+C to quit.')
        ip, port = args[0], args[1]
        logging.info(f"Connected successfully to {ip}:{port}!" if ping(ip, port) else f"Failed to connect {ip}:{port}")
    except KeyboardInterrupt:
        logging.info('Quitting... (CTRL+C pressed)')
        return 0
    except Exception:   # Catch-all for unexpected exceptions, with stack trace
        logging.exception(f'Unhandled exception occurred!')
        return 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
