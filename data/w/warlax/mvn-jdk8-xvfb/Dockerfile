FROM maven:3.3-jdk-8  
RUN apt-get -y update && apt-get -y install xvfb  
  
# Install Google Chrome:  
RUN apt-get -y install libxpm4 libxrender1 libgtk2.0-0 libnss3 libgconf-2-4  
#RUN apt-get -y install chromium  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
RUN apt-get update  
RUN apt-get install -y chromium  
  
# Dependencies to make "headless" chrome/selenium work:  
RUN apt-get -y install xvfb gtk2-engines-pixbuf  
RUN apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base
xfonts-scalable  
  
# Optional but nifty: For capturing screenshots of Xvfb display:  
RUN apt-get -y install imagemagick x11-apps  
  
## Install node (Code taken from official docker-node/6.7/Dockerfile  
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
ENV NODE_VERSION 6.7.0  
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
  
CMD [ "node" ]  
  
## Fill up the maven and node caches with some data, just to speed up builds
that little bit  
RUN mkdir /tmp/fake_build  
COPY pom.xml /tmp/fake_build/pom.xml  
COPY package.json /tmp/fake_build/package.json  
COPY bower.json /tmp/fake_build/bower.json  
  
RUN cd /tmp/fake_build && mvn dependency:go-offline  
RUN cd /tmp/fake_build && npm install  
RUN cd /tmp/fake_build && node node_modules/bower/bin/bower --allow-root
install  
  
# Set up hosts file  
RUN echo 127.0.0.1 spectrumlocal.com >> /etc/hosts  
RUN echo 127.0.0.1 internal.localspectrum.com >> /etc/hosts  
  

