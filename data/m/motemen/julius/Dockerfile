FROM ubuntu  
  
MAINTAINER motemen <motemen@gmail.com>  
  
ENV JULIUS_VERSION 4.3.1  
RUN apt-get update && apt-get install -y curl build-essential && apt-get clean  
  
RUN curl -s
http://jaist.dl.sourceforge.jp/julius/60273/julius-$JULIUS_VERSION.tar.gz |
tar -xvzf - && cd julius-$JULIUS_VERSION && ./configure && make && make
install  
RUN mkdir -p /opt/julius && curl -s
http://jaist.dl.sourceforge.jp/julius/60416/dictation-kit-v$JULIUS_VERSION-
linux.tgz | tar -C /opt/julius -xvzf -  

