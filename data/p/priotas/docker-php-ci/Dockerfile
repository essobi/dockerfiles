FROM priotas/docker-php  
  
ENV FIREFOX_VERSION=35.0.1  
  
RUN requirements="default-jre wget" \  
&& apt-get -qqy update \  
&& apt-get -qqy --no-install-recommends install $requirements \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox \  
&& apt-get purge --auto-remove -y  
  
RUN yarn global add selenium-standalone@5  
RUN yarn global add forever  
RUN selenium-standalone install  

