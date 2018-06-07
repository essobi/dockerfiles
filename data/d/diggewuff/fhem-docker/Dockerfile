## Copyright (c) 2018 Joscha Middendorf  
  
FROM debian:stretch  
  
MAINTAINER Joscha Middendorf <joscha.middendorf@me.com>  
  
ENV FHEM_VERSION=5.8 \  
DEBIAN_FRONTEND=noninteractive \  
TERM=xterm\  
TZ=Europe/Berlin  
  
RUN \  
## update and upgrade APT  
apt-get update \  
&& apt-get -qqy dist-upgrade \  
## Install dependencies  
&& apt-get -qqy install \  
apt-transport-https \  
bluez \  
build-essential \  
curl \  
dfu-programmer \  
etherwake \  
git \  
nano \  
perl \  
python \  
screenfetch \  
snmp \  
snmpd \  
sqlite3 \  
sudo \  
telnet-ssl \  
usbutils \  
wget \  
#at \  
#cron \  
#bluetooth \  
#dialog \  
#g++ \  
#gcc \  
#htop \  
#imagemagick \  
#libavahi-compat-libdnssd-dev \  
#libssl-dev \  
#lsof \  
#make \  
#mc \  
#mysql-client \  
#nodejs \  
#vim \  
## Install perl packages  
&& apt-get -qqy install \  
libalgorithm-merge-perl \  
libauthen-oath-perl \  
libavahi-compat-libdnssd-dev \  
libcgi-pm-perl \  
libclass-dbi-mysql-perl \  
libclass-isa-perl \  
libcommon-sense-perl \  
libconvert-base32-perl \  
libcrypt-cbc-perl \  
libcrypt-ecb-perl \  
libcrypt-urandom-perl \  
libdata-dump-perl \  
libdatetime-format-strptime-perl \  
libdbd-sqlite3-perl \  
libdbi-perl \  
libdevice-serialport-perl \  
libdigest-md5-perl \  
libdpkg-perl \  
liberror-perl \  
libfile-copy-recursive-perl \  
libfile-fcntllock-perl \  
libgd-graph-perl \  
libgd-text-perl \  
libimage-info-perl \  
libimage-librsvg-perl \  
libio-socket-inet6-perl \  
libio-socket-ip-perl \  
libio-socket-multicast-perl \  
libio-socket-ssl-perl \  
libio-socket-timeout-perl \  
libjson-perl \  
libjson-xs-perl \  
liblist-moreutils-perl \  
libmail-imapclient-perl \  
libmail-sendmail-perl \  
libmime-base64-perl \  
libmodule-pluggable-perl \  
libnet-telnet-perl \  
librpc-xml-perl \  
libsoap-lite-perl \  
libsocket-perl \  
libsocket6-perl \  
libswitch-perl \  
libsys-hostname-long-perl \  
libsys-statistics-linux-perl \  
libterm-readkey-perl \  
libterm-readline-perl-perl \  
libtext-csv-perl \  
libtext-diff-perl \  
libtimedate-perl \  
libwww-perl \  
libxml-simple-perl \  
#libav-tools \  
#libdbd-mysql \  
#libdbd-mysql-perl \  
#libdbd-pg-perl \  
#libdigest-crc-perl \  
#libio-socket-timeout-perl \  
#libmime-lite-perl \  
#libsnmp-perl \  
## Clean up APT when done  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## Install Perl Modules from CPAN  
RUN cpan install \  
Crypt::Cipher::AES \  
#Crypt::Rijndael_PP \  
Net::MQTT::Constants \  
Net::MQTT::Simple \  
Text::Diff  
  
## Customize console  
RUN echo "alias ll='ls -lah --color=auto'" >> /root/.bashrc \  
&& echo "screenfetch" >> /root/.bashrc  
  
## Install Speedtest-CLI  
RUN wget -O /usr/local/bin/speedtest-cli
https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py \  
&& chmod +x /usr/local/bin/speedtest-cli  
  
## Install FHEM (FHEM_VERSION)  
RUN wget https://fhem.de/fhem-${FHEM_VERSION}.deb \  
&& dpkg -i fhem-${FHEM_VERSION}.deb \  
&& rm fhem-${FHEM_VERSION}.deb \  
&& userdel fhem  
  
## add basic configation and scripts  
COPY fhem.cfg /opt/fhem/  
COPY controls.txt /opt/fhem/FHEM/  
COPY StartAndInitialize.sh healthcheck.sh /root/  
RUN chmod +x /root/*.sh  
  
## Compress FHEM base data from /opt/fhem/ to /root/ for later initialisation
of volumes  
  
RUN /root/StartAndInitialize.sh initialize /opt/fhem  
  
## open ports  
EXPOSE 7072 8083 8084 8085 8086 8087 8088 8089  
  
## add volumes  
VOLUME /opt/fhem  
  
## Healthcheck  
HEALTHCHECK --interval=20s --timeout=10s --start-period=60s --retries=5 CMD
/root/healthcheck.sh  
  
## Entrypoint  
ENTRYPOINT ["/root/StartAndInitialize.sh"]  
CMD ["extract", "/opt/fhem"]  
  
## End Dockerfile  

