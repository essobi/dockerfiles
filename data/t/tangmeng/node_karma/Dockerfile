FROM ubuntu:14.04  
MAINTAINER 357003671@qq.com  
  
RUN apt-get update; \  
apt-get install -y git curl; \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -; \  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
- ; \  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'; \  
apt-get update && apt-get install -y google-chrome-stable nodejs Xvfb; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV FIREFOX_VERSION 45.0.2  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  
  
ADD xvfb.sh /etc/init.d/xvfb  
RUN chmod 777 /etc/init.d/xvfb  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 777 /entrypoint.sh  
ENV DISPLAY :99.0  
ENV CHROME_BIN /usr/bin/google-chrome  
ENV FIREFOX_BIN /usr/bin/firefox  
  
ENTRYPOINT ["/entrypoint.sh"]

