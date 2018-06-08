# CasperJS using SlimerJS  
  
# VERSION 1.0.0  
  
FROM daald/ubuntu32:trusty  
  
ENV SLIMERJS_VERSION_F 0.9.5  
  
# Configure locales  
RUN locale-gen en_US.UTF-8  
  
# Set default locale for the environment  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim git wget unzip xvfb libxrender-dev libasound2:i386
libdbus-glib-1-2 libgtk2.0-0 bzip2 python && \  
mkdir -p /srv/var && \  
wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-i686.tar.bz2
http://download.slimerjs.org/releases/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F-
linux-i686.tar.bz2 && \  
tar -xjf /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-i686.tar.bz2 -C /tmp && \  
rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-i686.tar.bz2 && \  
mv /tmp/slimerjs-$SLIMERJS_VERSION_F/ /srv/var/slimerjs && \  
# echo '#!/bin/bash\nxvfb-run /srv/var/slimerjs/slimerjs $*' >
/srv/var/slimerjs/slimerjs.sh && \  
# chmod 755 /srv/var/slimerjs/slimerjs.sh && \  
ln -s /srv/var/slimerjs/slimerjs /usr/bin/slimerjs && \  
  
wget -O /tmp/casperjs-1.1-beta3
https://github.com/n1k0/casperjs/zipball/1.1-beta3 && \  
unzip /tmp/casperjs-1.1-beta3 -d /tmp && \  
rm -f /tmp/casperjs-1.1-beta3 && \  
mv /tmp/n1k0-casperjs-4f105a9/ /srv/var/casperjs && \  
  
# git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
# echo '#!/bin/bash\n/srv/var/casperjs/bin/casperjs --engine=slimerjs $*' >>
/srv/var/casperjs/casperjs.sh && \  
# chmod 755 /srv/var/casperjs/casperjs.sh && \  
  
ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  
# Default command  
ENTRYPOINT ["casperjs", "--engine=slimerjs"]  
CMD ["--help"]  

