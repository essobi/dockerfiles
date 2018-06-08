FROM python:3.6.5-alpine3.7  
RUN apk add --update --no-cache g++ gcc libxslt-dev postgresql-dev python3-dev
musl-dev  
WORKDIR /home/fundanl  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . .  
ENV PYTHONPATH /home

