FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
ENV SCREEN_WIDTH 1600  
ENV SCREEN_HEIGHT 1200  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
# Fixes https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n"
>> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu xenial-security main
universe\n" >> /etc/apt/sources.list  
  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install bzip2 ca-certificates
openjdk-8-jre-headless sudo unzip wget xvfb \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
#============================  
# Selenium server standalone  
#============================  
RUN mkdir -p /opt/selenium \  
&& wget --no-verbose https://github.com/groupon/Selenium-Grid-
Extras/releases/download/v1.12.9/SeleniumGridExtras-1.12.9-SNAPSHOT-jar-with-
dependencies.jar -O /opt/selenium/selenium-server-standalone.jar  
  
#===================  
# Timezone settings  
#===================  
ENV TZ "Europe/Tallinn"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
#============================================  
# Google Chrome  
#============================================  
# can specify versions by CHROME_VERSION;  
# e.g. google-chrome-stable=53.0.2785.101-1  
# google-chrome-beta=53.0.2785.92-1  
# google-chrome-unstable=54.0.2840.14-1  
# latest (equivalent to google-chrome-stable)  
# google-chrome-beta (pull latest beta)  
#============================================  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#==================  
# Chrome webdriver  
#==================  
ARG CHROME_DRIVER_VERSION=2.25  
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver
/opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \  
&& ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION
/usr/bin/chromedriver  
  
#=================================  
# Chrome Launch Script Modication  
#=================================  
COPY chrome_launcher.sh /opt/google/chrome/google-chrome  
RUN chmod +x /opt/google/chrome/google-chrome  
  
#====================================  
# Scripts to run Selenium Standalone  
#====================================  
COPY entry_point.sh functions.sh /opt/bin/  
RUN chmod +x /opt/bin/entry_point.sh  
ADD hub_4444.json /opt/selenium/hub_4444.json  
ADD node_5555.json /opt/selenium/node_5555.json  
ADD selenium_grid_extras_config.json
/opt/selenium/selenium_grid_extras_config.json  
  
EXPOSE 4444 5555 3000  
WORKDIR "/opt/selenium"  
CMD "/opt/bin/entry_point.sh"  

