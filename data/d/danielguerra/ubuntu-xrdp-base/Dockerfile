FROM ubuntu:16.04  
MAINTAINER Daniel Guerra  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed -i "s/# deb-src/deb-src/g" /etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -yy upgrade  
ENV BUILD_DEPS="git autoconf pkg-config libssl-dev libpam0g-dev \  
libx11-dev libxfixes-dev libxrandr-dev nasm xsltproc flex \  
bison libxml2-dev dpkg-dev libcap-dev xserver-xorg-dev"  
RUN apt-get -yy install \  
sudo apt-utils software-properties-common vim wget ca-certificates \  
xauth supervisor uuid-runtime pulseaudio locales xserver-xorg \  
$BUILD_DEPS  
  
  
# Build xrdp  
WORKDIR /tmp  
RUN apt-get source pulseaudio  
RUN apt-get build-dep -yy pulseaudio  
WORKDIR /tmp/pulseaudio-8.0  
RUN dpkg-buildpackage -rfakeroot -uc -b  
WORKDIR /tmp  
RUN git clone \--branch v0.9.4 --recursive
https://github.com/neutrinolabs/xrdp.git  
WORKDIR /tmp/xrdp  
RUN ./bootstrap  
RUN ./configure  
RUN make  
RUN make install  
WORKDIR /tmp/xrdp/sesman/chansrv/pulse  
RUN sed -i "s/\/tmp\/pulseaudio\\-10\\.0/\/tmp\/pulseaudio\\-8\\.0/g" Makefile  
RUN make  
RUN cp *.so /usr/lib/pulse-8.0/modules/  
  
# Build xorgxrdp  
WORKDIR /tmp  
RUN git clone \--branch v0.2.4 --recursive
https://github.com/neutrinolabs/xorgxrdp.git  
WORKDIR /tmp/xorgxrdp  
RUN ./bootstrap  
RUN ./configure  
RUN make  
RUN make install  
  
# Clean  
WORKDIR /  
RUN apt-get -yy remove xscreensaver  
RUN apt-get -yy remove $BULD_DEPS  
RUN apt-get -yy autoremove  
RUN apt-get -yy clean  
RUN rm -rf /tmp/*  
  
# Configure  
ADD etc /etc  
ADD bin /usr/bin  
RUN mkdir /var/run/dbus  
RUN cp /etc/X11/xrdp/xorg.conf /etc/X11  
RUN sed -i "s/xrdp\/xorg/xorg/g" /etc/xrdp/sesman.ini  
RUN locale-gen en_US.UTF-8  
  
# Clean preconfigured stuff  
RUN rm -rf /etc/xrdp/rsakeys.ini /etc/xrdp/rsakeys.ini /etc/xrdp/*.pem  
  
# Docker config  
VOLUME ["/etc","/home"]  
EXPOSE 3389 9001  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
CMD ["supervisord"]

