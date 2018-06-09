FROM python:3.6-alpine  
  
RUN apk add --update gcc musl-dev && rm -rf /var/cache/apk/*  
  
WORKDIR /app  
  
COPY ./requirements.txt /app/requirements.txt  
  
RUN pip install -r requirements.txt  
  
COPY . /app  
  
EXPOSE 8000  
CMD gunicorn -c gunicorn_conf.py dnsfwd:app  

