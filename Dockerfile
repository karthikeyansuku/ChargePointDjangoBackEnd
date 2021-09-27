FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /djangobackend
COPY requirements.txt /djangobackend/
RUN pip install -r requirements.txt
COPY . /djangobackend/
EXPOSE 8000
RUN chmod +x entry_point.sh
CMD ["./entry_point.sh"]