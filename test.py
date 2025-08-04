from moviepy.editor import TextClip

clip = TextClip("Hello!", fontsize=70, color='white', size=(640, 480))
clip = clip.set_duration(5)
clip.write_videofile("test_output.mp4", fps=24)
