FROM selenium/standalone-firefox:2.53.1-beryllium  
  
ENV FIREFOX_PROFILE_URL
https://testimstatic.blob.core.windows.net/extension/testim-firefox-
profile.zip  
ENV FIREFOX_PROFILE_ZIP_LOC /opt/testim-firefox-profile.zip  
ENV FIREFOX_PROFILE_LOC /opt/testim-firefox-profile  
  
USER root  
  
#===========================================  
# Replace selenium jar file (temp solution)  
#===========================================  
ENV GRID_JAR_VERSION 2.53.2  
  
RUN rm /opt/selenium/selenium-server-standalone.jar \  
&& wget --no-verbose -O /opt/selenium/selenium-server-standalone.jar
https://testimstatic.blob.core.windows.net/staging/selenium-server-
standalone-$GRID_JAR_VERSION.jar  
  
#=========  
# Firefox  
#=========  
ENV FIREFOX_VERSION 48.0b1  
ENV GECKO_DRIVER_VERSION 0.8.0  
  
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
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox \  
&& rm -rf /opt/geckodriver* \  
&& wget --no-verbose -O /tmp/geckodriver.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-
linux64.gz \  
&& gunzip -c /tmp/geckodriver.gz > /opt/geckodriver-$GECKO_DRIVER_VERSION \  
&& chmod +x /opt/geckodriver-$GECKO_DRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKO_DRIVER_VERSION /usr/bin/wires \  
&& rm -rf /tmp/geckodriver*  
  
  
#=================  
# Testim Headless  
#=================  
RUN apt-get update -qqy \  
&& apt-get -qqy install curl \  
&& wget --no-verbose -O $FIREFOX_PROFILE_ZIP_LOC $FIREFOX_PROFILE_URL \  
&& unzip $FIREFOX_PROFILE_ZIP_LOC -d $FIREFOX_PROFILE_LOC \  
&& echo $(curl -sI -X HEAD "${FIREFOX_PROFILE_URL}" | tr -d '\r' | sed -En
's/^ETag: (.*)/\1/p') > /opt/testim-headless-info \  
&& rm -rf /var/lib/apt/lists/* \  
&& chown -R seluser:seluser $FIREFOX_PROFILE_LOC \  
&& chmod -R 777 /opt  
  
USER seluser  

