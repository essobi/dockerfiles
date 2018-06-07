FROM debian:stretch  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https curl gnupg2 wget unzip && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
nodejs \  
build-essential \  
xvfb && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g karma @angular/cli  
  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb && \  
dpkg -i google-chrome*.deb || apt-get update && apt-get install -f -y && \  
rm google-chrome-stable_current_amd64.deb && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/bin/chromedriver && \  
rm /tmp/chromedriver_linux64.zip  
  
RUN mkdir -p /opt/selenium && \  
curl -sS https://selenium-release.storage.googleapis.com/3.3/selenium-server-
standalone-3.3.1.jar -o /opt/selenium/selenium-server-standalone.jar  
  
ENV DISPLAY :99  
ENV CHROME_BIN /usr/bin/google-chrome  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

