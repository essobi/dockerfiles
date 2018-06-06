FROM crabho/ci-build-php:5.6  
# Install SSL cert  
#COPY ./cert/*.crt /usr/local/share/ca-certificates/  
#RUN chmod 640 /usr/local/share/ca-certificates/* && update-ca-certificates  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
# Set timezone  
ENV TZ "Asia/Taipei"  
RUN echo "Asia/Taipei" | tee /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Install tools  
RUN apt-get update && apt-get install -y \  
unzip \  
wget \  
xvfb  
  
# Setup env  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
# Install chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google-chrome.list  
  
RUN apt-get update && apt-get install -y \  
google-chrome-stable && \  
rm /etc/apt/sources.list.d/google-chrome.list && \  
rm -rf /var/lib/apt/lists/*  
  
# Chrome driver  
ENV CHROME_DRIVER_VERSION 2.20  
COPY ./tools/chromedriver_linux64.zip /tmp/  
#RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
RUN rm -rf /opt/selenium/chromedriver && \  
unzip /tmp/chromedriver_linux64.zip -d /opt/selenium && \  
rm /tmp/chromedriver_linux64.zip && \  
mv /opt/selenium/chromedriver
/opt/selenium/chromedriver-$CHROME_DRIVER_VERSION && \  
chmod +x /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION && \  
ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver  
  
# Install selenium 2.48.2  
ENV SELENIUM_VERSION 2.48.2  
COPY ./tools/selenium-server-standalone-$SELENIUM_VERSION.jar
/opt/selenium/selenium-server-standalone.jar  
# RUN chmod 644 /opt/selenium/selenium-server-standalone.jar  
# Install script  
COPY ./sh/entry_point.sh /opt/bin/entry_point.sh  
RUN chmod +x /opt/bin/entry_point.sh  
  
COPY ./sh/chrome_launcher.sh /opt/google/chrome/google-chrome  
RUN chmod +x /opt/google/chrome/google-chrome  
  
ENTRYPOINT ["/opt/bin/entry_point.sh"]  

