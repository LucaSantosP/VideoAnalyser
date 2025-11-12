import whisper
import textwrap
from pytubefix import YouTube
from transformers import pipeline
from pytubefix.exceptions import RegexMatchError, VideoUnavailable


def baixar_audio(url, pasta_saida="downloads"):
    """Baixa o audio de um video ou short do youtube e retorna o caminho do arquivo"""
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(f"Baixando: {yt.title}")
        file_path = audio_stream.download(output_path=pasta_saida)
        print("Download concluído com sucesso.")
        return file_path
    except RegexMatchError:
        raise ValueError("URL inválida. Verifique o link e tente novamente.")
    except VideoUnavailable:
        raise ValueError("O vídeo não esta disponivel ou foi removido.")
    except Exception as erro:
        raise RuntimeError(f"Ocorreu um erro inesperado: {erro}")


def transcrever_audio(caminho_audio, modelo="base"):
    """Transcreve um arquivo de audio usando modelo whisper."""
    print("Carregando modelo Whisper...")
    model= whisper.load_model(modelo)
    print("Transcrevendo áudio, aguarde um momento...")
    result = model.transcribe(caminho_audio)
    return result["text"]


def resumir_texto(texto, modelo="facebook/bart-large-cnn"):
    """Cria um resumo no texto usando modelo Bart."""
    print("Gerando Resumo...")
    summarizer = pipeline("summarization", model=modelo)
    summary = summarizer(texto, do_sample=False)[0]["summary_text"]
    return summary


def exibir_texto_formatado(texto, largura=80):
    """Imprimi o texto com quebra de linhas automaticas e sem cortar palavras."""
    print(textwrap.fill(texto, width=largura))


def main():
    print('-'*80)
    print("Video Analyser".center(80))
    print('-'*80)

    while True:
        try:
            url = input('URL do vídeo: ').strip()
            caminho_audio = baixar_audio(url)
            texto_transcricao = transcrever_audio(caminho_audio)
            resumo = resumir_texto(texto_transcricao)
            print("\n" + "RESUMO".center(80, "-"))
            print()
            exibir_texto_formatado(resumo)
            break
        except ValueError as e:
            print(f'\033[31m{e}\033[m')
        except RuntimeError as e:
            print(f'\033[31m{e}\033[m')
        except KeyboardInterrupt:
            print("\nSaindo do programa...")

if __name__ == "__main__":
    main()