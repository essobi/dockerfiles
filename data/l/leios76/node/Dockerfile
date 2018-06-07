# Pull base image.  
FROM ubuntu:14.04  
RUN locale-gen ko_KR.UTF-8  
RUN update-locale LANG=ko_KR.UTF-8  
RUN dpkg-reconfigure locales  
  
ENV LANG ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
# Install curl  
RUN \  
sed -ri 's/\/archive\\.ubuntu\\.com/\/kr\\.archive\\.ubuntu\\.com/g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y git-core ca-certificates curl python build-essential && \  
rm -rf /var/lib/apt/lists/*  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.31/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
#RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
RUN \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
FD3A5288F042B6850C66B31F09FE44734EB7990E && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
DD8F2338BAE7501E3DD5AC78C273792F7D83545D && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
B9AE9905FFD7803F25714661B63B535A4C206CA9 && \  
gpg --keyserver pool.sks-keyservers.net --recv-keys
56730D5401028683275BD23C23EFEFE93C4CFFFE  
  
ENV NODE_VERSION 6.11.4  
#ENV NPM_VERSION 2.7.3  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
#RUN npm install -g npm@"$NPM_VERSION" && npm cache clear  
CMD [ "node" ]  

