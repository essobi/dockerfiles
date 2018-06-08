FROM alpine:latest  
MAINTAINER playniuniu@gmail.com  
  
ENV REDIS_BROKER="redis://redis:6379/0"  
RUN apk add --no-cache --update python3 \  
&& pyvenv /env \  
&& /env/bin/pip install --no-cache-dir redis flower \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /env/bin/flower /usr/bin/flower  
  
EXPOSE 5555  
CMD /env/bin/flower --port=5555 --broker=${REDIS_BROKER}  

