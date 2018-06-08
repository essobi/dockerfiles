FROM python:3-alpine  
EXPOSE 8080  
# Requirements to compile greenlet and gevent  
RUN apk add gcc musl-dev --no-cache  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY data.json /usr/src/app/data.json  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
CMD ["/usr/src/app/server.py"]  

