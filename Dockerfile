FROM python:3.8.2-alpine

RUN adduser -D kevinds

WORKDIR /home/kevinds

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY kevinds.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP kevinds.py

RUN chown -R kevinds:kevinds ./
USER kevinds

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]