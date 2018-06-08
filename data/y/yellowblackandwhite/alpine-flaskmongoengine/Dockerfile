FROM yellowblackandwhite/alpine-flask  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
COPY requirements.txt /tmp/  
RUN apk --update add build-base python3-dev gmp-dev && \  
pip3 install --upgrade -r /tmp/requirements.txt && \  
apk del build-base python3-dev gmp-dev && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
USER alpine  

