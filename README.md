# 📱➡️💻 CapSendFlow

**Transferência de vídeo 4K de dispositivos móveis para editores, em tempo real, sem interromper a gravação.**

## 🎯 O problema

Produtores audiovisuais que gravam em celular enfrentam um gargalo real: enviar arquivos de vídeo em 4K para o editor exige interromper a gravação, esperar o upload manual (WhatsApp, e-mail, drive) e lidar com conexões móveis instáveis — tudo isso trava o fluxo de trabalho em produções que precisam de agilidade.

O **CapSendFlow** é um MVP para validar a viabilidade técnica de um sistema que resolve esse gargalo: um endpoint de upload que recebe arquivos grandes diretamente do navegador do celular, em rede local, com acompanhamento de progresso em tempo real.

> ⚠️ Este é um projeto pessoal de **validação técnica (MVP)**, não um produto em produção. O objetivo foi testar a hipótese antes de pensar em escalar.

## 🛠️ Stack

- **Backend:** Python + FastAPI + Uvicorn
- **Upload:** endpoint REST com `multipart/form-data`, suportando arquivos de até 1,5GB
- **Frontend:** HTML, CSS e JavaScript puro (sem frameworks)
- **Progresso em tempo real:** barra de upload via `XMLHttpRequest`
- **Rede:** servidor rodando em rede local (Wi-Fi), testado enviando arquivos direto de um iPhone pelo navegador
- **Segurança:** HTTPS com certificado autoassinado (biblioteca `cryptography`)
- **Banco de dados:** SQLite (planejado, ainda não implementado)
- **Versionamento:** Git

## ▶️ Como rodar localmente

```bash
# clone o repositório
git clone https://github.com/SEU_USUARIO/capsendflow.git
cd capsendflow

# crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# instale as dependências
pip install -r requirements.txt

# rode o servidor
uvicorn main:app --host 0.0.0.0 --port 8000 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```

Depois, acesse pelo navegador do celular usando o IP local da máquina que está rodando o servidor (ex: `https://192.168.0.10:8000`), estando na mesma rede Wi-Fi.

## 📸 Demonstração

*(inserir aqui um GIF ou screenshot da barra de progresso de upload em ação)*

## ⚠️ Limitações atuais

- Certificado HTTPS autoassinado — o navegador exibe aviso de segurança (esperado em ambiente de teste local)
- Persistência em SQLite ainda não implementada — os uploads não são registrados em banco de dados
- Testado apenas em rede local (Wi-Fi), sem exposição à internet
- Sem autenticação de usuários

## 🚀 Próximos passos

- Implementar persistência com SQLite
- Adicionar autenticação básica
- Testar em rede externa com domínio e certificado válido (Let's Encrypt)

---

Desenvolvido como projeto pessoal para explorar transferência de arquivos grandes, APIs REST com FastAPI e upload com progresso em tempo real.
