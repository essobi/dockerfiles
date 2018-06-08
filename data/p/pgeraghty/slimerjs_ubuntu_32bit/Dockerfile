# SlimerJS  
# VERSION 1.0.0  
FROM intersoftlab/ubuntu:14.04-i386  
  
MAINTAINER pgeraghty  
  
# Env  
ENV SLIMERJS_VERSION_F 0.9.3  
# Commands  
RUN \  
echo "deb http://archive.canonical.com/ubuntu trusty partner" >
/etc/apt/sources.list.d/partner.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim git wget xvfb libxrender-dev libasound2:i386 libdbus-
glib-1-2 libgtk2.0-0 bzip2 && \  
mkdir -p /srv/var && \  
wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-i686.tar.bz2
http://download.slimerjs.org/releases/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F-
linux-i686.tar.bz2 && \  
tar -xjf /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-i686.tar.bz2 -C /tmp && \  
rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-i686.tar.bz2 && \  
mv /tmp/slimerjs-$SLIMERJS_VERSION_F/ /srv/var/slimerjs && \  
  
ln -s /srv/var/slimerjs/slimerjs /usr/bin/slimerjs && \  
  
apt-get autoremove -y && \  
apt-get clean all  
  
# Default command  
ENTRYPOINT ["slimerjs"]  
CMD ["--help"]  

