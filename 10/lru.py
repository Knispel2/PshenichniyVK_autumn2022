from collections import deque
import sys
import logging
import logging.config


log_conf = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(name)s\t%(levelname)s\t%(message)s",
        },
        "complex": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
        },
    },
    "handlers": {
        "simple_log": {
            "level": "NOTSET",
            "stream": sys.stdout,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "complex_log": {
            "level": "NOTSET",
            "filename": "cache.log",
            "class": "logging.FileHandler",
            "formatter": "complex",
        },
    },
    "loggers": {
        "s_complex": {
            "level": "DEBUG",
            "handlers": ["simple_log", "complex_log"],
        },
        "complex": {
            "level": "DEBUG",
            "handlers": ["complex_log"],
        },
    },
}


class MyLRU():

    def __init__(self, logger, limit=42) -> None:
        self.base = deque()
        self.logger = logger
        self.map = {}
        self.limit = limit
        self.logger.debug(f'Limit {limit} now')

    def upper_key(self, key):
        self.logger.debug(f'Upper key {key}')
        self.base.remove(key)
        self.base.append(key)

    def get(self, key):
        if key in self.base:
            self.logger.info(f'Key {key} get!')
            self.upper_key(key)
            return self.map[key]
        self.logger.error(f'Key {key} not exist!')
        return None

    def set(self, key, value):
        if key not in self.base:
            self.logger.info(f'Set not existing key {key}')
        else:
            self.logger.info(f'Set existing key {key}')
            self.map[key] = value
            return None
        if len(self.base) == self.limit:
            if key not in self.base:
                self.logger.info(f'''Set existing key {key},
                                    when capacity is reached''')
            buf = self.base.popleft()
            del self.map[buf]
        self.map[key] = value
        self.base.append(key)
        return None


def run():
    base = sys.argv
    logging.config.dictConfig(log_conf)
    main_logger = logging.getLogger('complex')
    if len(base) > 1:
        if base[1] == '-s':
            main_logger = logging.getLogger('s_complex')
    lru = MyLRU(main_logger, limit=3)
    lru.get(3)
    lru.set(3, 'data')
    lru.set(3, 'buffer')
    lru.set(4, 'data')
    lru.set(5, 'data')
    lru.set(6, 'data')
    lru.get(6)


if __name__ == '__main__':
    run()
