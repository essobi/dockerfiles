FROM pygmy/alpine-tini:edge  
  
MAINTAINER Maciej Lisiewski <maciej.lisiewski@gmail.com>  
  
ENV CONFIG "/data/pghoard/config.json"  
  
VOLUME /data/pghoard/  
  
RUN apk add --no-cache \  
ca-certificates \  
python3 \  
snappy \  
libffi \  
postgresql && \  
apk add --no-cache --virtual .build-deps \  
musl-dev \  
python3-dev \  
postgresql-dev \  
snappy-dev \  
libffi-dev \  
gcc \  
g++ && \  
python3 -m ensurepip && \  
pip3 install --upgrade pip setuptools && \  
pip3 install boto azure google-api-python-client cryptography
https://github.com/ohmu/pghoard/archive/master.zip && \  
rm -r /root/.cache && \  
apk del .build-deps  
  
CMD ["/usr/bin/pghoard", "--short-log"]

