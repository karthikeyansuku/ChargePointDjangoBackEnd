FROM python:3
WORKDIR /ChargePointDjangoBackEnd
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./entry_point.sh .
RUN sed -i 's/\r$//g' /ChargePointDjangoBackEnd/entry_point.sh
RUN chmod +x /ChargePointDjangoBackEnd/entry_point.sh
COPY . .
ENTRYPOINT ["/ChargePointDjangoBackEnd/entry_point.sh"]
