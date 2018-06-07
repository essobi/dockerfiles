FROM ubuntu:14.04  
MAINTAINER Peter Rosell <peter.rosell@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
npm nodejs nodejs-legacy \  
firefox \  
chromium-browser \  
libexif12 \  
default-jre \  
imagemagick \  
xvfb git && \  
apt-get autoremove -y --purge \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install --global npm@latest  
  
RUN npm install -g inherits \  
&& npm install -g \  
yo \  
bower \  
grunt-cli \  
jasmine-node \  
jasmine-reporters@1.0.0 \  
karma \  
karma-chrome-launcher \  
karma-firefox-launcher \  
karma-phantomjs-launcher \  
karma-jasmine \  
karma-junit-reporter \  
karma-ng-scenario \  
protractor \  
&& rm -rf /root/.npm/  
  
RUN webdriver-manager update  
  
ENV NODE_PATH /usr/lib/nodejs/:/usr/local/lib/node_modules/  
  
ENV RUN_NPM_INSTALL false  
ENV RUN_BOWER_INSTALL true  
ENV USER_ID 1000  
ENV GROUP_ID 1000  
  
VOLUME ["/app"]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["karma"]  

