FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /sources
COPY . /sources/
WORKDIR /sources

RUN cd /sources/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
