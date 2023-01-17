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


def del_config() -> None:
    """
    Delete file of configuration of command line
    """
    configuration_path = path.join(gettempdir(), 'monog_configuration.json')
    try:
        remove(configuration_path)
    except FileNotFoundError:
        pass


def set_config(arguments: argparse.Namespace) -> None:
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
    print(type(arguments))
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
        print('You need specify --exec')
        return
    last_error = ''
    for index in range(args.retry + 1):
        if index:
            print(f'Retry execution number: {index}')
        try:
            command = shlex.split(args.execution)
            with subprocess.Popen(command, stdout=sys.stdout, stderr=subprocess.PIPE) as process:
                if (result := process.stderr):
                    last_error = ''.join([line.decode() for line in result.readlines()])
            if last_error:
                print(f'Error in application:\n{last_error}')
                continue
            break
        except Exception as err:
            print(f'Error in application:\n{err}\n\n{last_error}')


if __name__ == '__main__':
    main()
    del_config()
