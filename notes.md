# Notes

- Setup: import data with Pdf2image, OCR with PyTesseract.
- Preprocessing: use LLM with Ollama to enrich the data.
- Database: store and query data as vectors with ChromaDB.
- Backend: use LLM with Ollama to generate answers.
- Frontend: build an interface with Streamlit to interact with the AI.

## References

- [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

- [GenAI with Python: RAG with LLM (Complete Tutorial)](https://towardsdatascience.com/genai-with-python-rag-with-llm-complete-tutorial-c276dda6707b)

- [CoreML Execution Provider](https://chatgpt.com/c/cb803075-bfbf-49f8-b42f-692a0023118b)

## Libraries

brew install tesseract
brew install poppler



## Testing 

### #( 07/31/24@ 3:01PM )( donbuddenbaum@donbs-imac ):~
   pyenv global 3.12.3
### #( 08/04/24@10:57PM )( donbuddenbaum@donbs-imac ):~/Documents/GenerativeAI@main✗✗✗
   
   python --version

      Python 3.11.5


### #( 07/31/24@ 3:02PM )( donbuddenbaum@donbs-imac ):~
   jupyter notebook

```
[I 2024-07-31 15:05:33.165 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2024-07-31 15:05:33.172 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2024-07-31 15:05:33.182 ServerApp] jupyterlab | extension was successfully linked.
[I 2024-07-31 15:05:33.189 ServerApp] notebook | extension was successfully linked.
[I 2024-07-31 15:05:33.738 ServerApp] notebook_shim | extension was successfully linked.
[I 2024-07-31 15:05:33.812 ServerApp] notebook_shim | extension was successfully loaded.
[I 2024-07-31 15:05:33.816 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2024-07-31 15:05:33.818 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2024-07-31 15:05:33.823 LabApp] JupyterLab extension loaded from /Users/donbuddenbaum/.pyenv/versions/3.12.3/lib/python3.12/site-packages/jupyterlab
[I 2024-07-31 15:05:33.824 LabApp] JupyterLab application directory is /Users/donbuddenbaum/.pyenv/versions/3.12.3/share/jupyter/lab
[I 2024-07-31 15:05:33.825 LabApp] Extension Manager is 'pypi'.
[I 2024-07-31 15:05:33.855 ServerApp] jupyterlab | extension was successfully loaded.
[I 2024-07-31 15:05:33.862 ServerApp] notebook | extension was successfully loaded.
[I 2024-07-31 15:05:33.863 ServerApp] Serving notebooks from local directory: /Users/donbuddenbaum
[I 2024-07-31 15:05:33.863 ServerApp] Jupyter Server 2.14.2 is running at:
[I 2024-07-31 15:05:33.863 ServerApp] http://localhost:8888/tree?token=e0a963970800f975bb5506d61f3b98577827aaeb7fa23114
[I 2024-07-31 15:05:33.863 ServerApp]     http://127.0.0.1:8888/tree?token=e0a963970800f975bb5506d61f3b98577827aaeb7fa23114
[I 2024-07-31 15:05:33.863 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2024-07-31 15:05:33.873 ServerApp]

    To access the server, open this file in a browser:
        file:///Users/donbuddenbaum/Library/Jupyter/runtime/jpserver-47738-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=e0a963970800f975bb5506d61f3b98577827aaeb7fa23114
        http://127.0.0.1:8888/tree?token=e0a963970800f975bb5506d61f3b98577827aaeb7fa23114
[I 2024-07-31 15:05:34.372 ServerApp] Skipped non-installed server(s): bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
```

## Model Installation

### #( 07/31/24@ 3:28PM )( donbuddenbaum@donbs-imac ):~
   ollama run phi3

    zsh: command not found: ollama
### #( 07/31/24@ 4:32PM )( donbuddenbaum@donbs-imac ):~
   ollama run phi3

```
pulling manifest
pulling 633fc5be925f... 100% ▕████████████████████████████████████████████▏ 2.2 GB
pulling fa8235e5b48f... 100% ▕████████████████████████████████████████████▏ 1.1 KB
pulling 542b217f179c... 100% ▕████████████████████████████████████████████▏  148 B
pulling 8dde1baf1db0... 100% ▕████████████████████████████████████████████▏   78 B
pulling 23291dc44752... 100% ▕████████████████████████████████████████████▏  483 B
verifying sha256 digest
writing manifest
removing any unused layers
success
>>>
Use Ctrl + d or /bye to exit.
>>>
```
### #( 07/31/24@ 4:40PM )( donbuddenbaum@donbs-imac ):~
   ollama run llava

```
pulling manifest
pulling 170370233dd5... 100% ▕████████████████████████████████████████████▏ 4.1 GB
pulling 72d6f08a42f6... 100% ▕████████████████████████████████████████████▏ 624 MB
pulling 43070e2d4e53... 100% ▕████████████████████████████████████████████▏  11 KB
pulling c43332387573... 100% ▕████████████████████████████████████████████▏   67 B
pulling ed11eda7790d... 100% ▕████████████████████████████████████████████▏   30 B
pulling 7c658f9561e5... 100% ▕████████████████████████████████████████████▏  564 B
verifying sha256 digest
writing manifest
removing any unused layers
success
>>>
```

### #( 07/31/24@ 4:48PM )( donbuddenbaum@donbs-imac ):~
   pip install ollama

```
Collecting ollama
  Downloading ollama-0.3.1-py3-none-any.whl.metadata (3.8 kB)
Requirement already satisfied: httpx<0.28.0,>=0.27.0 in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from ollama) (0.27.0)
Requirement already satisfied: anyio in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from httpx<0.28.0,>=0.27.0->ollama) (4.4.0)
Requirement already satisfied: certifi in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from httpx<0.28.0,>=0.27.0->ollama) (2024.2.2)
Requirement already satisfied: httpcore==1.* in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from httpx<0.28.0,>=0.27.0->ollama) (1.0.5)
Requirement already satisfied: idna in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from httpx<0.28.0,>=0.27.0->ollama) (3.7)
Requirement already satisfied: sniffio in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from httpx<0.28.0,>=0.27.0->ollama) (1.3.1)
Requirement already satisfied: h11<0.15,>=0.13 in ./.pyenv/versions/3.12.3/lib/python3.12/site-packages (from httpcore==1.*->httpx<0.28.0,>=0.27.0->ollama) (0.14.0)
Downloading ollama-0.3.1-py3-none-any.whl (10 kB)
Installing collected packages: ollama
Successfully installed ollama-0.3.1
```

### #( 08/04/24@11:10PM )( donbuddenbaum@donbs-imac ):~
   pip install chromadb==0.5.0

      Collecting chromadb==0.5.0


### #( 08/04/24@11:12PM )( donbuddenbaum@donbs-imac ):~
   pip install pytesseract==0.3.10

```
Collecting pytesseract==0.3.10

  Obtaining dependency information for pytesseract==0.3.10 from https://files.pythonhosted.org/packages/c5/54/ec007336f38d2d4ce61f3544af3e6855dacbf04a1ac8294f10cabe81146f/pytesseract-0.3.10-py3-none-any.whl.metadata
  Downloading pytesseract-0.3.10-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: packaging>=21.3 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from pytesseract==0.3.10) (24.1)
Requirement already satisfied: Pillow>=8.0.0 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from pytesseract==0.3.10) (10.4.0)
Downloading pytesseract-0.3.10-py3-none-any.whl (14 kB)
Installing collected packages: pytesseract
Successfully installed pytesseract-0.3.10
```

### #( 08/04/24@11:22PM )( donbuddenbaum@donbs-imac ):~
   pip install tqdm

      Requirement already satisfied: tqdm in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (4.66.5)

### #( 08/05/24@ 2:51AM )( donbuddenbaum@donbs-imac ):~
   pip install matplotlib

```
Collecting matplotlib
  Obtaining dependency information for matplotlib from https://files.pythonhosted.org/packages/09/49/569b50eb5e5a75b61f7a0bacb6029e9ea9c8a1190df55a39a31789244e09/matplotlib-3.9.0-cp311-cp311-macosx_10_12_x86_64.whl.metadata
  Downloading matplotlib-3.9.0-cp311-cp311-macosx_10_12_x86_64.whl.metadata (11 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Obtaining dependency information for contourpy>=1.0.1 from https://files.pythonhosted.org/packages/33/0e/51ff72fac17e2500baf30b6b2a24be423a8d27e1625e5de99f585b852d74/contourpy-1.2.1-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Downloading contourpy-1.2.1-cp311-cp311-macosx_10_9_x86_64.whl.metadata (5.8 kB)
Collecting cycler>=0.10 (from matplotlib)
  Obtaining dependency information for cycler>=0.10 from https://files.pythonhosted.org/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl.metadata
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Obtaining dependency information for fonttools>=4.22.0 from https://files.pythonhosted.org/packages/8b/6a/206391c869ab22d1374e2575cad7cab36b93b9e3d37f48f4696eed2c6e9e/fonttools-4.53.1-cp311-cp311-macosx_10_9_universal2.whl.metadata
  Downloading fonttools-4.53.1-cp311-cp311-macosx_10_9_universal2.whl.metadata (162 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 162.6/162.6 kB 2.0 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Obtaining dependency information for kiwisolver>=1.3.1 from https://files.pythonhosted.org/packages/a6/94/695922e71288855fc7cace3bdb52edda9d7e50edba77abb0c9d7abb51e96/kiwisolver-1.4.5-cp311-cp311-macosx_10_9_x86_64.whl.metadata
  Downloading kiwisolver-1.4.5-cp311-cp311-macosx_10_9_x86_64.whl.metadata (6.4 kB)
Requirement already satisfied: numpy>=1.23 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from matplotlib) (1.23.5)
Requirement already satisfied: packaging>=20.0 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from matplotlib) (24.1)
Requirement already satisfied: pillow>=8 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from matplotlib) (10.4.0)
Collecting pyparsing>=2.3.1 (from matplotlib)
  Obtaining dependency information for pyparsing>=2.3.1 from https://files.pythonhosted.org/packages/9d/ea/6d76df31432a0e6fdf81681a895f009a4bb47b3c39036db3e1b528191d52/pyparsing-3.1.2-py3-none-any.whl.metadata
  Downloading pyparsing-3.1.2-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: python-dateutil>=2.7 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in ./.pyenv/versions/3.11.5/lib/python3.11/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
Downloading matplotlib-3.9.0-cp311-cp311-macosx_10_12_x86_64.whl (7.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 10.4 MB/s eta 0:00:00
Downloading contourpy-1.2.1-cp311-cp311-macosx_10_9_x86_64.whl (262 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 262.1/262.1 kB 10.0 MB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.53.1-cp311-cp311-macosx_10_9_universal2.whl (2.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 10.7 MB/s eta 0:00:00
Downloading kiwisolver-1.4.5-cp311-cp311-macosx_10_9_x86_64.whl (68 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 68.2/68.2 kB 6.5 MB/s eta 0:00:00
Downloading pyparsing-3.1.2-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.2/103.2 kB 10.6 MB/s eta 0:00:00
Installing collected packages: pyparsing, kiwisolver, fonttools, cycler, contourpy, matplotlib
Successfully installed contourpy-1.2.1 cycler-0.12.1 fonttools-4.53.1 kiwisolver-1.4.5 matplotlib-3.9.0 pyparsing-3.1.2
```