"""
Decorators
"""
# standard
from datetime import datetime
from typing import Callable
# thirdparty
# local


def format_log(func: Callable) -> Callable:
    """
    Decorator for formatting logs
    """
    def main(*args, **kwargs):
        params = ['self', 'message', 'function_name', 'end']
        for index, value in enumerate(args):
            kwargs[params[index]] = value
        message = kwargs.get('message')
        self = kwargs.get('self')
        function_name = kwargs.get('function_name')
        output = ''
        output += f'{self.color_purple}[{self.application_name}] '
        output += f'{self.color_turquoise}[{function_name}] ' if function_name else ''
        output += f'{self.color_blue}[{datetime.now()}] '
        if func.__name__ == 'trace':
            output = f'{output}'\
                     f'{self.color_turquoise}[ TRACE ]: '
        elif func.__name__ == 'debug':
            output = f'{output}'\
                     f'{self.color_purple}[ DEBUG ]: '
        elif func.__name__ == 'info':
            output = f'{output}'\
                     f'{self.color_green}[ INFO ]: '
        elif func.__name__ == 'warn':
            output = f'{output}'\
                     f'{self.color_yellow}[ WARN ]: '
        elif func.__name__ == 'error':
            output = f'{output}'\
                     f'{self.color_red}[ ERROR ]: '
        elif func.__name__ == 'fatal':
            output = f'{output}'\
                     f'{self.bg_red}{self.color_white}[ FATAL ]{self.reset_attr}: '
        output = f'{output}{self.reset_attr}{message}'
        kwargs['message'] = output
        result = func(**kwargs)
        return result
    return main
