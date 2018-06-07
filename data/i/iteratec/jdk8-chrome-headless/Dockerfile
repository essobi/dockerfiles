FROM openjdk:8-jdk  
MAINTAINER OSM Team <osm@iteratec.de>  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
xvfb  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ARG CHROME_DRIVER_VERSION=2.30  
  
RUN wget --no-verbose -O /tmp/chromedriver.zip
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& unzip /tmp/chromedriver.zip -d /usr/bin/ \  
&& chmod 755 /usr/bin/chromedriver \  
&& rm /tmp/chromedriver.zip \  
&& mkdir /data  
  
WORKDIR /data  

