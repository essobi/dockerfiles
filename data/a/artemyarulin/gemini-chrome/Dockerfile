FROM selenium/standalone-chrome  
WORKDIR /tmp  
USER root  
  
ENV VER_NODE="9.3.0"  
ENV VER_GEMINI="5.1.2"  
ENV VER_CHROMEDRIVER="2.34.0"  
RUN apt-get -qq update && apt-get -qq install python build-essential -y && \  
wget -qO setup https://nodejs.org/dist/v$VER_NODE/node-v$VER_NODE-
linux-x64.tar.gz && \  
tar -C /usr/local \--strip-components=1 -xf setup && \  
npm install --silent --no-save && npm install gemini@$VER_GEMINI
chromedriver@$VER_CHROMEDRIVER  

