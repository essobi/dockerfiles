FROM ubuntu:trusty  
  
MAINTAINER thomasbrinker <tbrinker@evoila.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
nano \  
make \  
gcc \  
g++ \  
apt-transport-https \  
sudo  
  
# Install packages for perl  
RUN apt-get install -y \  
perl-base \  
libdevice-serialport-perl \  
libwww-perl \  
libio-socket-ssl-perl \  
libcgi-pm-perl \  
libjson-perl \  
sqlite3 \  
libdbd-sqlite3-perl \  
libtext-diff-perl \  
libtimedate-perl \  
libmail-imapclient-perl \  
libgd-graph-perl \  
libtext-csv-perl \  
libxml-simple-perl \  
liblist-moreutils-perl \  
ttf-liberation \  
libimage-librsvg-perl \  
libgd-text-perl \  
libsocket6-perl \  
libio-socket-inet6-perl \  
libmime-base64-perl \  
libimage-info-perl \  
libusb-1.0-0-dev \  
libnet-server-perl  
  
# Install fhem alternativ  
RUN wget https://debian.fhem.de/fhem.deb  
RUN dpkg -i fhem.deb  
RUN cp /opt/fhem/contrib/init-scripts/fhem.3 /etc/init.d/fhem  
RUN chmod a+x /etc/init.d/fhem  
RUN update-rc.d fhem defaults  
  
# setting timezone  
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure tzdata  
  
# Install supervisord for enabling sshd access to the docker container  
#RUN apt-get update && apt-get install -y openssh-server apache2 supervisor  
#RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
#COPY ./fhem/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
VOLUME ["/opt/fhem"]  
  
# Ports for fhem  
EXPOSE 8083 8084 8085  
# Port for supervisord  
#EXPOSE 22 80  
#CMD ["/usr/bin/supervisord"]  
CMD ["/etc/init.d/fhem","start"]  

