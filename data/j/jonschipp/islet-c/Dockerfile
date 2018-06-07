# C  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER demo  
  
RUN apt-get update -qq  
RUN apt-get install -y build-essential  
RUN apt-get install -y git vim emacs nano tcpdump gawk rsyslog  
RUN apt-get install -y --no-install-recommends man-db  
RUN adduser --disabled-password --gecos "" $VIRTUSER  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  

