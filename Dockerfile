FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install --upgrade pip "poetry==2.1.1"
RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY mysite .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]