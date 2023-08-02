from pytube import YouTube
import sys, getopt, os


def download_mp3(link, destination, output_file_title):
    print("start to downloaded...", link)
    yt = YouTube(str(link))
    # extract only audio and download to destination
    audio = yt.streams.filter(only_audio=True).first()    

    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    title = str(output_file_title) or (base)
    new_file_name = base + ".mp3"
    os.rename(out_file, new_file_name)
    print(new_file_name + " has been successfully downloaded.")


def batch_download():
    # download from source_links.csv
    pass    

def interactive_single_download():
    print("Enter link")
    link = str(input(">> "))
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
    print("Enter the file name (leave blank for default file name)")
    name = str(input(">> ")) or '.'

    download_mp3(link, destination)


def main(argv):
    batch_mode = 0
    opts, args = getopt.getopt(argv,"hi:b",["interactive=","batch="])
    # interactive mode is default
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <interactive mode> -b <batch mode> ')
            sys.exit()
        elif opt in ("-b", "--batch"):
            batch_mode = 1
    
    if (batch_mode):
        batch_download()
    else:
        interactive_single_download()


if __name__=='__main__':
    main(sys.argv[1:])
    