# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de dependências
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código-fonte para o container
COPY . /app/

# Exponha a porta 8000
EXPOSE 8000

# Defina o comando padrão para o container
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "evento_manager.wsgi:application"]
