FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /djangobackend
COPY requirements.txt /djangobackend/
RUN pip install -r requirements.txt
COPY . /djangobackend/
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:djangobackend
