FROM ubuntu:16.04  
MAINTAINER Sebastien Langoureaux <linuxworkgroup@hotmail.com> base on JP
<jportela@abyssal.eu>  
ENV LANG en_US.utf8  
  
ENV LC_ALL C  
  
RUN apt-get update && apt-get install --no-install-recommends -yq \  
python-all \  
python-pip \  
python-nose \  
python-mock \  
python-setuptools \  
python-dev \  
libpq-dev \  
build-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --upgrade pip  
  
  
ENV PYTHONIOENCODING utf-8  
WORKDIR /code  

