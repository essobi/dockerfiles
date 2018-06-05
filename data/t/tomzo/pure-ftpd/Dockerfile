  
FROM phusion/baseimage:0.9.17  
# feel free to change this ;)  
MAINTAINER Tomasz Setkowski <tom@ai-traders.com>  
  
# properly setup debian sources  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update  
  
# install package building helpers  
RUN apt-get -y --force-yes install dpkg-dev debhelper  
  
# install dependancies  
RUN apt-get -y build-dep pure-ftpd  
  
# build from source  
RUN mkdir /tmp/pure-ftpd/ && \  
cd /tmp/pure-ftpd/ && \  
apt-get source pure-ftpd && \  
cd pure-ftpd-* && \  
sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \  
dpkg-buildpackage -b -uc  
  
# install the new deb files  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb  
RUN apt-get -y install openbsd-inetd  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd_*.deb  
  
# Prevent pure-ftpd upgrading  
RUN apt-mark hold pure-ftpd pure-ftpd-common  
  
# setup ftpgroup and ftpuser  
RUN groupadd ftpgroup  
RUN useradd -g ftpgroup -d /dev/null -s /etc ftpuser  
  
RUN mkdir /ftp && useradd ftp --home /ftp && chown ftp:ftp /ftp  
  
RUN mkdir /etc/service/pure-ftp  
ADD run /etc/service/pure-ftp/run  
  
ADD my_init_fug.sh /sbin/my_init_fug  
  
VOLUME /ftp  
  
# startup  
CMD /sbin/my_init_fug  
  
EXPOSE 21/tcp  

