FROM python:3.11-slim

WORKDIR /app

# Evita a criação de arquivos .pyc e força o stdout sem buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema necessárias para compilar pacotes (se houver)
RUN apt-get update && apt-get install -y --no-install-recommends gcc libssl-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cria diretórios necessários
RUN mkdir -p reports db

ENTRYPOINT ["python", "main.py"]
CMD ["--help"]
