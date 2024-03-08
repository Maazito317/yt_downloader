from pytube import YouTube
import argparse 
import sys

def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    bar_length = 50
    done = int(bar_length * current / stream.filesize)

    sys.stdout.write(
        "\r[{}{}] {} MB / {} MB".format('=' * done, ' ' * (bar_length - done), "{:.2f}".format(bytes_to_megabytes(current)),
                                        "{:.2f}".format(bytes_to_megabytes(stream.filesize))))
    sys.stdout.flush()


def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size

def main():
    parser = argparse.ArgumentParser()
    # take input from command line: link, download dir (Create if doesn't exist) 
    parser.add_argument('link', type=str, help='Link to the youtube video')
    parser.add_argument('dir', type=str, help='Directory to be downloaded to')
    args = parser.parse_args()

    # create YouTube object
    yt: YouTube = YouTube(args.link)
    yt.register_on_progress_callback(progress_func)

    # print info of video
    print('Video Title: ', yt.title)
    print('Length of Video: ', yt.length)
    print('Number of Views: ',yt.views)

    # get stream
    high_res_stream = yt.streams.get_highest_resolution()

    # download video
    high_res_stream.download(args.dir)

if __name__ == '__main__':
    SystemExit(main())
