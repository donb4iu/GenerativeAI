# Notes

- Setup: import data with Pdf2image, OCR with PyTesseract.
- Preprocessing: use LLM with Ollama to enrich the data.
- Database: store and query data as vectors with ChromaDB.
- Backend: use LLM with Ollama to generate answers.
- Frontend: build an interface with Streamlit to interact with the AI.

## References

- [GenAI with Python: RAG with LLM (Complete Tutorial)](https://towardsdatascience.com/genai-with-python-rag-with-llm-complete-tutorial-c276dda6707b)

## Libraries

brew install tesseract



## Testing 

### #( 07/31/24@ 3:01PM )( donbuddenbaum@donbs-imac ):~
   pyenv global 3.12.3

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