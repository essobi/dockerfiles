#FROM perl:latest  
FROM ubuntu:latest  
MAINTAINER nkmry <nkmry333@gmail.com>  
  
WORKDIR /root  
  
# to use Japanese  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
ENV LC_ALL ja_JP.UTF-8  
  
RUN apt-get update \--fix-missing &&\  
apt-get upgrade -y --fix-missing &&\  
#RUN apt-get install -y --fix-missing build-essential  
apt-get install -y --fix-missing wget &&\  
apt-get install -y --fix-missing gcc &&\  
apt-get install -y --fix-missing g++ &&\  
apt-get install -y --fix-missing make &&\  
# to decompress *.tar.bz2  
apt-get install -y --fix-missing bzip2 &&\  
  
# to use Japanese  
apt-get install -y locales --no-install-recommends &&\  
rm -rf /var/lib/apt/lists/* &&\  
locale-gen ja_JP.UTF-8 &&\  
  
# install JUMAN  
wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-7.01.tar.bz2 &&\  
tar xf juman-7.01.tar.bz2 &&\  
cd juman-7.01/ &&\  
./configure && make && make install &&\  
cd .. &&\  
rm juman-7.01.tar.bz2 && rm -rf juman-7.01 &&\  
apt-get update && apt-get install -y --fix-missing libjuman4 &&\  
# install KNP  
apt-get install -y --fix-missing zlib1g-dev &&\  
wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-4.16.tar.bz2 &&\  
tar xf knp-4.16.tar.bz2 &&\  
cd knp-4.16/ &&\  
./configure && make && make install &&\  
cd .. &&\  
rm knp-4.16.tar.bz2 && rm -rf knp-4.16  

