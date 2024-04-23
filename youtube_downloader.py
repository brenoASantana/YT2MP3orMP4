from pytube import YouTube
from moviepy.editor import *

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    return stream.default_filename

def convert_to_mp3(video_file, output_path):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(output_path)
    audio.close()
    video.close()

def convert_to_mp4(video_file, output_path):
    video = VideoFileClip(video_file)
    video.write_videofile(output_path)
    video.close()

# Exemplo de uso:
url = input("Insira a URL do vídeo do YouTube: ")
output_path = input("Insira o caminho de saída: ")

video_file = download_video(url, output_path)

option = input("Deseja converter para MP3 ou MP4? (MP3/MP4): ").lower()

if option == "mp3":
    output_file = output_path + "/output.mp3"
    convert_to_mp3(video_file, output_file)
    print("Conversão para MP3 concluída!")
elif option == "mp4":
    output_file = output_path + "/output.mp4"
    convert_to_mp4(video_file, output_file)
    print("Conversão para MP4 concluída!")
else:
    print("Opção inválida. Por favor, escolha MP3 ou MP4.")
