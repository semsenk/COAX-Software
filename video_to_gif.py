"""
You are working on a project for TikTok. 
The future project will be a web-site of all public GIF images. 
You need to write a function that converts TikTok video to GIF. 
The input parameter is url address of TikTok video, i.e. "TikTok example". 
The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".
"""

from moviepy.editor import VideoFileClip
import requests

def video_to_gif(url):
    chunk_size = 256
    r = requests.get(url,stream=True)

    with open("tiktok_video.mp4", "wb") as video_file:
        for chunk in r.iter_content(chunk_size=chunk_size):
            video_file.write(chunk)

    video = VideoFileClip("tiktok_video.mp4").subclip(0,)

    gif = video.write_gif("tiktok.gif")

    return gif

video_to_gif("https://v16-webapp.tiktok.com/fc0a361eaf505072047999e3d4a314b3/62e8a68f/video/tos/useast2a/tos-useast2a-ve-0068c002/c09a53d06fc344dfa562dfebcd7c2436/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1656&bt=828&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZVcCKwe2N-sWyl7Gb&mime_type=video_mp4&qs=0&rc=Nzk5Zzc3NzMzZDdlNTQ8ZEBpajl5bGdoZzg7czMzOzczM0BhXzViMDAzNjUxYzYvNWJeYSNkb2ltNmJjbWdfLS0wMTZzcw%3D%3D&l=2022080122221401022312823000719F42")