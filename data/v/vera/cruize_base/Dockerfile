  
FROM centos:7  
MAINTAINER "Daniel Vera" vera@genomics.fsu.edu  
  
ENV CGI_BIN=/var/www/cgi-bin  
ENV SAMTABIXDIR=/opt/samtabix/  
ENV USE_SSL=1  
ENV USE_SAMTABIX=1  
ENV MACHTYPE=x86_64  
ENV
PATH=/root/bin/x86_64:/opt/samtabix/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV JKSRC=jksrc.zip  
  
RUN yum update -y && yum install -y \  
openssl-static.x86_64 \  
usbmuxd-devel.x86_64 \  
mariadb-devel.x86_64 \  
libimobiledevice-devel.x86_64 \  
ghostscript \  
libpng-devel.x86_64 \  
libplist-devel.x86_64 \  
gcc \  
libstdc++-devel.x86_64 \  
libstdc++-static.x86_64 \  
make \  
unzip \  
tcsh \  
perl \  
git \  
rsync \  
wget \  
gcc-c++  
  
RUN mkdir -p /root/bin/x86_64  
  
RUN git clone http://genome-source.cse.ucsc.edu/samtabix.git /opt/samtabix &&
cd /opt/samtabix && make  
  
RUN cd /opt && curl -sLo jksrc.zip
http://hgdownload.cse.ucsc.edu/admin/${JKSRC} && unzip -q jksrc.zip && rm -f
jksrc.zip  
RUN echo 'L+= -lz' >> /opt/kent/src/inc/common.mk  
RUN sed -i 's/hgBeacon//g;s/hgMirror//g' /opt/kent/src/hg/makefile  
RUN sed -i 's/#include <uuid\/uuid\\.h>//g' /opt/kent/src/inc/uuid.h  
RUN cd /opt/kent/src && make clean && make -j $(nproc) utils && make clean  

