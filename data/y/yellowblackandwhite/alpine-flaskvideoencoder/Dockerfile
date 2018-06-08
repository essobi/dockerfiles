FROM yellowblackandwhite/alpine-alpineffmpeg  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
COPY requirements.txt /tmp/  
RUN apk add build-base gmp-dev libffi-dev openssl-dev && \  
pip3 install --upgrade -r /tmp/requirements.txt && \  
apk del build-base gmp-dev openssl-dev && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
EXPOSE 8000  
USER alpine  

