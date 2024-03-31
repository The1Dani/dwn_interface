MAX_QUALITY = 1080

AUDIO = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }],
        "paths": {
            "home": None 
        },
        "outtmpl": "%(title)s.%(ext)s",
        "windowsfilenames": True
    }

VIDEO = {
    'format': f"bestvideo[height<={MAX_QUALITY}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "paths": {
        "home": None
    },
    "outtmpl": "%(title)s.%(ext)s",
    "windowsfilenames": True
}

MODES = {
    "audio": AUDIO,
    "video": VIDEO
}