FROM upspeck/gradle:2.11  
MAINTAINER Jeyson Maia <jeyson@upspeck.io>  
  
RUN \  
apt-get update && \  
apt-get install -y wget unzip && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
wget -N
http://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip && \  
unzip chromedriver_linux64.zip && \  
rm chromedriver_linux64.zip && \  
chmod +x chromedriver && \  
mv -f chromedriver /usr/bin/chromedriver && \  
apt-get update && apt-get install -y \  
ca-certificates \  
libgl1-mesa-dri \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
xvfb --no-install-recommends && \  
apt-get purge -y wget unzip && \  
apt-get install -y \  
google-chrome-stable && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

