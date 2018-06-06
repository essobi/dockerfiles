  
FROM selenium/node-base:3.5.3-boron  
LABEL authors=SeleniumHQ  
  
USER root  
  
ARG FIREFOX_VERSION=55.0.3  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
  
COPY generate_config /opt/bin/generate_config  
COPY google-chrome-base /opt/google/chrome/google-chrome-base  
COPY chrome_launcher.sh /opt/google/chrome/google-chrome  
  
RUN chmod +x /opt/google/chrome/google-chrome && \  
chmod +x /opt/bin/generate_config && \  
chmod +x /opt/google/chrome/google-chrome-base  
  
  
  
  
  
  
  
  
  
  

