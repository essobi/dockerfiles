FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
ENV REFRESHED_AT 2016-03-14-19-03  
RUN apt-get -y update && \  
apt-get -y install python-pip && \  
pip install -U awscli && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  

