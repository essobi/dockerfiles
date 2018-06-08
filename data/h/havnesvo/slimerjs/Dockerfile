# slimerjs  
# Fork of cmfatih/slimerjs  
# Usage  
# docker run havnesvo/slimerjs /usr/bin/slimerjs -v  
# docker run -v `pwd`:/scripts havnesvo/slimerjs /usr/bin/slimerjs
/scripts/test.js  
# docker run -v `pwd`:/scripts havnesvo/slimerjs /usr/bin/casperjs
/scripts/test-casperjs.js  
  
FROM ubuntu:14.04  
  
MAINTAINER havnesvo  
  
ENV SLIMERJS_VERSION_F 0.10.3  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y unzip git wget xvfb libxrender-dev libasound2 libdbus-
glib-1-2 libgtk2.0-0 bzip2 python && \  
mkdir -p /srv/var && \  
wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F.zip
http://download.slimerjs.org/releases/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F.zip
&& \  
unzip /tmp/slimerjs-$SLIMERJS_VERSION_F.zip -d /tmp && \  
rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F.zip && \  
mv /tmp/slimerjs-$SLIMERJS_VERSION_F/ /srv/var/slimerjs && \  
echo '#!/bin/bash\nxvfb-run /srv/var/slimerjs/slimerjs "$@"' >
/srv/var/slimerjs/slimerjs.sh && \  
chmod 755 /srv/var/slimerjs/slimerjs.sh && \  
ln -s /srv/var/slimerjs/slimerjs.sh /usr/bin/slimerjs && \  
git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
echo '#!/bin/bash\n/srv/var/casperjs/bin/casperjs --engine=slimerjs "$@"' >>
/srv/var/casperjs/casperjs.sh && \  
chmod 755 /srv/var/casperjs/casperjs.sh && \  
ln -s /srv/var/casperjs/casperjs.sh /usr/bin/casperjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  
ENV FIREFOX_VERSION=52.0.1  
RUN FIREFOX_DOWNLOAD_URL=$(if [ $FIREFOX_VERSION = "nightly" ]; then echo
"https://download.mozilla.org/?product=firefox-nightly-latest-
ssl&os=linux64&lang=en-US"; else echo "https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2"; fi) \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 $FIREFOX_DOWNLOAD_URL \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
# Default command  
CMD ["/usr/bin/slimerjs"]  

