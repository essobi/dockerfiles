FROM ubuntu:zesty  
MAINTAINER Jetsada Machom jim@imjim.im  
  
RUN apt-get update && \  
apt-get install -y wget python && \  
wget -q -O /opt/oclint-0.11.tar.gz
https://github.com/oclint/oclint/releases/download/v0.11/oclint-0.11-x86_64-linux-4.4.0-36-generic.tar.gz
&& \  
tar xzvf /opt/oclint-0.11.tar.gz -C /opt/ && \  
apt-get autoclean && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH /opt/oclint-0.11/bin:$PATH  
  
RUN mkdir /app  
WORKDIR /app  
VOLUME /app  
  
CMD ["oclint"]  

