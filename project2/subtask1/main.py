import os
import moviepy.editor as mp
import speech_recognition as sr
import PyPDF2
import sys
import ffmpeg

def extract_text_from_video(video_file):
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    transcript = extract_text_from_audio(audio)
    return transcript

def extract_text_from_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data) + '\n'
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + '\n'
    return text


def main():
    print("Enter choice for file type : \n1. Video\n2. Audio\n3. Pdf\n?- ", sep='')
    n = int(input())
    if n<1 or n>3:
        sys.exit("Choice should be in range 1-3")

    print("Enter file path : ", end='')
    file = input()
    text = ''
    match n:
        case 1:
            text = extract_text_from_video(file)
        case 2:
            filepath , filename = os.path.split(file)
            basename, ext = os.path.splitext(filename)
            wav_file = f"{basename}.wav"
            stream = ffmpeg.input(file)
            stream = ffmpeg.output(stream, wav_file, acodec='pcm_s16le', ac=1, ar='16k')
            ffmpeg.run(stream)
            file = wav_file
            text = extract_text_from_audio(file)
        case 3:
            text = extract_text_from_pdf(file)
        case _:
            sys.exit("ERROR")

    filepath , filename = os.path.split(file)
    basename, ext = os.path.splitext(filename)

    output = f"{basename}.txt"

    with open(output, 'w') as file:
        file.write(text)
        
if __name__ == "__main__":
    main()
