# Download HLS Stream using ffmpeg
Simple python script to download HLS (HTTP Live Streaming) streams using ffmpeg.

It fetches the master M3U8 playlist from a given URL, lets you choose the desired quality, and downloads the stream to a specified output file.

## Prerequisites
- Python 3.x
- requests library (install via pip install requests)
- ffmpeg (ensure ffmpeg is installed and accessible in your system's PATH)

## Usage
Clone the repository or download the script stream_catch.py . 

Install the required System libraries:
```shell
$ sudo apt install ffmpeg
```
Install the required Python libraries:
```shell
$ pip install requests
```
Run the script:
```shell
$ python stream_catch.py
```

- Enter the URL pointing to the HLS stream when prompted.
- Choose a quality option from the available list.
- Enter the output file path where the downloaded stream will be saved.
