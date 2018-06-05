FROM mhart/alpine-node:9  
  
Maintainer Pascal Gafner <pascal.gafner@postfinance.ch>  
  
RUN apk add --no-cache \  
openjdk8-jre-base \  
nss \  
chromium  
  
# Install node packages  
RUN npm -g install protractor && \  
npm -g install protractor-jasmine2-screenshot-reporter && \  
npm -g install typescript && \  
npm -g install jasmine-core && \  
npm -g install jasmine-reporters && \  
webdriver-manager update --standalone --chrome --gecko false  
# Alternative: user yarn  
# RUN yarn add protractor && \  
# yarn add protractor-jasmine2-screenshot-reporter && \  
# yarn add typescript && \  
# yarn add jasmine-core && \  
# yarn add jasmine-reporters && \  
# Minimize size  
# RUN apk del --purge --force linux-headers binutils-gold gnupg zlib-dev libc-
utils  
RUN rm -rf /var/lib/apt/lists/* \  
/var/cache/apk/* \  
/usr/share/man \  
/tmp/* \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html \  
/usr/lib/node_modules/npm/scripts  
  
ENV CHROME_BIN=/usr/bin/chromium-browser  
ENV CHROME_PATH=/usr/lib/chromium/  
  
CMD ["/usr/bin/webdriver-manager", "start", "\--detach"]  
ENTRYPOINT ["/bin/sh"]  

