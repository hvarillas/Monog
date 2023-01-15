from monog import Logger, LogLevel


if __name__ == '__main__':
    logger = Logger(application_name='Testing Application', log_level=1)
    logger.print('Testing log level trace', function_name='main', level=LogLevel.trace)
    logger.print('Testing log level debug', function_name='main', level=LogLevel.debug)
    logger.print('Testing log level info', function_name='main', level=LogLevel.info)
    logger.print('Testing log level warn', function_name='main', level=LogLevel.warn)
    logger.print('Testing log level error', function_name='main', level=LogLevel.error)
    logger.print('Testing log level fatal', function_name='main', level=LogLevel.fatal)