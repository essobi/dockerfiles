# Volatility  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER demo  
  
RUN apt-get update -qq  
RUN apt-get install -y python python-dev volatility yara python-yara pcregrep
libpcre++-dev python-pycryptopp  
RUN apt-get install -y wget unzip vim emacs nano tcpdump gawk rsyslog  
RUN wget http://distorm.googlecode.com/files/distorm3.zip && unzip
distorm3.zip && \  
cd distorm3 && python setup.py build && python setup.py build install  
RUN wget http://malwarecookbook.googlecode.com/svn/trunk/malware.py -O
/usr/share/volatility/contrib/plugins/malware.py  
RUN apt-get install -y --no-install-recommends man-db  
RUN echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig  
RUN adduser --disabled-password --gecos "" $VIRTUSER  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  

