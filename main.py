# Paleidimo failas
from trending_finder import get_trending_game
from description_writer import generate_description
from video_generator import generate_video
from youtube_uploader import upload_to_youtube

# Vykdymas
trending_game = get_trending_game()
description, title = generate_description(trending_game)
video_path = generate_video(trending_game, title)
upload_to_youtube(video_path, title, description)