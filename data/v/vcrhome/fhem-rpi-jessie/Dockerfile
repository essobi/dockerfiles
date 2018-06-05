### Set Timezone "Europe/Berlin"  
### Install dependencies  
## Main Tools and extras  
# apt-utils apt-transport-https bash wget curl unzip python-pip  
# htop vim usbutils etherwake sudo xterm imagemagick snmp lsof avahi-daemon  
# supervisor cron openssh-server nfs-common autofs nodejs  
## Firmware flash and compile  
# build-essential git make gcc g++ gcc-avr avr-libc dialog avrdude  
## FHEM  
# perl-base libdevice-serialport-perl libwww-perl libio-socket-ssl-perl
libcgi-pm-perl libjson-perl  
# sqlite3 libdbd-sqlite3-perl libtext-diff-perl libtimedate-perl libmail-
imapclient-perl libgd-graph-perl  
# libtext-csv-perl libxml-simple-perl liblist-moreutils-perl ttf-liberation
libimage-librsvg-perl libgd-text-perl  
# libsocket6-perl libio-socket-inet6-perl libmime-base64-perl libimage-info-
perl libusb-1.0-0-dev libnet-server-perl  
# net-tools libsoap-lite-perl libjson-xs-perl  
## DB log, SVG, sound  
# libdbi-perl libdbd-mysql-perl libclass-dbi-mysql-perl mysql-client libdbd-
mysql libimage-librsvg-perl libav-tools  
## whatsapp Python yowsup  
# python-soappy python-dateutil python-dev libgmp10  
## whatsapp images  
# libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-
dev tcl8.5-dev tk8.5-dev python-tk  
## wiringpi and wiringpi2  
# wiringpi python-virtualenv  
  
FROM jsurf/rpi-raspbian  
  
MAINTAINER VCR  
  
RUN [ "cross-build-start" ]  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure tzdata \  
&& apt-get update \  
&& apt-get -y \--force-yes upgrade \  
&& apt-get -y \--force-yes install \  
apt-utils apt-transport-https bash dbus wget curl unzip python-pip \  
htop vim usbutils etherwake sudo xterm imagemagick snmp lsof avahi-daemon \  
supervisor cron openssh-server nfs-common autofs nodejs wiringpi \  
build-essential git make gcc g++ gcc-avr avr-libc dialog avrdude \  
  
perl-base libdevice-serialport-perl libwww-perl libio-socket-ssl-perl libcgi-
pm-perl libjson-perl \  
sqlite3 libdbd-sqlite3-perl libtext-diff-perl libtimedate-perl libmail-
imapclient-perl libgd-graph-perl \  
libtext-csv-perl libxml-simple-perl liblist-moreutils-perl ttf-liberation
libimage-librsvg-perl libgd-text-perl \  
libsocket6-perl libio-socket-inet6-perl libmime-base64-perl libimage-info-perl
libusb-1.0-0-dev libnet-server-perl \  
net-tools libsoap-lite-perl libjson-xs-perl \  
  
libdbi-perl libdbd-mysql-perl libclass-dbi-mysql-perl mysql-client libdbd-
mysql libimage-librsvg-perl libav-tools \  
  
python-soappy python-dateutil python-dev libgmp10 \  
libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev
tcl8.5-dev tk8.5-dev python-tk \  
  
&& echo "deb http://apt.pilight.org/ stable main" >
/etc/apt/sources.list.d/pilight.list \  
&& wget -O - http://apt.pilight.org/pilight.key | apt-key add \- \  
&& apt-get update \  
&& apt-get install pilight \  
  
&& pip install --upgrade pip \  
&& pip install python-axolotl --upgrade \  
&& pip install pillow --upgrade \  
&& pip install pyserial --upgrade \  
&& pip install wiringpi2 --upgrade \  
  
&& apt-get clean \  
&& apt-get autoremove \  
&& apt-get clean \  
  
&& echo "/net /etc/auto.net --timeout=60" >> /etc/auto.master \  
  
&& sed -i 's/Port 22/Port 2222/g' /etc/ssh/sshd_config \  
&& sed -i 's/PermitRootLogin no/PermitRootLogin yes/g' /etc/ssh/sshd_config \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config \  
&& echo "root:fhem!" | chpasswd \  
&& /bin/rm /etc/ssh/ssh_host_*  
  
WORKDIR /opt  
  
# install yowsup-client  
RUN wget -N https://github.com/tgalal/yowsup/archive/master.zip \  
&& unzip -o master.zip \  
&& rm master.zip \  
&& wget https://github.com/tgalal/python-axolotl/archive/master.zip \  
&& unzip master.zip \  
&& rm master.zip \  
&& cd python-axolotl-master \  
&& python setup.py install \  
&& pip install yowsup2 --upgrade  
  
# install RCswitch  
RUN git clone https://github.com/r10r/rcswitch-pi.git \  
&& cd rcswitch-pi \  
&& make  
  
# MySensors Gateway  
RUN git clone https://github.com/mysensors/MySensors.git --branch master \  
&& cd MySensors \  
&& ./configure --soc=BCM2835 --my-transport=nrf24 --my-gateway=ethernet --my-
port=5003 \--my-rf24-irq-pin=15 \  
&& make  
  
# install fhem (debian paket)  
RUN wget https://fhem.de/fhem-5.8.deb \  
&& dpkg -i fhem-*.deb \  
&& rm fhem-*.deb \  
&& echo 'fhem ALL = NOPASSWD:ALL' >>/etc/sudoers \  
&& mkdir fhem/config \  
&& echo 'attr global pidfilename /var/run/fhem/fhem.pid' >> fhem/fhem.cfg \  
&& echo 'attr global nofork 1' >> fhem/fhem.cfg \  
&& mv fhem/fhem.cfg fhem/fhem.cfg.org \  
&& mv /etc/pilight/config.json /etc/pilight/config.json.org  
  
ENV RUNVAR fhem  
WORKDIR /root  
  
# SSH / Fhem ports  
EXPOSE 2222 7072 8083 8084 8085 8086 9001  
  
ADD run.sh /root/  
ADD runfhem.sh /root/  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENTRYPOINT ["./run.sh"]  
#CMD ["arg1"]  
  
VOLUME /opt/fhem/config  
  
RUN [ "cross-build-end" ]  
# End Dockerfile

