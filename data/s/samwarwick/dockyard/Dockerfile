FROM node:8  
  
MAINTAINER Sam Warwick <sam@samwarwick.com>  
  
RUN apt-get update  
RUN apt-get --yes --force-yes install unzip  
  
# Xvfb  
RUN apt-get update -qqy \  
&& apt-get -qqy install xvfb \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# Google Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& sed -i 's/"$HERE\/chrome"/xvfb-run "$HERE\/chrome" --no-sandbox/g'
/opt/google/chrome/google-chrome  
  
# Chrome driver  
RUN wget -O /tmp/chromedriver-version
http://chromedriver.storage.googleapis.com/LATEST_RELEASE && \  
wget http://chromedriver.storage.googleapis.com/`cat /tmp/chromedriver-
version`/chromedriver_linux64.zip && \  
unzip chromedriver_linux64.zip -d /usr/bin && \  
rm /tmp/chromedriver-version chromedriver_linux64.zip && \  
chmod 777 /usr/bin/chromedriver  

