import argparse
from typing import Any, Dict, List


class Parameters:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            prog='mnamer', description='a media file renaming utility',
            epilog='visit https://github.com/jkwill87/mnamer/wiki '
                   'for more information'
        )

        self._parser.add_argument(
            '-b', '--batch', action='store_true', default=None,
            help='batch mode; disables interactive prompts & persists on error'
        )

        self._parser.add_argument(
            '-d', '--dots', action='store_true', default=None,
            help='format using dots in place of whitespace when renaming'
        )

        self._parser.add_argument(
            '-l', '--lower', action='store_true', default=None,
            help='format using lowercase when renaming'
        )
        self._parser.add_argument(
            '-r', '--recurse', action='store_true', default=None,
            help='recursive file crawling and following symlinks'
        )

        self._parser.add_argument(
            '--extmask', nargs='+', metavar='E', default=None,
            help='define the extension mask used by the the file parser'
        )

        # if find_spec('PyQt5'):
        #     self._parser.add_argument(
        #         '--ui', action='store_true', default=None,
        #         help='set user interface mode'
        #     )

        self._parser.add_argument(
            '--movie_destination', nargs='?', metavar='D', default=None,
            help='set movie relocation destination'
        )

        self._parser.add_argument(
            '--movie_template', nargs='?', metavar='T', default=None,
            help='set movie renaming template'
        )

        self._parser.add_argument(
            '--tv_destination', nargs='?', metavar='D', default=None,
            help='set television relocation destination'
        )

        self._parser.add_argument(
            '--tv_template', nargs='?', metavar='T', default=None,
            help='set television renaming template'
        )

        self._parser.add_argument(
            'targets', nargs='+', default=[],
            help='media files and/or directories'
        )

        args = vars(self._parser.parse_args())
        self._targets = args.pop('targets')
        self._arguments = {k: v for k, v in args.items() if v}

    @property
    def targets(self) -> List[str]:
        return self._targets

    @property
    def arguments(self) -> Dict[str, Any]:
        return self._arguments