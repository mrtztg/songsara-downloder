import os
from urllib import request, parse
import pathlib
import re
from sys import stdout

regex_for_normalize_filename = re.compile('[/*?:"<>|]')


def _normalize(file_name: str):
    return re.sub(regex_for_normalize_filename, "", file_name)


class MusicFile:
    def __init__(self, file_name: str, url: str = ""):
        self.file_name = file_name
        self.url = url


class DownloadPack:
    def __init__(self, folder_name: str = "", song_list=None):
        if song_list is None:
            song_list = []
        self.folder_name = folder_name
        self.song_list = song_list

    def append_music(self, music: MusicFile):
        self.song_list.append(music)

    def download_all(self, root_folder: str = "download"):
        if len(self.song_list) == 0:
            return
        folder_path = os.path.join(root_folder, _normalize(self.folder_name))
        if not pathlib.Path(folder_path).is_dir():
            os.makedirs(folder_path)
            print(f'folder "{self.folder_name}" created')
        else:
            print(f'Folder "{self.folder_name}" creation ignored because created before')
        for song in self.song_list:
            _, file_extension = os.path.splitext(parse.urlparse(song.url).path)
            song_file_path = os.path.join(folder_path, _normalize(song.file_name) + file_extension)
            if pathlib.Path(song_file_path).is_file():
                print(f'file "{song.file_name}" ignored because downloaded before')
            else:
                stdout.write(f'file "{song.file_name}" is downloading...')
                stdout.flush()
                request.urlretrieve(song.url, song_file_path)
                stdout.write(f'\x1b[2K\rfile "{song.file_name}" downloaded\n')
                stdout.flush()
