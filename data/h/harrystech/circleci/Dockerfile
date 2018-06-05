FROM circleci/ruby:2.5.1  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y \  
libqt5webkit5-dev\  
qt5-default\  
postgresql-client\  
lsof \  
libasound2 \  
libgtk-3-0 \  
libstartup-notification0 \  
gconf-service \  
libgconf-2-4 \  
libnspr4 \  
libxss1 \  
fonts-liberation \  
libappindicator1 \  
libnss3 \  
xdg-utils  
  
USER root  
  
############ BEGIN NODE DOCKERFILE ####################  
# COPY-PASTED FROM NODE 8 INSTALLATION FROM
https://raw.githubusercontent.com/nodejs/docker-node/master/8/Dockerfile  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 \--gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NODE_VERSION 8.9.1  
  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
i386) ARCH='x86';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-
components=1 \--no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV YARN_VERSION 1.3.2  
  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
################ END NODE DOCKERFILE ################  
  
################ BEGIN BROWSERS #####################  
  
# Install geckodriver  
RUN \  
url=https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
\  
&& curl -s -L "$url" | tar -xz \  
&& chmod +x geckodriver \  
&& mv geckodriver /usr/local/bin  
  
  
########  
# install firefox  
ENV PATH /firefox:$PATH  
RUN FIREFOX_URL="https://download-
installer.cdn.mozilla.net/pub/firefox/releases/57.0/linux-x86_64/en-
US/firefox-57.0.tar.bz2" \  
FIREFOX_SHA256="c2cae016089e816c03283a359c582efab3bca34e6048ecc2382b43c1eb342457"
\  
&& curl --silent --show-error --location --fail --retry 3 \--output
/tmp/firefox.tar.bz2 $FIREFOX_URL \  
&& echo "$FIREFOX_SHA256 /tmp/firefox.tar.bz2" | sha256sum -c \  
&& tar -jxf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& firefox --version  
  
# install chrome  
RUN curl --silent --show-error --location --fail --retry 3 \--output
/tmp/google-chrome-stable_current_amd64.deb
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \  
&& (dpkg -i /tmp/google-chrome-stable_current_amd64.deb || apt-get -fy
install) \  
&& rm -rf /tmp/google-chrome-stable_current_amd64.deb \  
&& sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-
sandbox|g' \  
"/opt/google/chrome/google-chrome" \  
&& google-chrome --version  
  
# Install ChromeDriver  
RUN export CHROMEDRIVER_RELEASE=$(curl --location --fail --retry 3
http://chromedriver.storage.googleapis.com/LATEST_RELEASE) \  
&& curl --silent --show-error --location --fail --retry 3 \--output
/tmp/chromedriver_linux64.zip
"http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_RELEASE/chromedriver_linux64.zip"
\  
&& cd /tmp \  
&& unzip chromedriver_linux64.zip \  
&& rm -rf chromedriver_linux64.zip \  
&& mv chromedriver /usr/local/bin/chromedriver \  
&& chmod +x /usr/local/bin/chromedriver \  
&& chromedriver --version  
  
################## END BROWSERS #####################  
  
# Set DISPLAY for xvfb (for Firefox).  
# Note: need to start this manually in Circle.  
ENV DISPLAY :99  
  
USER circleci  
  

