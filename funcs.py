import os, yt_dlp

def get_urls(f):
    with open(f,"r") as f:
        return f.readlines()
           

def get_mode(f):
    mode = get_urls(f,m=1).strip()
    match mode:
        case "a":
            return 0
        case "v":
            return 1

def get_app_dir():
    return os.path.dirname(os.path.realpath(__file__))

def ytdwl(yt_opts, URLS):
    """
        returns error code
    """
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        return ydl.download(URLS)

def get_folder_name(folder, mode):
    if folder[-1] != "/":
        main_folder = folder + "/"
    
    if not os.path.isdir(folder):
        os.mkdir(folder)
    
    return main_folder + mode

def generate_format_string(quality):
    return f"bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"



