import speech_recognition as sr
from pydub import AudioSegment


def mp3_to_wav(mp3_file):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_file)
    wav_file = mp3_file.replace(".mp3", ".wav")
    audio.export(wav_file, format="wav")
    return wav_file


def audio_to_text(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Convert MP3 to WAV if needed
    if audio_file.endswith(".mp3"):
        audio_file = mp3_to_wav(audio_file)

    # Read and transcribe the audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

        try:
            # Transcribe audio to text using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("Transcription: ", text)

            # Save the transcription to a file
            with open("transcription.txt", "w") as file:
                file.write(text)
            print("Transcription saved to 'transcription.txt'.")

        except sr.UnknownValueError:
            print("Audio was unclear.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")


# Example usage
audio_to_text("audio.mp3")
