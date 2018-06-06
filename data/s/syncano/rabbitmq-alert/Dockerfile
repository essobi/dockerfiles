FROM python:2-alpine  
  
COPY . /app  
WORKDIR /app  
RUN python setup.py install  
  
CMD ["rabbitmq-alert"]  

