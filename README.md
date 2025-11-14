# VideoAnalyser

VideoAnalyser is a Python tool that downloads YouTube videos or shorts, transcribes the audio, and generates a concise summary. It supports multiple languages based on the system locale and uses the Google Generative AI API for transcription and summarization.

## Features

- Download audio from YouTube videos or shorts
- Transcribe audio automatically in the system language
- Summarize the transcription clearly and concisely
- Supports multiple languages
- Works directly in the terminal

## Prerequisites

Before running the project, you need:

- Python 3.9 or higher
- `pip` package manager (used to install Python libraries)
- A Google Generative AI API key stored in a `.env` file as `API_KEY`
- Required Python packages (install via `pip install -r requirements.txt`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/LucaSantosP/VideoAnalyser.git
```

2. Enter the project directory:

```bash
cd VideoAnalyser
```

3. (Optional but recommended) Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

- **Windows:**  
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**  
```bash
source .venv/bin/activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file in the project root and add your API key:

```text
API_KEY=your_google_genai_api_key_here
```

7. Run the program:

```bash
python main.py
```

## Usage

1. The program detects your system language automatically.
2. Enter the YouTube video URL when prompted.
3. The program will download the audio, transcribe it, and generate a summary.
4. The summary is printed in the same language as the transcription.

## Example

```
Video URL: https://www.youtube.com/watch?v=example
Detecting Language... en_US
Summarizing video...
-------------------------------- Summary in en_US --------------------------------
This is a concise summary of the video content, keeping the original language.
```

## Project Structure

```
VideoAnalyser/
├─ main.py          # Main script
├─ video_analyser/  # Modules for video/audio processing
├─ requirements.txt # Dependencies
├─ .gitignore       # Ignored files/folders
├─ LICENSE          # MIT License
├─ README.md        # This file
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
