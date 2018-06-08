FROM ubuntu:14.10  
MAINTAINER Gil Gyeong-Min "rushcut@gmail.com"  
RUN apt-get -y update  
RUN apt-get -y install autopoint automake autoconf gettext libavformat-dev
libavutil-dev libavcodec-dev libFLAC-dev libvorbis-dev libid3tag0-dev libexif-
dev libjpeg-dev libsqlite3-dev libogg-dev wget  
  
ENV MINIDLNA_VERSION 1.1.4  
RUN mkdir -p /tmp/minidlna  
RUN wget -O /tmp/minidlna/minidlna.tar.gz
http://sourceforge.net/projects/minidlna/files/minidlna/${MINIDLNA_VERSION}/minidlna-${MINIDLNA_VERSION}.tar.gz  
RUN cd /tmp/minidlna && tar --strip-components 1 -xvf minidlna.tar.gz &&
./configure && make && make install  
RUN mkdir -p /etc/minidlna  
RUN cp /tmp/minidlna/minidlna.conf /etc/minidlna/minidlna.conf  
  
VOLUME /etc/minidlna  
VOLUME /opt  
  
EXPOSE 1900/udp  
EXPOSE 8200  
CMD ["/usr/local/sbin/minidlnad", "-d", "-f", "/etc/minidlna/minidlna.conf"]  

