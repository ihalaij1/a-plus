#!/usr/bin/env python
import os
import sys
import signal

def sighandler(signum, frame):
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)
    if "test" in sys.argv:
        os.environ.setdefault("APLUS_BASE_URL", "http://localhost")
        os.environ.setdefault("APLUS_LOCAL_SETTINGS", "aplus/local_settings.test.py")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aplus.settings")

    # Add application directory to PYTHONPATH for auto-instrumentation
    try:
        app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        user_paths = os.environ["PYTHONPATH"].split(os.pathsep)
        if not app_path in user_paths:
            os.environ["PYTHONPATH"] += ':' + app_path
    except KeyError:
        pass

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
