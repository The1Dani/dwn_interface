from .funcs import *
from . import modes

class Options:
    
    AUDIO = modes.AUDIO
    VIDEO = modes.VIDEO
    MODES = modes.MODES    

    def __init__(self, folder:str=None) -> None:
        
        if folder != None:
            self.folder = folder
        else:
            self.folder = get_app_dir()

        for mode in self.MODES:
            self.MODES[mode]["paths"]["home"] = get_folder_name(self.folder, mode)
            
        self.download = Download(self)

    def __str__(self) -> str:
        return "\n".join(["[AUDIO]",str(self.AUDIO),"[VIDEO]",str(self.VIDEO),"[DIR]",self.folder])

class Download:

    def __init__(self, options:Options) -> None:
        self.options = options

    def __str__(self) -> str:
        return self.options.__str__()

    def mode(self, mode, URLS):
        return ytdwl(self.options.MODES[mode], URLS)      
        
    def quality_mode(self, URLS, quality=modes.MAX_QUALITY):
        quality_mode_dict = self.options.MODES["video"].copy()
        quality_mode_dict["format"] = generate_format_string(quality)
        return ytdwl(quality_mode_dict, URLS)

def main():
    o = Options()
    print(o)
    o.download.mode("audio","https://www.youtube.com/watch?v=B9synWjqBn8")

if __name__ == "__main__":
    main()