FROM ruby:2.4.4  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -yqq install unzip  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# Install Google Chrome  
RUN curl -sS -o \- https://dl-ssl.google.com/linux/linux_signing_key.pub |
apt-key add \- && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get -yqq update && \  
apt-get -yqq install google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs fonts-migmix python2.7-dev python-pip\  
&& apt-get clean  
  
COPY local.conf /etc/fonts/local.conf  

