FROM node:8.2.1-slim  
WORKDIR /tmp  
LABEL description="protractor with true headless chrome" \  
version="1.0" \  
maintainer="thiago.stahlschmidt@bcb.gov.br"  
ENV CHROME="google-chrome-stable_60.0.3112.90-1_amd64.deb"  
RUN apt-get update && \  
apt-get install -y openjdk-7-jre && \  
npm install -g protractor@4.0.14 jasmine@2.7.0 && \  
sed -i
"/webdriverVersions/,/},/{/chromedriver/{s,[\"][0-9.]*[\"],\"2.31\",};}"
/usr/local/lib/node_modules/protractor/node_modules/webdriver-
manager/built/config.json && \  
webdriver-manager update && \  
wget https://dl.google.com/linux/deb/pool/main/g/google-chrome-
stable/${CHROME} && \  
dpkg --unpack ${CHROME} && \  
apt-get install -f -y && \  
apt-get clean && \  
rm ${CHROME} && \  
mkdir /protractor && \  
echo '#!/bin/bash\nprotractor "$@"' >> /protractor/protractor.sh && \  
chmod 755 /protractor/protractor.sh  
ENTRYPOINT ["/protractor/protractor.sh"]  

