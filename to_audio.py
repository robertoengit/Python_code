from gtts import gTTS

# Texto a convertir en voz
texto = "Aqui el texto"

# Configurar la velocidad de lectura
velocidad = 0.5  # Ajusta la velocidad según sea necesario (0.5 para más lento)

# Generar el archivo de audio
tts = gTTS(text=texto, lang='es', slow=True)
tts.save("nombre_de_audio.mp3")