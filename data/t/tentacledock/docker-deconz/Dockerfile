FROM ubuntu:xenial  
MAINTAINER appserv.nl  
  
EXPOSE 3389  
EXPOSE 8080  
ENV DECONZ_MAJOR_VERSION 2  
ENV DECONZ_MINOR_VERSION 04  
ENV DECONZ_BUILD_VERSION 82  
VOLUME ["/root/.local/share/dresden-elektronik/deCONZ"]  
  
ADD start.sh /  
  
RUN usermod -a -G dialout root \  
# && echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
# && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
git \  
vim.tiny \  
wget \  
sudo \  
net-tools \  
ca-certificates \  
unzip \  
apt-transport-https \  
qt5-default \  
libqt5sql5 \  
libqt5websockets5-dev \  
libqt5serialport5-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& chmod +x ./start.sh  
  
RUN wget https://www.dresden-
elektronik.de/deconz/ubuntu/beta/deconz-${DECONZ_MAJOR_VERSION}.${DECONZ_MINOR_VERSION}.${DECONZ_BUILD_VERSION}-qt5.deb
\  
&& wget https://www.dresden-elektronik.de/deconz/ubuntu/beta/deconz-
dev-${DECONZ_MAJOR_VERSION}.${DECONZ_MINOR_VERSION}.${DECONZ_BUILD_VERSION}.deb
\  
&& dpkg -i
deconz-${DECONZ_MAJOR_VERSION}.${DECONZ_MINOR_VERSION}.${DECONZ_BUILD_VERSION}-qt5.deb
\  
&& dpkg -i deconz-
dev-${DECONZ_MAJOR_VERSION}.${DECONZ_MINOR_VERSION}.${DECONZ_BUILD_VERSION}.deb
\  
&& git clone https://github.com/dresden-elektronik/deconz-rest-plugin.git \  
&& cd deconz-rest-plugin \  
&& git checkout -b mybranch
V${DECONZ_MAJOR_VERSION}_${DECONZ_MINOR_VERSION}_${DECONZ_BUILD_VERSION} \  
&& qmake \  
&& make -j2 \  
&& cp ../libde_rest_plugin.so /usr/share/deCONZ/plugins  
  
#CMD ["/usr/bin/deCONZ", "--http-port=80", "-platform", "minimal", "--dbg-
info=3"]  
CMD ["./start.sh"]  
#ENTRYPOINT ["/sbin/entrypoint.sh"]  

