"""
Class to hanlde logs, prints and status bar
"""
# standard
from datetime import datetime
from enum import Enum
import json
from os import path
from tempfile import gettempdir
# third party
# local
from .decorators import format_log


class LogLevel(Enum):
    """
    Class to list log levels

    Attributes:
    -----------
        trace: int
            level trace
        debug: int
            level debug
        info: int
            level info
        warn: int
            level warning
        error: int
            level error
        fatal: int
            level 
    """
    trace = 1
    debug = 2
    info = 3
    warn = 4
    error = 5
    fatal = 6


class Logger:
    """
    Class to handle logs

    Attributes
    ----------
    * reset_attr: str
        reset ascii attributes of strings
    * color_<color_name>: str
        <color_name> color ascii code
        Options:
            - red
            - green
            - yellow
            - blue
            - purple
            - turquoise
            - white
    * attr_bold (str):
        change to emphasis ascii attribute
    * bg_red (str):
        ascii code for color red.
    * log_level (int):
        level of debugging, default 3.
    * application_name (str):
        Application name for debugging, default "Monog".
    * configuration (json):
        JSON with configuration of debugging.


    Methods
    -------
    * print(message, function_name, end, level):
        print message with format.
    * current_level():
        get current level of debugging.
    * send_to_server():
        prototype for send log to server.
    """

    # Attributes
    reset_attr: str = "\033[0m"
    attr_bold: str = "\033[1m"
    # font bolor
    color_back: str = "\033[38;5;0m"
    color_red: str = "\033[38;5;1m"
    color_green: str = "\033[38;5;2m"
    color_yellow: str = "\033[38;5;3m"
    color_blue: str = "\033[38;5;4m"
    color_purple: str = "\033[38;5;5m"
    color_turquoise: str = "\033[38;5;6m"
    color_white: str = "\033[38;5;255m"
    # background color
    bg_red: str = "\033[48;5;1m"

    _log_level = 3
    application_name = 'Monog'

    def __init__(self, application_name, log_level=0, config_file=None) -> None:
        self.application_name = application_name
        self.__log_level = log_level
        self.configuration = {}
        if config_file:
            if not path.isfile(config_file):
                self.print(f'File not exists: {config_file}', level=LogLevel.warn)
        else:
            config_file = path.join(gettempdir(), 'monog_configuration.json')
            if not path.isfile(config_file):
                self.print(f'Not found default file configuration', level=LogLevel.info)
            else:
                with open(config_file, 'r', encoding='utf-8') as conf:
                    self.configuration = json.loads(conf.read())
                self.__set_configuration()

    # Log level property
    @property
    def log_level(self) -> int:
        """
        Get current log level, comparison between class attribute
        and instance attribute.
        """
        if self.__log_level:
            return self.__log_level
        return Logger._log_level

    @log_level.setter
    def log_level(self, value: int) -> None:
        """
        Check and set log level value
        """
        try:
            LogLevel(value)
        except ValueError:
            self.print(f'Log level no valid: {value}', level=LogLevel.warn)
        self.__log_level = value

    @log_level.deleter
    def log_level(self) -> None:
        """
        Set value of __log_level 0
        """
        self.__log_level = 0


    def __set_configuration(self) -> None:
        """
        Set configuracion from config file
        """
        if not self.__log_level:
            self.__log_level = self.configuration.get('log_level', 0)

    def current_level(self) -> int:
        """
        Get current log level, comparison between class attribute
        and instance attribute.
        """
        if self.__log_level:
            return self.__log_level
        return Logger._log_level

    def print(self, message, function_name='', end='\n', level=LogLevel.info) -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        # if level.value < self.log_level:
        #     return
        print(message, end=end)
        # output = ''
        # output += f'{self.color_purple}[{self.application_name}] '
        # output += f'{self.color_turquoise}[{function_name}] ' if function_name else ''
        # output += f'{self.color_blue}[{datetime.now()}] '

        # if level == LogLevel.trace:
        #     output = f'{output}'\
        #              f'{self.color_turquoise}[ {level.name.upper()} ]: '
        # elif level == LogLevel.debug:
        #     output = f'{output}'\
        #              f'{self.color_purple}[ {level.name.upper()} ]: '
        # elif level == LogLevel.info:
        #     output = f'{output}'\
        #              f'{self.color_green}[ {level.name.upper()} ]: '
        # elif level == LogLevel.warn:
        #     output = f'{output}'\
        #              f'{self.color_yellow}[ {level.name.upper()} ]: '
        # elif level == LogLevel.error:
        #     output = f'{output}'\
        #              f'{self.color_red}[ {level.name.upper()} ]: '
        # elif level == LogLevel.fatal:
        #     output = f'{output}'\
        #              f'{self.bg_red}{self.color_white}[ {level.name.upper()} ]{self.reset_attr}: '
        # output = f'{output}{self.reset_attr}{message}'
        # print(output, end=end)
    
    @format_log
    def trace(self, message, function_name='', end='\n') -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if 1 < self.log_level:
            return
        print(message, end=end)

    @format_log
    def debug(self, message, function_name='', end='\n') -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if 2 < self.log_level:
            return
        print(message, end=end)
    
    @format_log
    def info(self, message, function_name='', end='\n') -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if 3 < self.current_level():
            return
        print(message, end=end)

    @format_log
    def warn(self, message, function_name='', end='\n') -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if 4 < self.log_level:
            return
        print(message, end=end)

    @format_log
    def error(self, message, function_name='', end='\n') -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if 5 < self.log_level:
            return
        print(message, end=end)

    @format_log
    def fatal(self, message, function_name='', end='\n') -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if 6 < self.log_level:
            return
        print(message, end=end)

    def send_to_server(self) -> bool:
        """
        prototype of function to send log to server
        """
        return False

