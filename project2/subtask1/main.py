import os
import moviepy.editor as mp
import PyPDF2
import sys
import whisper

# extect text from video
def text_from_video(video_file, model='base'):
    whisper_model = whisper.load_model(model)
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    temp = "temp.wav"
    audio.write_audiofile(temp, codec='pcm_s16le')
    result = whisper_model.transcribe(temp)
    transcript = result["text"] + '\n'
    os.remove(temp)
    return transcript

# extect text from audio
def text_from_audio(audio_file, model="base"):
    whisper_model = whisper.load_model(model)    
    result = whisper_model.transcribe(audio_file)
    transcript = result["text"] + '\n'
    return transcript

# extect text from pdf
def text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + '\n'
    return text

# main function
def main():
    print("Enter choice for file type : \n1. Video\n2. Audio\n3. Pdf\n?- ", end='')
    n = int(input())
    if n<1 or n>3:
        sys.exit("Choice should be in range 1-3")

    print("Enter file path : ", end='')
    file = str(input())
    text = ''
    match n:
        case 1:
            text = text_from_video(file)
        case 2:
            text = text_from_audio(file)
        case 3:
            text = text_from_pdf(file)
        case _:
            sys.exit("ERROR")

    filepath , filename = os.path.split(file)
    basename, ext = os.path.splitext(filename)

    output = f"{filepath}/{basename}.txt"

    with open(output, 'w') as file:
        file.write(text)
        
if __name__ == "__main__":
    main()
