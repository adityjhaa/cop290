## Subtask 1

### Implementations
- #### Programming Language - Python 🐍

- #### Libraries
    - **PyPDF2** – Using this library to extract text from *pdf* files.
    - **whisper** – Used to extract text from audio files. It supports all major file formats like *mp3*, *wav*, *mpga*, etc. It uses <b>*ffmpeg*</b> in its background for conversion among these formats.
    - **moviepy** – Used to convert *mp4*, *mkv* and other video formats to a temporary *wav* file so that we can use whisper for text extraction.

- #### Performance improving steps
    - I used OpenAI's whisper over my previous approach with Google's speech-recognizer which couldn’t handle heavier loads.
    - Used moviepy to convert videos to audio rather than using whisper to extract text directly from the video. This results in faster text extraction.

### Issues faced

- At first, I faced issues with *mp3* file format when I was using speech-recognizer as it only supports *wav* audio format.
- Working with whisper at first was a major pain as it tries to make a temporary file for each case, but once I installed <b>*ffmpeg*</b>, it did it all internally.
- Using whisper to extract text from videos would take so long. Using moviepy solved the problem.

### Tests
Some of my tests and their results (as *.txt* files) can be found in the following link.
<a href="https://csciitd-my.sharepoint.com/:f:/g/personal/cs1221102_iitd_ac_in/EgoJP2ng4tpGuyw4tj-PgcMBG4uNYlGjNDzUgM5Kmbo1fA?e=RBBGPm">Tests</a>

