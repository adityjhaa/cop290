import moviepy.editor as mp
import speech_recognition as sr
import PyPDF2
import sys
import os

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

# file = ''
file = 'test1.wav'
# file = 'instr.pdf'

# text = extract_text_from_video(file)
text = extract_text_from_audio(file)
# text = extract_text_from_pdf(file)

filepath , filename = os.path.split(file)
basename, ext = os.path.splitext(filename)

output = f"{basename}.txt"

with open(output, 'w') as file:
    file.write(text)
    
