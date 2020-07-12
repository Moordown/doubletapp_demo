FROM python:3.8-slim-buster
EXPOSE 80

ADD requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

ADD . /app
WORKDIR /app
CMD python /app/manage.py runserver
