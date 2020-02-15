import sys
from pathlib import Path

import toga
from toga import App


class Paths:
    @property
    def app(self):
        return Path(sys.modules[App.app.module_name].__file__).parent

    @property
    def author(self):
        if App.app.author is None:
            return "Unknown Developer"
        return App.app.author

    @property
    def data(self):
        return Path.home() / 'AppData' / 'Local' / self.author / App.app.formal_name

    @property
    def cache(self):
        return Path.home() / 'Library' / 'Local' / self.author / App.app.formal_name / 'Cache'

    @property
    def logs(self):
        return Path.home() / 'Library' / 'Local' / self.author / App.app.formal_name / 'Logs'

    @property
    def sys_resources(self):
        """Return a path to a Toga system resources
        """
        return Path(toga.__file__).parent

    def arbitrary(self, path):
        """Return an arbitrary path representing object

        Args:
            path (str): A string with the path to wrap. If a relative path is
                        given, it will be interpreted to be relative to the
                        application module directory.
        """
        return self.app / Path(path)


paths = Paths()
