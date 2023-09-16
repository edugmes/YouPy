# YouPy
Download Youtube videos with Python

# Prerequisites

- Python3
- Pip

# Installation

```
./install.sh
```
It creates a virtual environment on the current directory, activates it,
and installs dependencies with pip on the environment.

# Running

```
./youpy.sh [command] [sub-command]
```
usage: 
```
./youpy.sh [-h] [-v VIDEO_URL | -p PLAYLIST_URL | -i VIDEO_URL | -a VIDEO_URL] [-e [EXT]] [-r [RES]] [-ro [RES_ONLY]] [-eo [EXT_ONLY]]

options:
  -h, --help            show help message and exit
  -v VIDEO_URL, --video VIDEO_URL
                        Download video of VIDEO_URL
  -p PLAYLIST_URL, --playlist PLAYLIST_URL
                        Download videos of PLAYLIST_URL
  -i VIDEO_URL, --info VIDEO_URL
                        Show available extensions/resolutions of VIDEO_URL
  -a VIDEO_URL, --audio VIDEO_URL
                        Download audio only of VIDEO_URL

--video and --playlist options:
  -e [EXT], --ext [EXT]
                        Set download extension (e.g. mp4, mkv, avi)
  -r [RES], --res [RES]
                        Set download resolution (e.g. 1080p, 2k, 4k)

--info options:
  -ro [RES_ONLY], --res-only [RES_ONLY]
                        Show resolutions only
  -eo [EXT_ONLY], --ext-only [EXT_ONLY]
                        Show extensions only

```