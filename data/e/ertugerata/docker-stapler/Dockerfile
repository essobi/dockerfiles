#ertugerata/docker-stapler  
FROM python:2.7-alpine3.7  
LABEL maintainer Ertuğrul Erata <ertugrulerata@gmail.com>  
  
RUN pip install --no-cache stapler  
  
WORKDIR /root  
  
ENTRYPOINT ["/usr/local/bin/stapler"]  

