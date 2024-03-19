FROM python:3.11

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]