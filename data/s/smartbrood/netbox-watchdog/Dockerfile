FROM python:3.6-alpine  
MAINTAINER Andrey N. Petrov <andreynpetrov@gmail.com>  
  
ENV PYTHONUNBUFFERED=1  
  
RUN apk add --no-cache \  
bash \  
build-base \  
ca-certificates \  
cyrus-sasl-dev \  
graphviz \  
ttf-ubuntu-font-family \  
jpeg-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
openssl-dev \  
mercurial  
  
RUN pip install \  
schedule \  
python-libmaas \  
python-netbox \  
slackclient \  
napalm \  
python-hglib \  
ipython  
  
ENTRYPOINT ["/netbox-watchdog.py"]  

