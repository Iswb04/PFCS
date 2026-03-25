import os
import sys
import threading
import webbrowser
from django.core.management import execute_from_command_line


def open_browser():
    webbrowser.open("http://127.0.0.1:8000")


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financeiro.settings')

    if getattr(sys, 'frozen', False):
        os.chdir(os.path.dirname(sys.executable))

    threading.Timer(1.5, open_browser).start()

    execute_from_command_line([
        'manage.py',
        'runserver',
        '127.0.0.1:8000',
        '--noreload',
        '--nothreading'
    ])


if __name__ == '__main__':
    main()