FROM node:9.8.0  
ARG EMBER_VERSION=3.0.0  
ARG WATCHMAN_VERSION=4.9.0  
ARG LIVE_RELOAD_PORT=9999  
ARG BUILD_DATE  
  
  
LABEL name="ember-cli ${EMBER_VERSION}" \  
maintainer="Thomas J. Taylor <thomas@infotechsoft.com>" \  
build-date="${BUILD_DATE}"  
# Add Python, Build Watchman, Remove Python  
RUN set -ex && \  
apt-get update && \  
apt-get install -y --no-install-recommends python-dev && \  
curl -SL
"https://github.com/facebook/watchman/archive/v${WATCHMAN_VERSION}.tar.gz" |
tar -xz -C /tmp/ && \  
cd /tmp/watchman-${WATCHMAN_VERSION} && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/* && \  
apt-get purge -y --auto-remove python-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Add Ember, Bower, PhantomJS, and Check-Dependencies  
RUN npm install -g ember-cli@${EMBER_VERSION} && \  
npm install -g bower --unsafe-perm=true && \  
npm install -g phantomjs-prebuilt --unsafe-perm=true && \  
npm install -g check-dependencies  
  
  
EXPOSE 4200 ${LIVE_RELOAD_PORT}  
  
VOLUME /usr/local/ember  
WORKDIR /usr/local/ember  
  
ENV PATH=/usr/local/ember/bin:$PATH  
  
# 7: Set the default command:  
CMD ["ember", "server", "--live-reload-port", "${LIVE_RELOAD_PORT}"]

