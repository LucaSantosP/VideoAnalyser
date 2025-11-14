import os
import locale
import textwrap
from dotenv import load_dotenv
from pytubefix import YouTube
import google.generativeai as genai
from pytubefix.exceptions import RegexMatchError, VideoUnavailable


load_dotenv()
API_KEY = os.getenv("API_KEY")
client = genai.configure(api_key=API_KEY)


def descobrir_idioma():
    """Usa o locale do python pra descobrir o idioma do sistema, só funciona desktop"""
    idioma = locale.getlocale()
    if idioma[0] is None:
        idioma = "en_US"
        return idioma
    return idioma[0]


idioma = descobrir_idioma()


def baixar_audio(url, pasta_saida="downloads"):
    """Baixa o audio de um video ou short do youtube e retorna o caminho do arquivo"""
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_path = audio_stream.download(output_path=pasta_saida)
        return file_path
    except RegexMatchError:
        raise ValueError("Invalid URL. Please check the link and try again.")
    except VideoUnavailable:
        raise ValueError("The video is unavailable or has been removed.")
    except Exception as erro:
        raise RuntimeError(f"An unexpected error occurred: {erro}")


def transcrever_audio(caminho_audio, modelo="gemini-2.5-flash"):
    """Transcreve um audio m4a usando modelo gemini"""
    with open(caminho_audio, "rb") as f:
        audio_bytes = f.read()
    resposta = genai.GenerativeModel(modelo).generate_content(
        [
            f"Transcreva exatamente o audio abaixo para texto em tal idioma: {idioma}",
            {"mime_type": "audio/m4a", "data": audio_bytes}
        ]
    )
    return resposta.text


def resumir_texto(texto, modelo="gemini-2.5-flash"):
    """Recebe um texto e resumi usando modelo gemini"""
    prompt = f"Resuma o seguinte texto de forma clara e objetiva mantendo o idioma original do texto: \n\n{texto}"
    resposta = genai.GenerativeModel(modelo).generate_content([prompt])
    return resposta.text


def exibir_texto_formatado(texto, largura=80):
    """Imprimi o texto com quebra de linhas automaticas e sem cortar palavras."""
    print(textwrap.fill(texto, width=largura))


def main():
    print('-'*80)
    print("Video Analyser".center(80))
    print('-'*80)
    print("Detecting Language...", end=" ")
    print(idioma)
    while True:
        try:
            url = input('Video URL: ').strip()
            print("Summarizing video...")
            caminho_audio = baixar_audio(url)
            texto_transcricao = transcrever_audio(caminho_audio)
            resumo = resumir_texto(texto_transcricao)
            print("\n" + f"Summary in {idioma}".center(80, "-"))
            print()
            exibir_texto_formatado(resumo)
            break
        except ValueError as e:
            print(f'\033[31m{e}\033[m')
        except RuntimeError as e:
            print(f'\033[31m{e}\033[m')
        except KeyboardInterrupt:
            print("\nExiting the program...")

if __name__ == "__main__":
    main()