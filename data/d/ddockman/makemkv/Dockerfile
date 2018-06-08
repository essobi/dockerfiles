FROM ubuntu:trusty  
  
ENV LANG en_US.UTF-8  
ENV VERSION 1.10.2  
#RUN locale-gen $LANG  
RUN apt-get update -q  
RUN apt-get install -yqq build-essential pkg-config libc6-dev libssl-dev
libexpat1-dev libavcodec-dev libgl1-mesa-dev libqt4-dev  
  
ADD http://www.makemkv.com/download/makemkv-oss-$VERSION.tar.gz /tmp/makemkv-
oss-$VERSION.tar.gz  
RUN tar xzf /tmp/makemkv-oss-$VERSION.tar.gz && \  
rm /tmp/makemkv-oss-$VERSION.tar.gz && \  
cd /makemkv-oss-$VERSION && \  
./configure && \  
make && \  
make install && \  
rm -rf /makemkv-oss-$VERSION  
  
ADD http://www.makemkv.com/download/makemkv-bin-$VERSION.tar.gz /tmp/makemkv-
bin-$VERSION.tar.gz  
RUN tar xzf /tmp/makemkv-bin-$VERSION.tar.gz && \  
rm /tmp/makemkv-bin-$VERSION.tar.gz && \  
cd /makemkv-bin-$VERSION && \  
yes yes | make && \  
make install && \  
rm -rf /makemkv-bin-$VERSION  
  
RUN mkdir /data  
VOLUME ["/data"]  
  
#CMD ["/start.sh"]  

