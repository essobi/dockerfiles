FROM ubuntu:16.04  
MAINTAINER gliacloud <robot@gliacloud.com>  
  
  
RUN apt-get update && \  
apt-get install -y locales \  
libssl-dev \  
openssl \  
imagemagick \  
ffmpeg \  
libfreeimage-dev \  
libjpeg-dev \  
libpng-dev \  
libffi-dev \  
libblas-dev \  
liblapack-dev \  
libatlas-base-dev \  
gfortran \  
python-pip \  
wget \  
libevent-dev \  
python-dev \  
libxml2-dev \  
libxslt1-dev \  
python-lxml \  
libpq-dev \  
curl \  
git \  
unzip \  
python-numpy \  
python-sklearn \  
python-skimage \  
python-gevent \  
python-libsass \  
software-properties-common \  
python-mysqldb && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
  
RUN locale-gen zh_TW.UTF-8  
ENV LANG zh_TW.UTF-8  
ENV LANGUAGE zh_TW:en  
ENV LC_ALL zh_TW.UTF-8  
  
RUN pip install -U pip  
run rm /etc/ImageMagick-6/policy.xml  
ADD requirements.txt /tmp/requirement.txt  
RUN pip install -r /tmp/requirement.txt  

