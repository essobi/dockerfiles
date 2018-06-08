FROM enonic/java8  
  
MAINTAINER Jørgen Sivesind <jsi@enonic.com>  
  
USER root  
  
# Setup  
RUN mkdir /data  
VOLUME /data  
ENV HOME=/data  
  
# Tools  
RUN apt-get update \  
&& apt-get install -y curl zip \  
&& apt-get install -y curl unzip  
  
# NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# Firefox  
ARG FIREFOX_VERSION=57.0.4  
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
  
# Geckodriver  
ARG GECKODRIVER_VERSION=0.19.1  
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& rm -rf /opt/geckodriver \  
&& tar -C /opt -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \  
&& chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver  

