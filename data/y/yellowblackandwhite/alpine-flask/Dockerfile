FROM yellowblackandwhite/alpine-gunicorn  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
ENV WERKZEUG_DEBUG_PIN 'off'  
COPY requirements.txt /tmp/  
RUN apk --update add build-base py-openssl py-cryptography python3-dev
libxml2-dev libxslt-dev gmp-dev && \  
pip3 install --upgrade -r /tmp/requirements.txt && \  
apk del build-base python3-dev gmp-dev && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
EXPOSE 8000  
USER alpine  

