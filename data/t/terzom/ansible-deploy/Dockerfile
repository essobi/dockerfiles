FROM python:2.7-alpine  
  
MAINTAINER Mike Terzo <mike@terzo.org>  
  
ENV ANSIBLE_HOST_KEY_CHECKING=False  
ENV LANG C.UTF-8  
RUN mkdir -p /src/  
WORKDIR /src  
COPY requirements.txt /src  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
git \  
libffi \  
openssh \  
openssl \  
rsync \  
sshpass \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
libffi-dev \  
linux-headers \  
make \  
openssl-dev \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apk del .build-deps  
  
RUN ln -s /usr/local/bin/python /usr/bin/python  
  
COPY root /root  

