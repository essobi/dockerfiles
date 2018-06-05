FROM debian:jessie-slim  
MAINTAINER Leonardo Loures <luvres@hotmail.com>  
  
ENV PATH=/opt/anaconda3/bin:$PATH \  
NOTEBOOKS_PATH=/root/notebooks  
  
RUN \  
apt-get update \  
&& apt-get install -y \  
curl git zsh \  
bzip2 \  
build-essential \  
\  
# Anaconda3  
&& ANACONDA_VERSION=5.0.1 \  
&& curl -L
https://repo.continuum.io/archive/Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh
\  
-o Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh \  
\  
&& /bin/bash Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -b -p
/usr/local/anaconda3 \  
&& ln -s /usr/local/anaconda3/ /opt/anaconda3 \  
&& rm Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh \  
\  
&& pip install --upgrade pip \  
&& pip install \  
mrjob \  
shapely \  
selenium \  
termcolor \  
scrapy \  
js2xml \  
\  
&& mkdir $NOTEBOOKS_PATH  
  
WORKDIR $NOTEBOOKS_PATH  
  
# Jupyter Notebook port  
EXPOSE 8888  
  

