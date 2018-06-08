#  
FROM centos:7  
MAINTAINER Pornchai Rungsirijaratthong <songpr@gmail.com>  
  
  
ENV LIBDATRIE_VERSION 0.2.10  
ENV SWATH_VERSION 0.5.5  
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig/  
  
# Define SWATH_SRC_HOME variable  
ENV SWATH_SRC_HOME /opt/swath  
  
RUN yum -y update && \  
yum -y install wget && \  
yum -y install deltarpm && \  
yum -y groupinstall 'Development Tools'  
  
RUN mkdir /opt/swath && \  
cd /opt/swath && \  
wget
http://linux.thai.net/pub/ThaiLinux/software/libthai/libdatrie-${LIBDATRIE_VERSION}.tar.xz
&& \  
tar -xf libdatrie-${LIBDATRIE_VERSION}.tar.xz && \  
rm libdatrie-${LIBDATRIE_VERSION}.tar.xz && \  
cd /opt/swath/libdatrie-${LIBDATRIE_VERSION} && \  
./configure && make && make install  
  
RUN cd /opt/swath && \  
wget
http://linux.thai.net/pub/thailinux/software/swath/swath-${SWATH_VERSION}.tar.xz
&& \  
tar -xf swath-${SWATH_VERSION}.tar.xz && \  
rm swath-${SWATH_VERSION}.tar.xz && \  
cd /opt/swath/swath-${SWATH_VERSION} && \  
./configure && make && make install  
  
VOLUME ["/opt/swath"]  
  
WORKDIR /opt/swath  
  

