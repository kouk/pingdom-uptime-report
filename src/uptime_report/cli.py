from __future__ import print_function, unicode_literals

from clize import run
from uptime_report._version import get_versions
from uptime_report.backends import list_backends
from uptime_report.config import write_config


def uptime():
    """Do the uptime reporting stuff."""
    pass


def version():
    """Get the version of this program."""
    return get_versions().get('version', 'unknown')


def backends():
    """Print supported backends."""
    return "\n".join(list_backends())


def main(**kwargs):
    """Run the CLI application."""
    run([uptime, write_config], alt=[version, backends], **kwargs)


if __name__ == '__main__':
    main()
