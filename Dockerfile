FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PORT 8000
WORKDIR /djangobackend
COPY requirements.txt /djangobackend/
RUN pip install -r requirements.txt
COPY . /djangobackend/
COPY entry_point.sh /djangobackend/
ENTRYPOINT ["/djangobackend/entry_point.sh"]
