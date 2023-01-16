"""
Decorators
"""
# standard
from datetime import datetime
import os
import sys
from typing import Callable
# thirdparty
# local
import monog as mm


def format_log(func: Callable) -> Callable:
    def main(self, *args, **kwargs):
        print(self)
        params = ['message', 'function_name', 'end']
        for index, value in enumerate(args):
            kwargs[params[index]] = value
        message = kwargs.get('message')
        function_name = kwargs.get('function_name')
        output = ''
        output += f'{mm.Logger.color_purple}[{mm.Logger.application_name}] '
        output += f'{mm.Logger.color_turquoise}[{function_name}] ' if function_name else ''
        output += f'{mm.Logger.color_blue}[{datetime.now()}] '
        if func.__name__ == 'trace':
            output = f'{output}'\
                     f'{mm.Logger.color_turquoise}[ TRACE ]: '
        elif func.__name__ == 'debug':
            output = f'{output}'\
                     f'{mm.Logger.color_purple}[ DEBUG ]: '
        elif func.__name__ == 'info':
            output = f'{output}'\
                     f'{mm.Logger.color_green}[ INFO ]: '
        elif func.__name__ == 'warn':
            output = f'{output}'\
                     f'{mm.Logger.color_yellow}[ WARN ]: '
        elif func.__name__ == 'error':
            output = f'{output}'\
                     f'{mm.Logger.color_red}[ ERROR ]: '
        elif func.__name__ == 'fatal':
            output = f'{output}'\
                     f'{mm.Logger.bg_red}{mm.Logger.color_white}[ FATAL ]{mm.Logger.reset_attr}: '
        output = f'{output}{mm.Logger.reset_attr}{message}'
        kwargs['message'] = output
        result = func(self, **kwargs)
        return result
    return main
