FROM alpine:3.3  
MAINTAINER docker@libreelec.tv  
  
RUN apk add --update g++ \  
gcc \  
libffi \  
libffi-dev \  
libxml2 \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
make \  
openssl \  
openssl-dev \  
python \  
python-dev \  
py-pip \  
&& pip install --no-cache-dir cheetah \  
&& pip install --no-cache-dir configobj \  
&& pip install --no-cache-dir feedparser \  
&& pip install --no-cache-dir lxml \  
&& pip install --no-cache-dir pyOpenSSL \  
&& apk del --purge g++ \  
gcc \  
libffi-dev \  
make \  
libxml2-dev \  
libxslt-dev \  
openssl-dev \  
python-dev \  
py-pip \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.cache \  
&& rm -rf /tmp/*  

