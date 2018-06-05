FROM homeassistant/home-assistant:latest  
LABEL maintainer="Andrew Sanjanwala <sanfam@gmail.com>"  
  
# Install Chrome for Selenium  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee -a
/etc/apt/sources.list && \  
curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
\- && \  
apt-get update && \  
apt-get -y --no-install-recommends install unzip libxpm4 libxrender1
libgtk2.0-0 libnss3 libgconf-2-4 && \  
apt-get -y --no-install-recommends install google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Selenium Chromedriver  
RUN CHROME_DRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && wget -N
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
-P /tmp  
RUN unzip /tmp/chromedriver_linux64.zip -d /tmp  
RUN install -m 0755 -o root /tmp/chromedriver /usr/local/bin/chromedriver  
  
# Install myChevy python module  
RUN pip install mychevy  

