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
apt-get install -y ca-certificates curl python build-essential git-core && \  
rm -rf /var/lib/apt/lists/*  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.31/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
ENV NODE_VERSION 4.4.7  
ENV NPM_VERSION 2.7.3  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g npm@3.10.3 \  
&& npm install -g strongloop \  
&& npm cache clear  
  
WORKDIR /work  
CMD [ "npm start" ]  

