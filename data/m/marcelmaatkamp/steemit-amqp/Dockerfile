FROM python:3-alpine  
  
RUN apk add --update build-base openssl-dev &&\  
pip3 install steem pika &&\  
rm -rf /var/cache/apk/*  
  
WORKDIR /app  
COPY *.py /app/  
  
CMD ["python", "-u", "amqp.py"]  

