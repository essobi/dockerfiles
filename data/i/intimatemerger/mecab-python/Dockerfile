FROM python:2.7.12  
  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
RUN apt-get update && \  
apt-get install -y mecab=0.996-1.1 \  
libmecab-dev=0.996-1.1 \  
mecab-ipadic-utf8 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
pip install mecab-python==0.996  

