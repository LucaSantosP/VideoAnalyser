import whisper
from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

print('-'*60)
txt = 'Video Analyser'
print(txt.center(60))
print('-'*60)

while True:
    try:
        a = input('Url do Video: ')
        try:
            yt = YouTube(a)
            audio_stream = yt.streams.filter(only_audio=True).first()
            print(f'Baixando: {yt.title}')
            file_path = audio_stream.download(output_path='Downloads')
            print('Download concluido com sucesso.')
            break
        except RegexMatchError:
            print('\033[31mURL inválida. Verifique o link e tente novamente.\033[m')
            continue
        except VideoUnavailable:
            print('\033[31mO vídeo não esta disponivel ou foi removido.\033[m')
            continue
        except Exception as erro:
            print(f'\033[31mOcorreu um erro inesperado: {erro}!!. Tente novamente.\033[m')
            continue
    except KeyboardInterrupt:
        print()
        print('Saindo do programa...')
        break


model = whisper.load_model('base')
print('Transcrevendo audio, aguarde um momento por favor.')
print()
result = model.transcribe(file_path)

print(result['text'])