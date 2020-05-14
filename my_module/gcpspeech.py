from google.cloud import texttospeech
import sys
import subprocess

# Instantiates a client
client = texttospeech.TextToSpeechClient()
filename = 'output.mp3'

def start(output_text):
    output_mp3(output_text)
    speech()

def output_mp3(output_text):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=output_text)
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='ja-JP',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    
    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
        speaking_rate=1.2)
    
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    
    # The response's audio_content is binary.
    with open(filename, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)

def speech():
    subprocess.run('mpg321 ' + filename, shell=True)

if __name__ == '__main__':
    try:
        args = sys.argv
        start(str(args[1]))
    finally:
        subprocess.run('rm -f ' + filename, shell=True)

