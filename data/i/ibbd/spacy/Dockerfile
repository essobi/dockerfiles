#  
# tensorflow Dockerfile  
#  
#  
# Pull base image.  
FROM python:3.6-slim  
  
MAINTAINER Alex Cai "cyy0523xc@gmail.com"  
# config  
RUN mkdir -p /var/www \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
python-dev \  
git \  
python3-pip \  
&& pip3 install -U pip  
  
ENV SPACY_VERSION 2.0.3  
# spacy  
RUN \  
pip3 install -U jieba \  
ipython \  
numpy \  
pandas \  
requests \  
chardet \  
&& pip3 install -U spacy==${SPACY_VERSION} \  
&& python3 -m spacy download en \  
&& python3 -m spacy download xx  
  
  
# Define working directory.  
WORKDIR /var/www  
  
# 解决时区问题  
ENV TZ "Asia/Shanghai"  

