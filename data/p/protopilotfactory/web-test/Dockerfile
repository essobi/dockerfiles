FROM protopilotfactory/node:latest  
  
#=========  
# Adding Headless Selenium with Chrome and Firefox  
#=========  
ENV CHROME_DRIVER_VERSION 2.20  
# Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
RUN apt-get update && apt-get install -y \  
google-chrome-stable  
  
# Chrome driver  
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip  
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/  
RUN chmod ugo+rx /usr/bin/chromedriver  
  
# Dependencies to make "headless" selenium work  
RUN apt-get -y install \  
gtk2-engines-pixbuf \  
libxtst6 \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-base \  
xfonts-cyrillic \  
xfonts-scalable \  
xvfb && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  

