from datetime import datetime
from hashlib import md5
from os import environ, path, makedirs, listdir
from shutil import copy2
from subprocess import Popen, CREATE_NO_WINDOW
from sys import argv, executable

from PIL import Image
from plyer import notification
from rich import print

ARGS = argv + ['']
EXECUTION_TYPE = path.splitext(ARGS[0])[-1]
APPDATA = environ.get('appdata')
USERPROFILE = environ.get('userprofile')
SOURCE_FILE = path.join(APPDATA,'Microsoft','Windows','Themes','TranscodedWallpaper')
DESTINATION_DIRECTORY = path.join(USERPROFILE,'Pictures','Windows Spotlight')


DEBUG = lambda log: print(f'[[bold green]DEBUG[/bold green]] {log}')
INFO = lambda log: print(f'[[bold blue]INFO[/bold blue]] {log}')
ERROR = lambda log: print(f'[[bold red]ERROR[/bold red]] {log}')


class Spotlight:
    def __init__(self):
        makedirs(DESTINATION_DIRECTORY, exist_ok=True)

        self.date = datetime.today().strftime('%Y-%m-%d')
        self.index = 1
        self.prefix = 'Windows-Spotlight'
        self.last_wallpaper = self.fetch_last_wallpaper()

    def fetch_last_wallpaper(self):
        try:
            last_wallpaper = sorted(
                filter(
                    lambda x: x.startswith(self.prefix),
                    listdir(DESTINATION_DIRECTORY)
                ),
                reverse=True
            )[0]
            return path.join(DESTINATION_DIRECTORY, last_wallpaper)
        except IndexError:
            return None

    def fetch_current_wallpaper(self):
        try:
            if self.last_wallpaper:
                self.check_duplicate()
            output = self.generate_output_filename()
            copy2(SOURCE_FILE, output)
            message = 'Wallpaper copied'
            INFO(f'{message}: "[blue]{path.basename(output)}[/blue]"')
            show_notification(message)
        except FileExistsError:
            message = 'Wallpaper already copied'
            INFO(f'{message}')
            if ARGS[1] != '-n': show_notification(message)

    def check_duplicate(self):
        hash1 = generate_hash(SOURCE_FILE)
        hash2 = generate_hash(self.last_wallpaper)

        if hash1 == hash2:
            INFO(f'Hashes match (hash1: [italic]{hash1}[/italic], hash2: [italic]{hash2})[/italic]')
            raise FileExistsError
        else:
            INFO(f'Hashes doesn\'t match (hash1: [italic]{hash1}[/italic], hash2: [italic]{hash2})[/italic]')
        return None

    def generate_output_filename(self):
        while True:
            file = path.join(DESTINATION_DIRECTORY, f'{self.prefix}-{self.date}_{str(self.index).rjust(2,"0")}.jpg')
            if path.exists(file): self.index += 1
            else: return file

def generate_hash(file: str):
    try:
        INFO(f'Generating Hash for "[blue]{path.basename(file)}[/blue]"')
        with Image.open(file) as img:
            return md5(img.tobytes()).hexdigest()
    except FileNotFoundError:
        ERROR(f'FileNotFound: [blue]"{file}"[/blue]')
        return None

def notify(message):
    notification.notify(
        title="Fetch Spotlight",
        message=message,
        app_icon="icons/spotlight.ico"
    )

def show_notification(message):
    args = []
    if EXECUTION_TYPE == '.exe':
        args = [ARGS[0], '--show-notification', message]
    elif EXECUTION_TYPE == '.py':
        args = ['cmd', '/C', executable, ARGS[0], '--show-notification', message]
    Popen(args, shell=True, creationflags=CREATE_NO_WINDOW)


def main():
    if ARGS[1] == '--show-notification':
        notify(ARGS[2])
    else:
        Spotlight().fetch_current_wallpaper()

if __name__ == '__main__':
    main()