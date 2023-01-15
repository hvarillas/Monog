"""
Class to hanlde logs, prints and status bar
"""
# standard
from datetime import datetime
from enum import Enum
# third party
# local


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
    reset_attr: str
        reset attributes of strings
    color_[color_name]: str
        [color_name] color code
        Options:
            * red
            * green
            * yellow
            * blue
            * purple
            * turquoise

    Methods
    -------
    print(message, function_name, end, level):
        print message with format
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

    log_level = 3

    def __init__(self, application_name, log_level=3) -> None:
        self.application_name = application_name
        Logger.log_level = log_level

    def print(self, message, function_name='', end='\n', level=LogLevel.info) -> None:
        """
        Write message in host

        Arguments:
            message (str): string to print
        """
        if level.value < Logger.log_level:
            return
        output = ''
        output += f'{self.color_purple}[{self.application_name}] '
        output += f'{self.color_turquoise}[{function_name}] ' if function_name else ''
        output += f'{self.color_blue}[{datetime.now()}] '

        if level == LogLevel.trace:
            output = f'{output}'\
                     f'{self.color_turquoise}[ {level.name.upper()} ]: '
        elif level == LogLevel.debug:
            output = f'{output}'\
                     f'{self.color_purple}[ {level.name.upper()} ]: '
        elif level == LogLevel.info:
            output = f'{output}'\
                     f'{self.color_green}[ {level.name.upper()} ]: '
        elif level == LogLevel.warn:
            output = f'{output}'\
                     f'{self.color_yellow}[ {level.name.upper()} ]: '
        elif level == LogLevel.error:
            output = f'{output}'\
                     f'{self.color_red}[ {level.name.upper()} ]: '
        elif level == LogLevel.fatal:
            output = f'{output}'\
                     f'{self.bg_red}{self.color_white}[ {level.name.upper()} ]{self.reset_attr}: '
        output = f'{output}{self.reset_attr}{message}'
        print(output, end=end)

    def send_to_server(self) -> bool:
        """
        prototype of function to send log to server
        """
        return False

