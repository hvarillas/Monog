"""
script execution handle
"""
# standard
import shlex
import subprocess
import sys
# thirdparty
import argparse
# local
from monog import Logger, LogLevel 


def main() -> None:
    """
    Main function
    """
    log = Logger(application_name='Monog', log_level=2)
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

    args = parse.parse_args()
    if not args.execution:
        log.print('You need specify --exec', function_name='main', level=LogLevel.fatal)
        return
    last_error = ''
    for index in range(args.retry + 1):
        if index:
            log.print(f'Retry execution number: {index}', level=LogLevel.info)
        try:
            command = shlex.split(args.execution)
            process = subprocess.Popen(command, stdout=sys.stdout, stderr=subprocess.PIPE)
            last_error = ''.join([line.decode() for line in process.stderr.readlines()])
            if last_error:
                log.print(f'Error in application:\n{last_error}', level=LogLevel.fatal)
                continue
            break
        except Exception as err:
            log.print(f'Error in application:\n{err}\n\n{last_error}', level=LogLevel.fatal)


if __name__ == '__main__':
    main()
