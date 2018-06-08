FROM debian:stretch  
  
MAINTAINER michaelatdocker <michael.kunzmann@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Base Packages  
RUN apt-get update && apt-get -y install apt-utils wget apt-transport-https
supervisor telnet  
  
# Setup Supervisor  
RUN mkdir -p /var/log/supervisor  
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
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
libcrypt-pbkdf2-perl \  
libcpan-meta-yaml-perl \  
libxml-simple-perl \  
build-essential  
  
RUN cpan install Net::MQTT:Simple  
  
# Install Fhem  
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure tzdata  
  
# Install Fhem via apt-get  
RUN touch /sbin/init  
RUN apt-get -y install gnupg  
RUN wget -qO - https://debian.fhem.de/archive.key | apt-key add -  
RUN echo "deb https://debian.fhem.de/nightly/ /" | tee -a
/etc/apt/sources.list.d/fhem.list  
RUN apt-get update  
RUN apt-get -y --force-yes install fhem  
RUN userdel fhem  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/opt/fhem"]  
EXPOSE 8083  
CMD ["/usr/bin/supervisord"]  
  

