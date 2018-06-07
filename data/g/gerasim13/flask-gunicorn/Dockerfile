FROM gerasim13/flask  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
  
RUN apk --update add build-base python3-dev gmp-dev  
COPY requirements.txt /tmp/  
RUN pip3 install --upgrade -r /tmp/requirements.txt  
RUN apk del build-base python3-dev gmp-dev && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /root/.cache/

