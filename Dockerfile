#python padrao
FROM python:3 as python-base

#ambiente
ENV PYTHONUNBUFFERED=1 \
    #previne o python de criar arquivos .pyc
    PYTHONDONTWRITEBYTECODE=1 \
    \
    #pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    #poetry
    #https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=2.1.1 \
    #diretorio do poetry p/ instalacoes
    POETRY_HOME="/opt/poetry" \
    #faz o poetry criar o ambiente virtual na pasta raiz do projeto, com o nome de '.venv'
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    #nao pedir perguntas interativas de instalacao
    POETRY_NO_INTERACTION=1 \
    \
    #caminhos: caminho onde nosso 'requisitos.txt' e nosso ambiente virtual sera transmitido
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
    
#incrementa 'poetry' e 'venv' pro caminho
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

#configuracoes p/ linux: atualiza repositorios
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        #dependencias do poetry
        curl \
        #dependencias do python
        build-essential

#instala poetry
RUN curl -sSL https://install.python-poetry.org | python

#instala bibl. + compilador
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

#copia os requisitos do projeto aqui p/ garantir que sera carregado
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

#instalacao rapida de runtime dependencias ja estao instaladas
RUN poetry install --no-root

#----------------
WORKDIR /app
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]