# 📱➡️💻 CapSendFlow

**MVP para transferência rápida de vídeos grandes do celular para o computador pela rede local, com backend em FastAPI e acompanhamento de upload pelo navegador.**

## 🎯 O problema

Em produções audiovisuais feitas com celular, transferir arquivos grandes para um editor pode virar um gargalo. O processo costuma envolver serviços externos, upload manual, compressão de mídia ou interrupções no fluxo de trabalho.

O **CapSendFlow** foi criado como uma prova de conceito para validar uma alternativa simples: enviar o arquivo diretamente do navegador do celular para um computador conectado à mesma rede Wi-Fi.

O projeto expõe uma página de envio, recebe o arquivo por uma API REST e salva o conteúdo localmente no computador responsável pelo servidor.

> ⚠️ Este projeto é um MVP educacional e de validação técnica. Não foi desenvolvido como solução pronta para produção ou exposição direta à internet.

## ✨ O que o projeto demonstra

- Criação de API REST com **FastAPI**
- Recebimento de arquivos com `multipart/form-data`
- Transferência de arquivos entre dispositivos em rede local
- Integração entre frontend e backend
- Upload pelo navegador sem necessidade de aplicativo dedicado
- Geração de certificado HTTPS autoassinado com Python
- Manipulação e persistência de arquivos no sistema operacional
- Tratamento básico de erros e validação de upload

## 🏗️ Arquitetura atual

```text
┌──────────────────────┐
│ Celular / navegador  │
│      index.html      │
└──────────┬───────────┘
           │ HTTPS / Wi-Fi local
           ▼
┌──────────────────────┐
│      FastAPI         │
│       main.py        │
├──────────────────────┤
│ GET  /               │
│ GET  /enviar         │
│ POST /upload         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     uploads/         │
│ arquivos recebidos   │
└──────────────────────┘
```

## 🛠️ Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **HTML, CSS e JavaScript**
- **python-multipart** para processamento do upload
- **cryptography** para geração do certificado local
- **Git / GitHub** para versionamento

## 📂 Estrutura do projeto

```text
CAPSENDFLOW/
├── main.py                 # API FastAPI e lógica de recebimento dos arquivos
├── index.html              # Interface web para envio
├── gerar_certificado.py    # Gera certificado e chave HTTPS de desenvolvimento
├── requirements.txt        # Dependências Python
├── .gitignore              # Protege uploads, certificados e arquivos locais
└── README.md
```

A pasta `uploads/` é criada automaticamente quando o backend inicia e não deve ser versionada.

## ▶️ Como executar localmente

### 1. Clone o projeto

```bash
git clone https://github.com/aavpires93/CAPSENDFLOW.git
cd CAPSENDFLOW
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Gere o certificado de desenvolvimento

```bash
python gerar_certificado.py
```

O script atual contém um IP local de exemplo no certificado. Caso seu computador use outro endereço IP na rede, atualize o valor em `gerar_certificado.py` antes de gerar novamente `cert.pem` e `key.pem`.

### 5. Inicie a API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```

### 6. Abra pelo celular

Com o celular conectado à mesma rede Wi-Fi do computador, acesse:

```text
https://IP_DO_COMPUTADOR:8000/enviar
```

Por utilizar um certificado autoassinado, o navegador pode exibir um aviso de segurança no ambiente de desenvolvimento.

## 🔌 Endpoints

| Método | Endpoint | Função |
|---|---|---|
| `GET` | `/` | Verifica se a API está ativa |
| `GET` | `/enviar` | Retorna a interface web de upload |
| `POST` | `/upload` | Recebe e salva o arquivo enviado |

Exemplo de resposta após um upload concluído:

```json
{
  "nome_arquivo": "video.mp4",
  "status": "recebido",
  "tempo_segundos": 8.42
}
```

## 🔐 Segurança e privacidade

O repositório foi configurado para não versionar:

- arquivos enviados pelos usuários;
- pasta `uploads/`;
- chaves privadas e certificados `.pem`;
- arquivos `.env`;
- bancos de dados locais;
- ambientes virtuais e caches do Python.

Mesmo assim, o MVP **não possui autenticação** e não deve ser exposto diretamente à internet no estado atual.

Também seria necessário endurecer a validação do nome, tamanho e tipo dos arquivos antes de considerar qualquer uso real.

## ⚠️ Limitações atuais

- Funciona como prova de conceito em rede local
- Sem autenticação ou autorização
- Sem banco de dados
- Sem histórico de transferências
- Arquivos são gravados diretamente no filesystem
- Certificado HTTPS autoassinado
- O script de certificado utiliza um IP local configurado manualmente
- Ainda não há testes automatizados

## 🚀 Roadmap

Possíveis evoluções do projeto:

1. Sanitizar nomes de arquivos e impedir sobrescrita acidental
2. Definir limite configurável de tamanho de upload
3. Validar MIME type/extensão dos arquivos
4. Criar persistência de transferências em SQLite
5. Adicionar autenticação por token ou QR Code
6. Exibir histórico de uploads no frontend
7. Gerar automaticamente o certificado para o IP local da máquina
8. Adicionar testes com `pytest`
9. Containerizar a aplicação com Docker
10. Evoluir para transferência em chunks e retomada de uploads interrompidos

## 💼 Competências demonstradas

Este projeto é especialmente útil no portfólio por demonstrar conhecimentos em:

`Python` · `FastAPI` · `REST APIs` · `HTTP` · `Upload de arquivos` · `Frontend` · `Redes` · `HTTPS` · `Git` · `Tratamento de erros`

---

Desenvolvido como projeto pessoal para estudar APIs, transferência de arquivos grandes e comunicação entre dispositivos em rede local.
