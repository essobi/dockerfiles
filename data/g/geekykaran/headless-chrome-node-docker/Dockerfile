FROM debian:stable-slim  
  
# Install basic tools/utilities and google Chrome unstable (which has cross
platform support for headless mode). Combining theem together so that apt
cache cleanup would need to be done just once.  
RUN apt-get update -y && \  
apt-get install ca-certificates \  
gconf-service \  
libasound2 \  
libatk1.0-0 \  
libatk1.0-0 \  
libdbus-1-3 \  
libgconf-2-4 \  
libgtk-3-0 \  
libnspr4 \  
libnss3 \  
libx11-xcb1 \  
libxss1 \  
libxtst6 \  
fonts-liberation \  
libappindicator1 \  
xdg-utils \  
lsb-release \  
wget \  
curl \  
xz-utils -y --no-install-recommends && \  
wget https://dl.google.com/linux/direct/google-chrome-
unstable_current_amd64.deb && \  
dpkg -i google-chrome*.deb && \  
apt-get install -f && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* google-chrome-
unstable_current_amd64.deb  
  
# Install nodejs  
ENV NPM_CONFIG_LOGLEVEL=info NODE_VERSION=8.4.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Install yarn  
ENV YARN_VERSION 0.27.5  
RUN curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz  

