FROM ubuntu:16.04  
  
MAINTAINER Alan Bondarchuk <imacoda@gmail.com>  
  
# Env  
ENV SLIMERJS_VERSION_F 0.10.1  
ENV CASPERJS_VERSION_F 1.1.3  
ENV FIREFOX_VERSION_F 49.0.2  
# Commands  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y unzip git wget xvfb libxrender-dev libasound2 libdbus-
glib-1-2 libgtk-3-0 bzip2 python && \  
mkdir -p /srv/var && \  
# Firefox  
wget -O /tmp/firefox-mozilla-build_$FIREFOX_VERSION_F-0ubuntu1_amd64.deb
http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt/pool/main/f/firefox-
mozilla-build/firefox-mozilla-build_$FIREFOX_VERSION_F-0ubuntu1_amd64.deb && \  
cd /tmp && \  
dpkg -i firefox-mozilla-build_$FIREFOX_VERSION_F-0ubuntu1_amd64.deb && \  
rm firefox-mozilla-build_$FIREFOX_VERSION_F-0ubuntu1_amd64.deb && \  
# SlimerJS  
wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F.zip
http://download.slimerjs.org/releases/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F.zip
&& \  
unzip /tmp/slimerjs-$SLIMERJS_VERSION_F.zip -d /tmp && \  
rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F.zip && \  
mv /tmp/slimerjs-$SLIMERJS_VERSION_F/ /srv/var/slimerjs && \  
echo -e '#!/bin/bash\nxvfb-run /srv/var/slimerjs/slimerjs "$@"' >
/srv/var/slimerjs/slimerjs.sh && \  
chmod 755 /srv/var/slimerjs/slimerjs.sh && \  
ln -s /srv/var/slimerjs/slimerjs.sh /usr/bin/slimerjs && \  
# CasperJS  
wget -O /tmp/casperjs-$CASPERJS_VERSION_F.zip
https://github.com/casperjs/casperjs/archive/$CASPERJS_VERSION_F.zip && \  
unzip /tmp/casperjs-$CASPERJS_VERSION_F.zip -d /tmp && \  
rm -f /tmp/casperjs-$CASPERJS_VERSION_F.zip && \  
mv /tmp/casperjs-$CASPERJS_VERSION_F/ /srv/var/casperjs && \  
echo -e '#!/bin/bash\n/srv/var/casperjs/bin/casperjs --engine=slimerjs "$@"'
>> /srv/var/casperjs/casperjs.sh && \  
chmod 755 /srv/var/casperjs/casperjs.sh && \  
ln -s /srv/var/casperjs/casperjs.sh /usr/bin/casperjs && \  
# Cleanup  
apt-get autoremove -y && \  
apt-get clean all  
  
# Default command  
CMD ["/usr/bin/slimerjs"]  

