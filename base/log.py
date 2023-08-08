from base.public import publicmethod
import logging

class Logger():
    def __init__(self,*filename):
        self.file = publicmethod().get_path(*filename)

    def logger(self):
        logger = logging.getLogger('Mylog')
        logger.setLevel(logging.WARN)

        handdler1 = logging.StreamHandler()
        handdler2 = logging.FileHandler(self.file,encoding='utf-8')

        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d:%(message)s"
        formatter = logging.Formatter(fmt)

        handdler1.setFormatter(formatter)
        handdler2.setFormatter(formatter)

        logger.addHandler(handdler1)
        logger.addHandler(handdler2)

        return logger

Log = Logger('log','log')

if __name__ == "__main__":
    log = Log.logger()
    log.warning('2222')