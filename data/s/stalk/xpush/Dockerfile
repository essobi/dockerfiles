#  
# XPush standalone (single) Dockerfile  
#  
# https://github.com/xpush/dockerfile/xpush/single  
#  
FROM centos:centos6  
  
# Install packages  
RUN \  
yum -y install wget && \  
yum -y install tar && \  
yum -y install gcc && \  
yum -y install xz && \  
yum -y install git && \  
yum -y install gcc-c++  
  
# Install node.js  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 4.5.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
RUN \  
mkdir -p /var/logs/xpush  
  
# Install node-gyp  
RUN export USER=root && npm install -g node-gyp  
  
# Install XPUSH Servers  
RUN export USER=root && mkdir -p /data && npm install -g xpush forever  
  
# Make xpush-session.sh  
RUN \  
printf "\  
cd /usr/local/lib/node_modules/xpush && \n\  
forever start -al /var/logs/xpush/session.log ./bin/start --config
/data/session.json --port 8000 --home /data --session \n\  
echo -ne \"\\\\\nTailing log\"\n\  
sleep 5\n\  
tail -f /var/logs/xpush/session.log" > /usr/bin/xpush-session.sh  
  
# Make xpush-channel.sh  
RUN \  
printf "\  
mkdir -p /var/logs/xpush && \n\  
cd /usr/local/lib/node_modules/xpush && \n\  
forever start -al /var/logs/xpush/channel.log ./bin/start --config
/data/channel.json --port 9000 --home /data\n\  
echo -ne \"\\\\\nTailing log\"\n\  
sleep 5\n\  
tail -f /var/logs/xpush/channel.log" > /usr/bin/xpush-channel.sh  
  
RUN chmod 775 /usr/bin/xpush-*.sh  
  
# Expose ports.  
# - 8000 : xpush session server  
# - 9000 : xpush channel server  
EXPOSE 8000  
EXPOSE 9000

