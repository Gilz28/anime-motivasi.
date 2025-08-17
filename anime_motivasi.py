from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.all import fadein, fadeout

# ==========================
# 1. Background (gambar anime style)
# ==========================
# Untuk contoh, pakai gambar apapun dulu (nanti bisa diganti dengan gambar anime style).
# Simpan di folder yang sama dengan script ini, misalnya bg1.jpg, bg2.jpg, bg3.jpg.

scenes = [
    {"img": "bg1.jpg", "text": "Jangan pernah berhenti melangkah..."},
    {"img": "bg2.jpg", "text": "Meskipun dunia terasa berat...\nIngat, setiap luka akan membuatmu lebih kuat."},
    {"img": "bg3.jpg", "text": "Kamu adalah pemeran utama di hidupmu sendiri."}
]

# ==========================
# 2. Setting font
# ==========================
def make_textclip(txt, duration):
    return (TextClip(txt, fontsize=50, color='white', font="Arial-Bold")
            .set_duration(duration)
            .set_position(("center", "bottom"))
            .margin(bottom=80, opacity=0))

clips = []

for scene in scenes:
    bg = ImageClip(scene["img"]).set_duration(10).resize(height=720)  # setiap scene 10 detik
    text = make_textclip(scene["text"], 10)
    video = CompositeVideoClip([bg, text])
    clips.append(video)

final_video = concatenate_videoclips(clips, method="compose")

# ==========================
# 3. Tambah musik
# ==========================
# Download musik bebas copyright dari link yang aku kasih di bawah, simpan sebagai music.mp3
music = AudioFileClip("music.mp3").volumex(0.5)
final_video = final_video.set_audio(music)

# Fade in/out
final_video = fadein(final_video, 1).fadeout(1)

# ==========================
# 4. Export ke mp4
# ==========================
final_video.write_videofile("anime_motivasi.mp4", fps=24, codec="libx264")
