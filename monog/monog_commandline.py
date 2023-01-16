"""
script execution handle
"""
# standard
import json
from os import path, remove
import shlex
import subprocess
import sys
from tempfile import gettempdir
# thirdparty
import argparse
# local
from monog import Logger, LogLevel 


def del_config() -> None:
    configuration_path = path.join(gettempdir(), 'monog_configuration.json')
    try:
        remove(configuration_path)
    except FileNotFoundError:
        pass

def set_config(arguments: argparse.ArgumentParser) -> None:
    """
    Create file configuration for global configuration
    
    Argumetns:
    ----------
    * arguments (argparse.ArgumentParser):
        variable that content all arguments

    Returns:
    --------
    * None
    """
    del_config()
    configuration = {}
    if (level := arguments.level):
        configuration['log_level'] = level
    configuration_path = path.join(gettempdir(), 'monog_configuration.json')
    with open(configuration_path, 'w', encoding='utf-8') as conf:
        conf.write(json.dumps(configuration, indent=2))



def main() -> None:
    """
    Main function
    """
    Logger.info(Logger, "start")
    # log = Logger(application_name='Monog', log_level=2)
    parse = argparse.ArgumentParser(description="script execution handle")
    # Add argument for command execution
    parse.add_argument(
        '--exec',
        '-e',
        dest='execution',
        type=str,
        default=''
    )
    # Add argument for retry
    parse.add_argument(
        '--retry',
        '-r',
        dest='retry',
        type=int,
        default=0
    )
    # Add argument for log level
    parse.add_argument(
        '--level',
        '-l',
        dest='level',
        type=int,
        default=3
    )
    args = parse.parse_args()
    set_config(args)
    if not args.execution:
        Logger.print(Logger, 'You need specify --exec', function_name='main', level=LogLevel.fatal)
        return
    last_error = ''
    for index in range(args.retry + 1):
        if index:
            Logger.print(f'Retry execution number: {index}', level=LogLevel.info)
        try:
            command = shlex.split(args.execution)
            process = subprocess.Popen(command, stdout=sys.stdout, stderr=subprocess.PIPE)
            last_error = ''.join([line.decode() for line in process.stderr.readlines()])
            if last_error:
                Logger.print(f'Error in application:\n{last_error}', level=LogLevel.fatal)
                continue
            break
        except Exception as err:
            Logger.print(f'Error in application:\n{err}\n\n{last_error}', level=LogLevel.fatal)


if __name__ == '__main__':
    main()
    del_config()
