FROM debian  
MAINTAINER Piotr Gaczkowski <DoomHammerNG@gmail.com>  
  
ADD http://debian.pengutronix.de/debian/pengutronix.list
/etc/apt/sources.list.d/  
  
RUN apt-get update && \  
apt-get install -qqy --force-yes \  
oselas.toolchain-2014.12.1-arm-cortexa8-linux-gnueabihf-
gcc-4.9.2-glibc-2.20-binutils-2.24-kernel-3.16-sanitized && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /opt/OSELAS.Toolchain-2014.12.1  
  
ENTRYPOINT /usr/bin/tail -f /dev/null  

