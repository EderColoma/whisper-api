# Whisper-API

![Python Badge](https://img.shields.io/badge/-Pyhton-3776AB?style=flat-square&logo=Python&logoColor=white)
![OpenAi Badge](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=OpenAI&logoColor=white)
<br>
<br>
Provides a REST API to the OpenAI Whisper tool.
<br>
<br>
### Available endpoints:
#### `[GET] /whisper/transcribe`
Tanscribes the audio.

CUrl Example:
<br>
`curl --location --request POST 'http://localhost:5000/whisper/transcribe' \`
<br>
`--header 'Content-Type: multipart/form-data' \`
<br>
`--form 'file=@"/home/files/PR0016.mp3"'`

#### `[GET] /whisper/translate`
Tanscribes and translates the audio to english.

CUrl Example:
<br>
`curl --location --request POST 'http://localhost:5000/whisper/translate' \`
<br>
`--header 'Content-Type: multipart/form-data' \`
<br>
`--form 'file=@"/home/files/PR0016.mp3"'`

