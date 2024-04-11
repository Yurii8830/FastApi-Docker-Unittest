FROM python:3.10-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY . /app

RUN /opt/venv/bin/pip install --upgrade pip setuptools wheel pip-tools
RUN /opt/venv/bin/pip-compile requirements/requirements.in > requirements/requirements.txt
RUN /opt/venv/bin/pip install -r requirements/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
