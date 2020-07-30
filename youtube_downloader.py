import sys
from youtube_dl import YoutubeDL
from termcolor import colored


def downloader(link: list, choice: int, quality: int) -> str:

    try:
        download_quality = None
        if quality == 1 and choice == 1:
            download_quality = "bestvideo+bestaudio"
        elif quality == 1 and choice == 2:
            download_quality = "bestaudio"
        elif quality == 2 and choice == 1:
            download_quality = "best"
        elif quality == 3 and choice == 1:
            download_quality = "worstvideo+worstaudio"
        elif quality == 3 and choice == 2:
            download_quality = "worstaudio"

        params = {
            "outtmpl": "D:\\Videos\\%(title)s.%(ext)s",
            "format": download_quality,
            # "listformats": True,
        }
        ytube = YoutubeDL(params=params)
        with ytube as ydl:
            ydl.download(link)

        return colored("Download success", "green")
    except:
        return colored(f"Download Error\n{sys.exc_info()[0].__doc__}", "red")


if __name__ == "__main__":
    while True:
        print(
            colored("Welcome to Youtube Downloader \N{grinning face}\n", "yellow"))
        choice = int(
            input(colored("Please enter 1 to download video, 2 to download audio only: ", "yellow")))
        choice_name = "video" if choice == 1 else "audio"
        download_link = input(
            colored("Please enter the link of the video/playlist you want to download: ", "yellow"))
        print(
            colored(f"Please enter the quality you want to download the {choice_name} in\n", "yellow"))
        quality = int(input(
            colored("Please enter 1 for best quality (greater than 720p), 2 for okay quality (between 720p and 480p), 3 for worst quality (less than 480p): ", "yellow")))
        link_list = [download_link]
        r = downloader(link_list, choice, quality)
        print(r)
        program_exit = int(input(
            colored("If you want to quit the program press 1, if you want to continue downloading press 2: ", "yellow")))
        if program_exit == 1:
            print(colored("Thank you for using Youtube downloader", "yellow"))
            break
        else:
            continue
