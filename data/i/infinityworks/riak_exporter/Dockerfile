FROM python:3.5-alpine  
  
ADD . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN pip install -e /usr/src/app  
  
ENTRYPOINT ["riak-exporter"]  

