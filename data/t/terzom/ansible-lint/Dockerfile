FROM python:2.7-alpine  
  
MAINTAINER Mike Terzo <mike@terzo.org>  
  
ENV LANG C.UTF-8  
RUN mkdir -p /src/  
WORKDIR /src  
COPY requirements.txt /src  
  
RUN apk add --no-cache --virtual .fetch-deps \  
gcc \  
libc-dev \  
libffi-dev \  
make \  
openssl-dev \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apk del .fetch-deps  
  
CMD ["/usr/local/bin/ansible-lint"]  

