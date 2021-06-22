FROM python:buster as base

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

FROM base as production
COPY . .
RUN git clone https://github.com/pyenv/pyenv.git /home/todo/app/.pyenv/ \
	&& pip install "poetry==$POETRY_VERSION" \
	&& poetry install --no-root --no-dev

EXPOSE 5000
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:flask_app"]

FROM base as development
COPY . .
RUN pip install "poetry==$POETRY_VERSION" \
	&& poetry install --no-root \
	&& chmod +x ./dev_entry_point.sh
	# found chmod behaviour inconsistent. Had to check execute perms on host 1st

EXPOSE 5001
ENTRYPOINT ["./dev_entry_point.sh"]
