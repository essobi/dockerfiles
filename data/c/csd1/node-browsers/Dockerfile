FROM node:8  
  
RUN groupadd ci \  
&& useradd \--gid ci \--shell /bin/bash \--create-home ci \  
&& mkdir /home/ci/src \  
&& chown -R ci:ci /home/ci/src  
  
RUN export FIREFOX_VERSION=$(curl -s
"https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" |
sed -n '/<a href="/{s|.*/firefox-\\(.*\\)\.tar.*|\1|p;q;}') \  
&& apt-get update -qy \  
&& apt-get -qy install apt-transport-https \  
&& curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list \  
&& apt-get update -qy \  
&& apt-get -qy \--no-install-recommends install firefox-esr google-chrome-
stable \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget \--no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox-esr \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
USER ci  
WORKDIR /home/ci/src  
  
ENV HOME=/home/ci  
RUN mkdir "${HOME}/.npm-packages" \  
&& echo "prefix=${HOME}/.npm-packages" > ~/.npmrc  
  
ENV NPM_PACKAGES="${HOME}/.npm-packages"  
ENV PATH="$NPM_PACKAGES/bin:$PATH"  

