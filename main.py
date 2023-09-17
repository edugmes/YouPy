import argparse
from pytube import YouTube, Playlist

def download_video(video_url: str, resolution: str | None = None, extension: str | None = None, path: str | None = None) -> None:
    yt = YouTube(video_url)
    if not resolution and not extension:
        video = yt.streams.get_highest_resolution()
    else:
        streams = yt.streams.filter(progressive=True, file_extension=extension, resolution=resolution).order_by('resolution').desc()
        if not streams:
            video = yt.streams.get_highest_resolution()
        else:
            video = streams[0]

    print(f"Downloading '{video.title}' with resolution={video.resolution} and extension={video.mime_type}")

    video.download(output_path=path)


def download_playlist(playlist_url: str, audio_only: bool = False) -> None:
    playlist = Playlist(playlist_url)

    if not audio_only:
        for url in playlist:
            download_video(url, path="playlist")
    else:
        for url in playlist:
            download_audio(url, path="playlist-audio")

def download_audio(video_url: str, path: str | None = None) -> None:
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True)[0]

    print(f"Downloading audio '{audio.title}' with extension={audio.mime_type}")

    audio.download(output_path=path or "audio")


class YouPyCmdParser:
    default_res = '720p'
    default_ext = 'mp4'

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description='YouPy Downloader')

        # Group 1: Main and mutually exclusive commands
        group_main = self.parser.add_mutually_exclusive_group()
        group_main.add_argument('-v', '--video', metavar="VIDEO_URL", type=str, help='Download video of VIDEO_URL')
        group_main.add_argument('-p', '--playlist', metavar="PLAYLIST_URL", type=str, help='Download videos of PLAYLIST_URL')
        group_main.add_argument('-i', '--info', metavar="VIDEO_URL", type=str, help='Show available extensions/resolutions of VIDEO_URL')
        group_main.add_argument('-a', '--audio', metavar="VIDEO_URL", type=str, help='Download audio only of VIDEO_URL')

        # Group 2: sub commands to be used with --video and --playlist
        group_video_playlist = self.parser.add_argument_group("--video and --playlist options")
        group_video_playlist.add_argument('-e', '--ext', type=str, nargs="?", help='Set download extension (e.g. mp4, mkv, avi)', default=self.default_ext, const=self.default_ext)
        group_video_playlist.add_argument('-r', '--res', type=str, nargs="?", help='Set download resolution (e.g. 1080p, 2k, 4k)', default=self.default_res, const=self.default_res)

        # Group 3: sub commands to be used with --info
        group_info = self.parser.add_argument_group("--info options")
        group_info.add_argument('-ro', '--res-only', type=bool, nargs="?", help='Show resolutions only', default=False, const=True)
        group_info.add_argument('-eo', '--ext-only', type=bool, nargs="?", help='Show extensions only', default=False, const=True)


    def parse_args(self) -> argparse.Namespace:
        args = self.parser.parse_args()

        # Check for valid command
        if not args.video and not args.playlist and not args.info and not args.audio:
            # If the user did not specify any of the other commands, invalidate all other combinations.
            if args.res_only or args.ext_only:
                self.parser.error("--res-only or --ext-only can only be use if --info is present")
            
            if (args.res and args.res != self.default_res)  or (args.ext and args.ext != self.default_ext):
                self.parser.error('--res or --ext can only be used if --video or --playlist is present')
            
            self.parser.print_help()
        
        else:
            # Check for invalid extension
            if args.ext not in ['mp4', 'mkv', 'avi']:
                self.parser.error('Invalid extension: {}'.format(args.ext))

        return args


if __name__ == '__main__':
    parser = YouPyCmdParser()
    args = parser.parse_args()

    # Execute the commands
    if args.video:
        download_video(video_url=args.video, resolution=args.res, extension=args.ext, path="video")
    elif args.playlist:
        download_playlist(args.playlist)
    elif args.info:
        pass
    elif args.audio:
        download_audio(args.audio)
