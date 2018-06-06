FROM selenium/node-chrome:2.53.1-beryllium  
  
ENV EXT_HEADLESS_URL
https://testimstatic.blob.core.windows.net/extension/testim-headless.zip  
ENV EXT_HEADLESS_ZIP_LOC /opt/testim-headless.zip  
ENV EXT_HEADLESS_LOC /opt/testim-headless  
  
USER root  
  
RUN apt-get update -qqy \  
&& apt-get -qqy install curl \  
&& wget --no-verbose -O $EXT_HEADLESS_ZIP_LOC $EXT_HEADLESS_URL \  
&& unzip $EXT_HEADLESS_ZIP_LOC -d $EXT_HEADLESS_LOC \  
&& echo $(curl -sI -X HEAD "${EXT_HEADLESS_URL}" | tr -d '\r' | sed -En
's/^ETag: (.*)/\1/p') > /opt/testim-headless-info \  
&& rm -rf /var/lib/apt/lists/*  
  
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
&& apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} ttf-unfonts-
core ttf-unfonts-extra fonts-takao-mincho fonts-arphic-ukai \  
&& apt-get install --only-upgrade libnss3 -qqy \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#=================================  
# Chrome Launch Script Wrapper  
#=================================  
COPY wrap_chrome_binary /opt/bin/wrap_chrome_binary  
RUN chmod 755 /opt/bin/wrap_chrome_binary  
RUN /opt/bin/wrap_chrome_binary  
  
USER seluser  
  
#============================================  
# Chrome webdriver  
#============================================  
# can specify versions by CHROME_DRIVER_VERSION  
# Latest released version will be used by default  
#============================================  
ARG CHROME_DRIVER_VERSION="latest"  
RUN CD_VERSION=$(if [ ${CHROME_DRIVER_VERSION:-latest} = "latest" ]; then echo
$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else
echo $CHROME_DRIVER_VERSION; fi) \  
&& echo "Using chromedriver version: "$CD_VERSION \  
&& wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CD_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CD_VERSION \  
&& sudo ln -fs /opt/selenium/chromedriver-$CD_VERSION /usr/bin/chromedriver

