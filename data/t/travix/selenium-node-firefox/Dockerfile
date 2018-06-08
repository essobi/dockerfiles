FROM selenium/node-base:3.6.0-copper  
  
MAINTAINER Travix  
  
USER root  
  
ENV FIREFOX_VERSION="54.0" \  
GECKODRIVER_VERSION="0.18.0" \  
NODE_MAX_INSTANCES="1" \  
NODE_MAX_SESSION="1" \  
NODE_REGISTER_CYCLE="5000" \  
NODE_PORT="5555"  
  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install dbus \  
&& dbus-uuidgen > /etc/machine-id \  
&& version=$(echo $FIREFOX_VERSION | awk '{split($0,a,"."); print a[1]}') \  
&& echo "deb http://ppa.launchpad.net/ubuntu-mozilla-daily/ppa/ubuntu xenial
main" >> /etc/apt/sources.list.d/mozilla.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
B34505EA326FEAEA07E3618DEF4186FE247510BE \  
&& apt-get update -qqy \  
&& apt-get install -qqy xul-ext-ubufox libasound2 libpulse-dev \  
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
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox \  
&& wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& rm -rf /opt/geckodriver \  
&& tar -C /opt -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \  
&& chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \  
&& ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver  
  
USER seluser  
COPY generate_config /opt/bin/generate_config  
  
RUN sudo echo "" \  
&& /opt/bin/generate_config > /opt/selenium/config.json  
  

