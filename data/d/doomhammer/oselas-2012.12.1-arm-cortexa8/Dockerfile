FROM debian  
MAINTAINER Piotr Gaczkowski <DoomHammerNG@gmail.com>  
  
ADD http://debian.pengutronix.de/debian/pengutronix.list
/etc/apt/sources.list.d/  
  
RUN apt-get update && \  
apt-get install -qqy --force-yes \  
oselas.toolchain-2012.12.1-arm-cortexa8-linux-gnueabihf-
gcc-4.7.3-glibc-2.16.0-binutils-2.22-kernel-3.6-sanitized && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /opt/OSELAS.Toolchain-2012.12.1  
  
ENTRYPOINT /usr/bin/tail -f /dev/null  

