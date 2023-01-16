from monog import Logger, LogLevel


logger = Logger(application_name='Testing Application')
def all(log) -> None:
    log.trace('Testing log level trace')
    log.debug('Testing log level debug', function_name='main')
    log.info('Testing log level info', function_name='main')
    log.warn('Testing log level warn', function_name='main')
    log.error('Testing log level error', function_name='main')
    log.fatal('Testing log level fatal', function_name='main')

if __name__ == '__main__':
    all(logger)
    print("="*200)
    logger.log_level = 1
    all(logger)
    print("="*200)
    del logger.log_level
    all(logger)

