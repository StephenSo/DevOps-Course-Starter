FROM python:buster

RUN useradd -ms /bin/bash todo

RUN apt-get update && apt-get install -y \
	build-essential \
	libssl-dev \
	zlib1g-dev \
	libbz2-dev \
	libreadline-dev \
	libsqlite3-dev \
	wget \
	curl \
	llvm \
	libncurses5-dev \
	libncursesw5-dev \
	xz-utils \
	tk-dev \
	libffi-dev \
	liblzma-dev \
	python-openssl \
	git libxml2-dev \
	libxmlsec1-dev \
	&& rm -rf /var/lib/apt/lists/*


WORKDIR /home/todo/app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6 \
  PYENV_ROOT=/home/todo/app/.pyenv \
  PATH=$PYENV_ROOT/bin:/home/todo/.poetry/bin:/home/todo/.local/bin:$PATH

#COPY --chown=todo:todo ./app /home/todo/app
COPY ./ /home/todo/app

RUN git clone https://github.com/pyenv/pyenv.git /home/todo/app/.pyenv/
RUN pip install "poetry==$POETRY_VERSION" gunicorn flask flask_wtf
RUN poetry install --no-root --no-dev
#USER todo

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind", "172.17.0.3:5000", "wsgi:flask_app"]
