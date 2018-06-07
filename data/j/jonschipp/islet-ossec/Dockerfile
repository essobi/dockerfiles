# OSSEC  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER root  
  
# OSSEC version  
ENV VERSION 2.8.1  
RUN apt-get update -qq  
RUN apt-get install -y build-essential  
RUN apt-get install -y wget git vim emacs nano tcpdump gawk rsyslog  
RUN cd /root && wget -U "Mozilla" http://www.ossec.net/files/ossec-
hids-$VERSION.tar.gz  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  

