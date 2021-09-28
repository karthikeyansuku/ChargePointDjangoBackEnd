FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /djangobackend
COPY requirements.txt /djangobackend/
RUN pip install -r requirements.txt
COPY . /djangobackend/
ENV PORT 8000
CMD [ "python", "manage.py" ]
