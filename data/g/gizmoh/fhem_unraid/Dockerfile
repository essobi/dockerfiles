# Version 2 1/2017  
# Changes:  
# * added volumedata2.sh - extracts data from a tgz when using empty host
volumes  
# * added superivsord config for fhem running foreground  
# * supervisor web at port 9001 export  
# * added service sshd to supervisord  
FROM debian:jessie  
MAINTAINER Armin Pipp <armin@pipp.at>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Install dependencies  
RUN apt-get update  
# RUN apt-get -y --force-yes install apt-utils  
RUN apt-get -y --force-yes install wget git nano make gcc g++ apt-transport-
https libavahi-compat-libdnssd-dev sudo nodejs etherwake && apt-get clean  
RUN apt-get -y --force-yes install mc vim htop snmp lsof libssl-dev telnet-ssl
imagemagick dialog curl usbutils && apt-get clean  
  
# Install arp-scan and hping3 for precence detection  
RUN apt-get -y --force-yes install arp-scan hping3 && apt-get clean  
  
# Fix for FHEM 5.8  
RUN apt-get -y --force-yes install sqlite3 libdbd-sqlite3-perl libtext-diff-
perl && apt-get clean  
  
# Additional packages  
RUN apt-get -y --force-yes install libio-socket-multicast-perl cpanminus
libjson-perl libsoap-lite-perl && apt-get clean  
RUN cpan install Net::WebSocket::Server  
RUN cpan install JSON  
RUN cpan Crypt::Rijndael_PP  
RUN cpan Crypt::Cipher::AES  
  
# Firmware flash  
RUN apt-get -y --force-yes install avrdude git-core gcc-avr avr-libc && apt-
get clean  
  
# Install perl packages  
RUN apt-get -y --force-yes install libalgorithm-merge-perl \  
libcrypt-ecb-perl \  
libclass-isa-perl \  
libcommon-sense-perl \  
libdpkg-perl \  
liberror-perl \  
libfile-copy-recursive-perl \  
libfile-fcntllock-perl \  
libio-socket-ip-perl \  
libjson-perl \  
libjson-xs-perl \  
libmail-sendmail-perl \  
libsocket-perl \  
libswitch-perl \  
libsys-hostname-long-perl \  
libterm-readkey-perl \  
libterm-readline-perl-perl \  
libsnmp-perl \  
libnet-telnet-perl \  
libmime-lite-perl \  
libxml-simple-perl \  
libdigest-crc-perl \  
libcrypt-cbc-perl \  
libio-socket-timeout-perl \  
libmime-lite-perl \  
libany-uri-escape-perl \  
libdevice-serialport-perl && apt-get clean  
  
# whatsapp Python yowsup  
RUN apt-get -y --force-yes install python-soappy python-dateutil python-pip
python-dev build-essential libgmp10 && apt-get clean  
# whatsapp images  
RUN apt-get -y --force-yes install libtiff5-dev libjpeg-dev zlib1g-dev
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk &&
apt-get clean  
  
# Pyhton stuff  
RUN pip install --upgrade setuptools  
RUN pip install --upgrade pip \  
&& pip install python-axolotl --upgrade \  
&& pip install pillow --upgrade  
  
RUN pip install yowsup2 --upgrade  
  
# install yowsup-client  
WORKDIR /opt  
RUN mkdir /opt/yowsup-config  
RUN wget -N https://github.com/tgalal/yowsup/archive/master.zip  
RUN unzip -o master.zip && rm master.zip  
  
WORKDIR /opt  
# install fhem (debian paket)  
RUN wget http://fhem.de/fhem-5.8.deb  
RUN dpkg -i fhem-5.8.deb  
# RUN rm fhem.deb  
RUN echo 'fhem ALL = NOPASSWD:ALL' >>/etc/sudoers  
RUN echo 'attr global pidfilename /var/run/fhem/fhem.pid' >>
/opt/fhem/fhem.cfg  
RUN echo 'define Wetter_Villach Weather 540859 1800 de' >> /opt/fhem/fhem.cfg  
  
RUN apt-get -y --force-yes install supervisor  
RUN mkdir -p /var/log/supervisor  
  
# Do some stuff  
RUN echo Europe/Vienna > /etc/timezone && dpkg-reconfigure tzdata \  
&& apt-get -y --force-yes install at cron && apt-get clean  
  
# sshd on port 2222 and allow root login / password = fhem!  
RUN apt-get -y --force-yes install openssh-server && apt-get clean \  
&& sed -i 's/Port 22/Port 2222/g' /etc/ssh/sshd_config \  
&& sed -i 's/PermitRootLogin no/PermitRootLogin yes/g' /etc/ssh/sshd_config \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config \  
&& echo "root:fhem!" | chpasswd \  
&& /bin/rm /etc/ssh/ssh_host_*  
# RUN dpkg-reconfigure openssh-server  
# dbi, svg, sound  
RUN apt-get -y --force-yes install libdbd-pg-perl \  
libdbi-perl \  
libdbd-sqlite3-perl \  
sqlite3 \  
libclass-dbi-mysql-perl \  
mysql-client \  
libdbd-mysql \  
libdbd-mysql-perl \  
libimage-librsvg-perl \  
libav-tools \  
&& apt-get clean  
  
# NFS client / autofs  
RUN apt-get -y --force-yes install nfs-common autofs && apt-get clean && apt-
get autoremove  
RUN echo "/net /etc/auto.net --timeout=60" >> /etc/auto.master  
  
ENV RUNVAR fhem  
WORKDIR /root  
  
# SSH / Fhem ports  
EXPOSE 2222 7072 8083 8084 8085 9001  
ADD run.sh /root/  
ADD runfhem.sh /root/  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir /_cfg  
ADD volumedata2.sh /_cfg/  
RUN chmod +x /root/run.sh && chmod +x /_cfg/*.sh  
RUN /_cfg/volumedata2.sh create /opt/fhem \  
&& /_cfg/volumedata2.sh create /opt/yowsup-config \  
&& touch /opt/yowsup-config/empty.txt  
  
ENTRYPOINT ["./run.sh"]  
#CMD ["arg1"]  
# last add volumes  
VOLUME /opt/fhem /opt/yowsup-config  
  
# End Dockerfile  

