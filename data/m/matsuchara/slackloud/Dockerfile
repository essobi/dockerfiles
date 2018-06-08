FROM ubuntu:14.04  
MAINTAINER matsu_chara<matsuy00@gmail.com>  
  
RUN apt-get -y update  
  
# install mecab  
RUN apt-get -y --no-install-recommends install \  
mecab=0.996-1.1 libmecab-dev=0.996-1.1 \  
mecab-ipadic-utf8=2.7.0-20070801+main-1 \  
git=1:1.9.1-1ubuntu0.3 ca-certificates=20160104ubuntu0.14.04.1 \  
make=3.81-8.2ubuntu3 xz-utils=5.1.1alpha+20120614-2ubuntu2 \  
curl=7.35.0-1ubuntu2.6 file=1:5.14-2ubuntu3.3 patch=2.7.1-4ubuntu2.3  
RUN update-ca-certificates  
  
# mecab-ipadic-neologd to /usr/lib/mecab/dic/mecab-ipadic-neologd/  
WORKDIR /app  
RUN git clone \--depth 1 https://github.com/neologd/mecab-ipadic-neologd.git  
RUN ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y  
  
# install python, pip  
RUN apt-get -y --no-install-recommends install \  
python3-dev=3.4.0-0ubuntu2 gcc=4:4.8.2-1ubuntu6 g++=4:4.8.2-1ubuntu6 \  
libfreetype6-dev=2.5.2-1ubuntu2.5 libxft-dev=2.3.1-2 \  
fonts-ipafont=00303-12ubuntu1  
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3  
  
# clean apt-get  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# install app  
COPY requirements.txt /app/  
RUN pip3 install -r requirements.txt  
  
### start: for debugging inside container  
# you can test your user_dict login with  
# `docker run -i -t --entrypoint=/bin/bash matsuchara/slackloud`  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
### end: for debugging inside container  
ENV PYTHONIOENCODING utf-8  
ENTRYPOINT ["python3", "/app/src/slackloud.py"]  

