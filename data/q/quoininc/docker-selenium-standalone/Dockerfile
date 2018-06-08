FROM ubuntu:14.04  
ENTRYPOINT ["/entrypoint"]  
ENV DEBIAN_FRONTEND noninteractive  
EXPOSE 4444 5900  
RUN apt-get update -q &&\  
apt-get install -yq default-jre-headless firefox chromium-browser wget unzip
fluxbox xserver-xorg-video-dummy-lts-trusty x11vnc &&\  
apt-get clean  
  
ENV FIREFOX_VERSION 38.0  
RUN cd /opt &&\  
wget
http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 &&\  
tar -xf firefox*.tar.bz2 &&\  
ln -sf $(pwd)/firefox/firefox /usr/bin/firefox &&\  
rm firefox*.tar.bz2  
  
ENV SELENIUM_JAR_URL http://selenium-
release.storage.googleapis.com/2.45/selenium-server-standalone-2.45.0.jar  
RUN cd /opt &&\  
wget "$SELENIUM_JAR_URL" -O selenium-standalone.jar  
  
ENV CHROME_DRIVER_URL
http://chromedriver.storage.googleapis.com/2.15/chromedriver_linux64.zip  
RUN cd /opt &&\  
wget "$CHROME_DRIVER_URL" -O chrome-driver.zip &&\  
cd /opt &&\  
unzip /opt/chrome-driver.zip &&\  
rm /opt/chrome-driver.zip &&\  
ln -s /opt/chromedriver /usr/bin/chromedriver  
  
COPY xorg.conf /etc/X11/xorg.conf  
COPY entrypoint /entrypoint  

