FROM python:3.6-alpine  
  
RUN apk update \  
&& apk add \  
bzip2-dev \  
gcc \  
libc-dev \  
linux-headers \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
postgresql-dev \  
&& pip install uwsgi psycopg2 --no-cache-dir \  
&& rm -rf /var/cache/apk/*

