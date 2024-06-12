from moviepy.editor import ImageClip, AudioFileClip

def create_video(image_path, audio_path, output_path):
    # Cargar la imagen
    image_clip = ImageClip(image_path)

    # Cargar el audio
    audio_clip = AudioFileClip(audio_path)

    # Establecer la duración del video como la duración del audio
    duration = audio_clip.duration
    video_clip = image_clip.set_duration(duration)

    # Unir el audio y el video
    video_with_audio = video_clip.set_audio(audio_clip)

    # Guardar el video resultante
    video_with_audio.write_videofile(output_path, codec='libx264', fps=24)

# Rutas de los archivos de entrada y salida
image_path = "cristo.jpg"
audio_path = "cristo.mp3"
output_path = "video_cristo.mp4"

# Crear el video
create_video(image_path, audio_path, output_path)