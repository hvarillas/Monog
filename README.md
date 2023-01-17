# Monog
Monitoring and log of applications in python

## Simple loggin
```py
from monog import Logger, LogLevel


if __name__ == '__main__':
    logger = Logger(application_name='Testing Application', log_level=1)
    logger.trace('Testing log level trace')
    logger.debug('Testing log level debug')
    logger.info('Testing log level info', function_name='main')
    logger.warn('Testing log level warn', function_name='main')
    logger.error('Testing log level error', function_name='main')
    logger.fatal('Testing log level fatal', function_name='main')
```

## Run command line
````bash
monog --exec "python app.py" --retry 3 --log-level 2
```
