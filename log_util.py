import logging

def create_logger(logger_name, print_console = False, use_loggly = False, loggly_api_key = None):
    """
    Create a logger write to file logger_name.log
    :param logger_name: name of the file
    :param print_console: (Default False) True = print log on console (also write to file).
    :param use_loggly: (Default False) Set true if you want to use loggly
    :param loggly_api_key (Default None) Put your loggly api key here
    :return: logger
    """
    FORMAT = '%(asctime)s : %(levelname)s : %(message)s'
    logFormatter = logging.Formatter(FORMAT)
    logging.basicConfig(filename=logger_name + '.log', level=logging.DEBUG, format=FORMAT)
    logger = logging.getLogger(logger_name)
    if (print_console):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logFormatter)
        logger.addHandler(console_handler)

    if (use_loggly):
        assert loggly_api_key != None
        import loggly.handlers
        lgy = loggly.handlers.HTTPSHandler(
            'https://logs-01.loggly.com/inputs/'+loggly_api_key+'/tag/python')
        lgy.setFormatter(logFormatter)
        logger.addHandler(lgy)

    return logger


class StreamToLogger(object):
   """
   Source: https://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/
   Fake file-like stream object that redirects writes to a logger instance.
   """
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''

   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())