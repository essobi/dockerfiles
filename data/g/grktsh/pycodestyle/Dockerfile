FROM alpine:3.6  
ENV PYTHONUNBUFFERED 1  
RUN apk add --no-cache python3  
  
ENV PYCODESTYLE_VERSION 2.3.1  
RUN python3 -m pip install --no-cache-dir pycodestyle==$PYCODESTYLE_VERSION  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  

