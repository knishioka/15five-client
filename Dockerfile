FROM python:3.8.6-slim-buster
WORKDIR /usr/src

COPY requirements.txt /usr/src/requirements.txt

RUN pip install pip==20.2.3 && \
    pip install -r /usr/src/requirements.txt

RUN useradd app
RUN mkdir -p /home/app && chown -R app:app /home/app
USER app
