FROM ruby:latest  
RUN apt-get update \  
&& apt-get install -y ruby-dev zlib1g-dev liblzma-dev build-essential git
unzip libfontconfig1 libssl-dev \  
libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 \  
libxtst6 libcups2 libxss1 libxrandr2 libasound2 libatk1.0-0 libgtk-3-0 \  
xvfb fonts-ipafont-gothic fonts-ipafont-mincho \  
&& rm -rf /var/lib/apt/lists/*  
RUN gem install nokogiri  
RUN gem install nokogiri -v '~> 1.7.0'  
RUN gem install nokogiri -v '~> 1.6.0'  
#============================================  
# Google Chrome  
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
ARG CHROME_DRIVER_VERSION=2.37  
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

