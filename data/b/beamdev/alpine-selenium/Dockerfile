FROM openjdk:8-jre-alpine  
  
Maintainer Pascal Gafner <pascal.gafner@postfinance.ch>  
  
RUN apk add --no-cache \  
chromium \  
chromium-chromedriver && \  
wget https://selenium-release.storage.googleapis.com/3.9/selenium-server-
standalone-3.9.1.jar && \  
rm -rf /var/lib/apt/lists/* \  
/var/cache/apk/* \  
/usr/share/man \  
/tmp/* \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html \  
/usr/lib/node_modules/npm/scripts  
  
ENV CHROME_BIN=/usr/bin/chromium-browser  
ENV CHROME_PATH=/usr/lib/chromium/  
  
ENTRYPOINT java -jar selenium-server-standalone-3.9.1.jar  

