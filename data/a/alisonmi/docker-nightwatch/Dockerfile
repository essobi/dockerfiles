FROM java:8-jre  
  
## Install dependencies: nodejs, chrome and xvfb  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y nodejs google-chrome-stable xvfb && \  
npm install -g nightwatch && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tests  
  
## Fix for selenium issue, see: https://github.com/SeleniumHQ/docker-
selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
## Run nightwatch tests using xvfb  
CMD xvfb-run --server-args="-screen 0 1600x1200x24" nightwatch  

