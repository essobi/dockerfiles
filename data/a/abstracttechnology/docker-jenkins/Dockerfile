FROM jenkins:latest  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NODE_VERSION 4.2.2  
ENV SLIMERJS_VERSION_F 0.9.6  
  
  
RUN apt-get update && \  
apt-get install -y build-essential libssl-dev python-dev libffi-dev \  
git wget xvfb libxrender-dev libasound2 libdbus-glib-1-2 \  
libgtk2.0-0 bzip2 docker.io && \  
mkdir -p /srv/var && \  
wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2
http://download.slimerjs.org/releases/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 && \  
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
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
ADD https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz /node.tar.gz  
  
RUN tar -xzf node.tar.gz --strip-components=1 -C /  
  
USER jenkins  

