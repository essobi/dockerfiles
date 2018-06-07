FROM ubuntu:14.04  
MAINTAINER David Barbarisi <dbarbarisi@industrydive.com>  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q \  
build-essential \  
git \  
python \  
python-dev \  
python-setuptools \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
ENV PYTHONUNBUFFERED 1  
  
RUN easy_install pip  
RUN pip install virtualenv  

