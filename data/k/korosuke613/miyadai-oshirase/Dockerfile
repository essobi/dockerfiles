FROM ubuntu:16.04  
# 作者の指定  
MAINTAINER Futa HIRAKOBA  
  
# 作業用ディレクトリの生成、移動  
WORKDIR /home/tmp  
  
# makeのラッパースクリプトを追加  
ADD requirements.txt /home/tmp  
  
# Update and Upgrade  
RUN apt-get update && apt-get upgrade -y && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y \  
apt-file \  
software-properties-common \  
wget \  
git \  
bzip2 \  
libfontconfig \  
imagemagick && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Python3.6のインストール  
RUN add-apt-repository -y ppa:jonathonf/python-3.6 && \  
apt-get -y update && \  
apt-get install -y python3.6 python3.6-dev && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python3.6 get-pip.py && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Pythonライブラリのインストール  
RUN pip3 install -r requirements.txt  
  
# PhantomJSのインストール  
WORKDIR /tmp  
RUN wget -O /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar -xvjf /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/  

