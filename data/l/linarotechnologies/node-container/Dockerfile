FROM bitnami/minideb  
  
LABEL description="nodejs container based on bitnami/minideb:jessie"  
LABEL "com.linarotechnologies.version"="1.0"  
LABEL "com.linarotechnologies.production"="1"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV DISABLE_WELCOME_MESSAGE 1  
ENV NAMI_DEBUG 1  
ENV DISABLE_LAUNCH_TRACKING 1  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.11.3  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# Node release team GPG keys  
# https://github.com/nodejs/node#release-team  
RUN install_packages gnupg dirmngr \  
&& set -ex \  
&& for key in \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
RUN install_packages \  
ca-certificates \  
curl \  
git \  
tar \  
xz-utils \  
libc6 \  
libssl1.1 \  
zlib1g \  
libbz2-1.0 \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
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
  
# Update npm to the latest version and move the node_modules/ dir in  
# place. Should prevent weird errors when running 'npm install' afterwards.  
RUN cd / \  
&& npm install npm \  
&& rm -rf /usr/local/lib/node_modules/ \  
&& mv node_modules/ /usr/local/lib/  
  
USER node  
CMD ["node"]  

