FROM node:6-slim  
  
VOLUME /tests  
VOLUME /resources  
VOLUME /results  
VOLUME /commands  
  
ENV SELENIUM_HOST 'localhost'  
ENV SELENIUM_PORT 4444  
ENV SELENIUM_ENV chrome,firefox  
  
ENV SRC_FOLDERS ''  
ENV LAUNCH_URL 'http://localhost'  
ENV RETRIES 1  
ENV LOG_LEVEL 'result'  
RUN npm install -g \  
webdriverio \  
wdio-firefox-profile-service \  
wdio-junit-reporter \  
wdio-mocha-framework \  
wdio-spec-reporter \  
babel-plugin-transform-runtime \  
babel-register \  
babel-preset-es2015 \  
chai \  
mocha \  
node-fetch \  
sinon  
  
RUN groupadd -r webdriverio && useradd -r -g webdriverio webdriverio  
  
COPY *.js .  
  
USER webdriverio  
  
CMD wdio -c ./wdio.conf.js  

