FROM node:4.4.5  
ENV EMBER_CLI_VERSION 2.5.1  
ENV BOWER_VERSION 1.7.9  
ENV PHANTOMJS_VERSION 2.1.7  
ENV WATCHMAN_VERSION 3.5.0  
WORKDIR /myapp  
  
# Note: npm is v2.14.7  
RUN \  
npm install -g ember-cli@$EMBER_CLI_VERSION && \  
npm install -g bower@$BOWER_VERSION && \  
npm install -g phantomjs-prebuilt@$PHANTOMJS_VERSION  
  
# install watchman  
RUN \  
git clone https://github.com/facebook/watchman.git && \  
cd watchman && \  
git checkout v$WATCHMAN_VERSION && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -r watchman  
  
# optimization!  
RUN \  
curl -o package.json https://raw.githubusercontent.com/ember-cli/ember-new-
output/v$EMBER_CLI_VERSION/package.json && \  
npm install && \  
rm package.json && \  
curl -o bower.json https://raw.githubusercontent.com/ember-cli/ember-new-
output/v$EMBER_CLI_VERSION/bower.json && \  
bower install --allow-root && \  
rm bower.json  
  
RUN \  
ln -s package-temp.json package.json  
  
CMD \  
bower install --allow-root && \  
npm install && \  
cd node_modules && \  
find ember-suave -type d -not -path '*/broccoli-jscs/*' -exec mkdir -p
'../node_modules_temp/{}' ';' && \  
find ember-suave -type f -not -path '*/broccoli-jscs/*' -exec cp '{}'
'../node_modules_temp/{}' ';' && \  
ember server  

