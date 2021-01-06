#!/usr/bin/python3
import requests
import pathlib
from download_pack import DownloadPack, MusicFile
from bs4 import BeautifulSoup

url_list_file = "input_url_list.txt"
download_list_file = "download_list.txt"
downloaded_folder = "download"


def get_download_pack_from_download_file():
    with open(download_list_file) as file:
        lines = [x.strip() for x in file.readlines()]
    download_pack_list = []
    is_folder_name = True
    music_detail_pos = 0
    current_music: MusicFile
    for line in lines:
        if not line.strip():
            is_folder_name = True
            music_detail_pos = 0
        elif is_folder_name:
            pack = DownloadPack(line)
            download_pack_list.append(pack)
            is_folder_name = False
        elif music_detail_pos == 0:
            music_detail_pos = 1
            current_music = MusicFile(line)
        elif music_detail_pos == 1:
            music_detail_pos = 0
            current_music.url = line
            download_pack_list[len(download_pack_list) - 1].append_music(current_music)

    return download_pack_list


def scrap_and_fill_download_file():
    with open(url_list_file) as file:
        dest_pages = [x.strip() for x in file.readlines() if x.strip()]
    download_file_lines = []
    for dest_page in dest_pages:
        response = requests.get(dest_page)
        soup = BeautifulSoup(response.text, "html.parser")
        folder_name = soup.select_one(".AL-Si").string
        download_file_lines.append(folder_name)
        track_rows = soup.select("#aramplayer .audioplayer-audios li")
        if track_rows is not None:
            for track_row in track_rows:
                song_name = track_row["data-title"]
                download_file_lines.append(song_name)
                song_url = track_row.select_one("div.audioplayer-source")["data-src"]
                download_file_lines.append(song_url)
        download_file_lines.append("")
    with open(download_list_file, mode="w") as file:
        file.writelines([f'{x}\n' for x in download_file_lines])


def get_download_list():
    if pathlib.Path(download_list_file).is_file():
        while True:
            answer = input(
                "Download List file exists. Select option:\n"
                "1- Scrap Again\n2- Download This links\n").lower()
            if str(answer) == "1":
                scrap_and_fill_download_file()
                break
            elif str(answer) == "2":
                break
    else:
        scrap_and_fill_download_file()
    return get_download_pack_from_download_file()


download_list = get_download_list()
for download_item in download_list:
    download_item.download_all()