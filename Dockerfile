FROM tiangolo/uwsgi-nginx:python3.6

RUN pip install bottle

COPY ./webapp /app
