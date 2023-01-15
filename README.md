# Monog
Monitoring and log of applications in python

## Simple loggin
````py
from monog import Logger, LogLevel


if __name__ == '__main__':
    logger = Logger(application_name='Testing Application')
    logger.print('Testing log level info', function_name='main', level=LogLevel.error)
```
