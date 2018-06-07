FROM doublexminus/xx-ubuntu16.04  
  
MAINTAINER doublexminus <samson@vgraevenitz.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install wget apt-transport-https  
  
# Install perl packages  
RUN apt-get -y install libalgorithm-merge-perl \  
libclass-isa-perl \  
libcommon-sense-perl \  
libdpkg-perl \  
liberror-perl \  
libfile-copy-recursive-perl \  
libfile-fcntllock-perl \  
libio-socket-ip-perl \  
libio-socket-multicast-perl \  
libjson-perl \  
libjson-xs-perl \  
libmail-sendmail-perl \  
libsocket-perl \  
libswitch-perl \  
libsys-hostname-long-perl \  
libterm-readkey-perl \  
libterm-readline-perl-perl \  
libxml-simple-perl \  
libwww-perl \  
libsoap-lite-perl \  
libjson-xs-perl \  
libnet-telnet-perl \  
iputils-ping \  
ssh \  
sshpass  
  
  
  
RUN wget -qO - https://debian.fhem.de/archive.key | apt-key add -  
RUN echo "deb https://debian.fhem.de/nightly ./" | tee -a
/etc/apt/sources.list.d/fhem.list  
RUN apt-get update  
RUN apt-get -y install supervisor fhem telnet  
RUN mkdir -p /var/log/supervisor  
  
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/opt/fhem"]  
EXPOSE 8083  
  
CMD ["/usr/bin/supervisord"]  

