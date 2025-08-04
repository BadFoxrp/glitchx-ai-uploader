from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"})

from moviepy.editor import TextClip
import os

def generate_video(game, title):
    txt = f"{title}\n#{game}"
    
    clip = TextClip(txt, fontsize=72, color='white', size=(720, 1280))
    clip = clip.set_duration(10)
    clip = clip.set_position('center')
    clip = clip.set_fps(24)

    if not os.path.exists("output"):
        os.makedirs("output")

    video_path = "output/video.mp4"
    clip.write_videofile(video_path, fps=24)
    return video_path
