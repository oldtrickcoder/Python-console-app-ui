# importing vlc module
import vlc

# importing time module
import time


# creating vlc media player object
media_player = vlc.MediaPlayer()

video_path = 'samplevideo.mp4'
# media object
media = vlc.Media(video_path)

# setting media to the media player
media_player.set_media(media)
duration = media_player.get_length()

# start playing video
media_player.play()
    # printing the duration of the video
print("Duration : " + str(duration))
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(10)