FROM python:3.6-stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends unzip wget curl unzip fontconfig
xvfb libgconf2-4 imagemagick && \  
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add
\- && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update && \  
apt-get -y install --no-install-recommends google-chrome-stable  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends python3-dev python3-pip python-
twisted libxml2-dev python-lxml python-requests nodejs && \  
rm -rf /var/lib/apt/lists/*  
RUN pip3 install pymongo urllib3 requests scrapy mpegdash m3u8 fake-useragent
twython mojimoji pillow slackweb lxml && \  
pip3 install git+https://github.com/yashaka/selene.git  
  
RUN wget
https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip && \  
unzip chromedriver_linux64.zip -d /usr/bin/  
  
WORKDIR /data  
VOLUME /data  
  
COPY IPAfont00303.zip /data/IPAfont00303.zip  
  
RUN unzip IPAfont00303.zip -d /usr/share/fonts/ && \  
fc-cache -fv  
  
  
  
  
  
  
  

