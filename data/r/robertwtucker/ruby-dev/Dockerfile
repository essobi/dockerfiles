FROM ruby:2  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex &&\  
for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \  
gpg --keyserver hkp://keyserver.pgp.com:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_MAJOR_VERSION 6  
RUN NODE_VERSION=$(curl -SL "https://nodejs.org/dist/index.tab" \  
| grep "v${NODE_MAJOR_VERSION}" \  
| head -n 1 | awk '{ print $1 }') \  
&& curl -SLO
"https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.gz"
\  
&& curl -SLO "https://nodejs.org/dist/${NODE_VERSION}/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-${NODE_VERSION}-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-${NODE_VERSION}-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-${NODE_VERSION}-linux-x64.tar.gz" SHASUMS256.txt.asc  

