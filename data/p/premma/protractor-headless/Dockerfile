FROM node:6.9.4-slim  
MAINTAINER Premysl Maly premma@gmail.com  
WORKDIR /tmp  
COPY webdriver-versions.js ./  
ENV PATH=$PATH:/opt/google/chrome  
ENV CHROME_PACKAGE="google-chrome-stable_55.0.2883.75-1_amd64.deb"
NODE_PATH=/usr/local/lib/node_modules  
RUN npm install -g protractor@4.0.14 mocha@3.2.0 jasmine@2.5.3 minimist@1.2.0
protractor-jasmine2-screenshot-reporter && \  
node ./webdriver-versions.js --chromedriver 2.28 && \  
webdriver-manager update && \  
apt-get update && \  
apt-get install -y xvfb wget openjdk-7-jre && \  
wget https://github.com/webnicer/chrome-
downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \  
dpkg --unpack ${CHROME_PACKAGE} && \  
apt-get install -f -y && \  
apt-get clean && \  
rm ${CHROME_PACKAGE} && \  
mkdir /protractor  
ADD protractor.sh /protractor.sh  
RUN chmod a+x /protractor.sh  
VOLUME /protractor  
WORKDIR /protractor  
ENTRYPOINT ["/protractor.sh"]  
  
#  
# Do not forget to add this piece of code into protractor config:  
# capabilities: {  
# 'browserName': 'chrome',  
# chromeOptions: {  
# args: ['--no-sandbox']  
# }  
# },  
# directConnect: true,  
#

