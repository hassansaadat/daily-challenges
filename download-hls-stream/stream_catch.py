import re
import subprocess
from typing import List, Dict
from urllib.parse import urlparse, urlunparse, urljoin
from typing import Union

import requests


def get_master_playlist(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_base_url(url: str) -> str:
    parsed_url = urlparse(url)
    path = parsed_url.path
    base_path = path.rsplit('/', 1)[0] + '/' if '/' in path else '/'

    base_url = urlunparse((
        parsed_url.scheme,
        parsed_url.netloc,
        base_path,
        '',  # params
        '',  # query
        ''  # fragment
    ))

    return base_url


def parse_qualities(base_url: str, master_playlist: str) -> List[Dict]:
    qualities = []
    pattern = re.compile(r'#EXT-X-STREAM-INF.*BANDWIDTH=(\d+).*RESOLUTION=(\d+x\d+).*\n(.*)\n')

    matches = pattern.findall(master_playlist)
    for match in matches:
        bandwidth = int(match[0])
        resolution = match[1]
        url = match[2].strip()

        qualities.append({
            'bandwidth': bandwidth,
            'resolution': resolution,
            'url': urljoin(base_url, url)
        })

    return qualities


def prompt_quality_selection(qualities: List[Dict]) -> Union[Dict, None]:
    print("Available qualities:")
    for idx, quality in enumerate(qualities):
        print(f"{idx + 1}: Resolution = {quality['resolution']}, Bandwidth = {quality['bandwidth']}")

    choice = int(input("Enter the index of the quality you want to download: ")) - 1
    if choice < 0 or choice >= len(qualities):
        print("Invalid choice. Please enter a valid index.")
        return None

    return qualities[choice]


def download_with_ffmpeg(url: str, output_file: str) -> None:
    command = [
        'ffmpeg',
        '-i', url,
        '-c', 'copy',  # Copy codec to avoid re-encoding
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Download completed successfully. Saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    hls_url = input("Enter the Master playlist .m3u8 file URL: ")

    base_url = get_base_url(hls_url)
    master_playlist = get_master_playlist(hls_url)
    qualities = parse_qualities(base_url, master_playlist)

    if not qualities:
        print("No qualities found in the master playlist.")
    else:
        chosen_quality = prompt_quality_selection(qualities)
        if chosen_quality:
            output_file = input("Enter the output file path: ")
            download_with_ffmpeg(chosen_quality['url'], output_file)
        else:
            print("Download canceled.")
