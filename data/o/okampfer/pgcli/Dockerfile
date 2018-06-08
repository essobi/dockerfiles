FROM python:3.5-alpine  
  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
RUN apk add --no-cache \  
python3 \  
libevent \  
libpq && \  
apk add --no-cache --virtual .build-deps \  
python3-dev \  
postgresql-dev \  
libevent-dev \  
musl-dev \  
gcc && \  
python -m ensurepip && \  
pip install --upgrade pip && \  
pip install pgcli && \  
apk del .build-deps && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
ENTRYPOINT ["/usr/local/bin/pgcli"]  
CMD ["--help"]  

