FROM phusion/baseimage:0.9.19  
#Prerequisites  
RUN apt-get update && apt-get upgrade -y; \  
apt-get install -y apt-utils ca-certificates git npm  
  
#Setup Node - Taken from node docker image v6  
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
ENV NODE_VERSION 6.3.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
########################  
#Setup gekko  
RUN mkdir -p /usr/src/gekko  
WORKDIR /usr/src/gekko  
  
#Download & setup Gekko trading bot  
RUN git clone -b stable https://github.com/askmike/gekko.git .; \  
npm install; \  
npm install  
  
#Setup auto start service  
COPY build/service_start_gekko.sh /service_start_gekko.sh  
RUN ls /;  
RUN mkdir -p /etc/service/gekko; ln -s /service_start_gekko.sh
/etc/service/gekko/run; \  
chmod 750 /service_start_gekko.sh  
########################  
#Enable plugins  
RUN npm install redis@0.10.0 talib@1.0.2 pg  
  
VOLUME /usr/src/gekko/history  
  
CMD ["/sbin/my_init"]  

