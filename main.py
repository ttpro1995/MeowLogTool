import sys

from meowlogtool import log_util

api = "07510d18-73c8-4552-8227-264c111ab3ab"
if __name__ == "__main__":
    logger = log_util.create_logger("temp_file", print_console=True)
    logger.info("LOG_FILE")
    logger2 = log_util.create_logger("loggly", print_console=True, use_loggly=True, loggly_api_key=api)
    logger2.info("Log from python")

    s1 = log_util.StreamToLogger(logger2)
    sys.stdout = s1
    print 'I am Pusheen the cat'
    a = 1234
    print ('I eat 3 shortcakes already. It is too short')
    print ('cost = ', a)