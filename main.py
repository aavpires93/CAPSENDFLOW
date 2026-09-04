from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
import time

app = FastAPI()

PASTA_UPLOADS = "uploads"
os.makedirs(PASTA_UPLOADS, exist_ok=True)


@app.get("/")
def home():
    return {"mensagem": "CapSendFlow está no ar"}


@app.get("/enviar")
def pagina_envio():
    return FileResponse("index.html")


@app.post("/upload")
async def receber_video(file: UploadFile = File(...)):
    if not file.filename:
        return JSONResponse(
            status_code=400,
            content={"erro": "Nenhum arquivo foi enviado."}
        )

    inicio = time.time()
    caminho_destino = os.path.join(PASTA_UPLOADS, file.filename)

    try:
        with open(caminho_destino, "wb") as destino:
            shutil.copyfileobj(file.file, destino)
    except Exception as erro:
        return JSONResponse(
            status_code=500,
            content={"erro": f"Não foi possível salvar o arquivo: {erro}"}
        )

    tamanho = os.path.getsize(caminho_destino)
    if tamanho == 0:
        os.remove(caminho_destino)
        return JSONResponse(
            status_code=400,
            content={"erro": "O arquivo chegou vazio."}
        )

    fim = time.time()
    duracao = round(fim - inicio, 2)
    print(f"Upload de '{file.filename}' concluído em {duracao} segundos")

    return {
        "nome_arquivo": file.filename,
        "status": "recebido",
        "tempo_segundos": duracao
    }