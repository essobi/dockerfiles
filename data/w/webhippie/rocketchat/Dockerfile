FROM webhippie/ubuntu:xenial  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/var/lib/rocketchat"]  
  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
EXPOSE 3000  
WORKDIR /srv/www  
  
ENV ROCKETCHAT_VERSION 0.63.3  
ENV ROCKETCHAT_TARBALL https://cdn-
download.rocket.chat/build/rocket.chat-${ROCKETCHAT_VERSION}.tgz  
  
RUN apt-get update -y && \  
mkdir -p \  
/srv/www && \  
groupadd \  
-g 1000 \  
rocketchat && \  
useradd \  
-u 1000 \  
-d /srv/www \  
-g rocketchat \  
-s /bin/bash \  
-M \  
rocketchat && \  
apt-get install -y \  
python-minimal \  
build-essential \  
git && \  
rm -rf \  
/var/lib/apt/lists/*  
  
RUN curl -sLo /tmp/nodejs.deb
https://deb.nodesource.com/node_8.x/pool/main/n/nodejs/nodejs_8.9.4-1nodesource1_amd64.deb
&& \  
dpkg -i /tmp/nodejs.deb && \  
rm /tmp/nodejs.deb  
  
RUN curl -sLo - ${ROCKETCHAT_TARBALL} | tar -xzf - --strip 0 -C /srv/www && \  
chown -R rocketchat:rocketchat /srv/www && \  
cd /srv/www/bundle/programs/server && \  
npm install  
  
ADD rootfs /  

