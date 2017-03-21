import sys
from meowlogtool import log_util

api = "YOUR-API"

if __name__ == "__main__":

    # log to console and file
    logger1 = log_util.create_logger("temp_file", print_console=True)
    logger1.info("LOG_FILE") # log using logger1

    # log to console, file and loggly.com
    logger2 = log_util.create_logger("loggly", print_console=True, use_loggly=True, loggly_api_key=api, loggly_tag='test')
    logger2.info("Log from python")

    # attach log to stdout (print function)
    s1 = log_util.StreamToLogger(logger2)
    sys.stdout = s1

    # anything print to console will be log
    print 'I am Pusheen the cat'
    a = 1234
    print ('I eat 3 shortcakes already. It is too short')
    print ('cost = ', a)