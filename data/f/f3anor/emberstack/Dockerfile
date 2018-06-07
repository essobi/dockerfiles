FROM phusion/baseimage:0.9.19  
WORKDIR /app  
  
RUN set -x && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install --no-install-recommends -y -q git nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN npm install -g -q bower ember-cli && npm cache clean  
  
ENV WATCHMAN_VERSION v4.7.0  
RUN set -x && \  
apt-get update && \  
apt-get install -q -y --no-install-recommends build-essential autoconf
automake && \  
git clone https://github.com/facebook/watchman.git && \  
cd watchman && \  
git checkout $WATCHMAN_VERSION && \  
./autogen.sh && \  
./configure --without-python && \  
make && \  
make install && \  
cd .. && \  
rm -rf watchman && \  
apt-get purge -y build-essential autoconf automake && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
ADD entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  
  
CMD [ "ember", "server" ]  
  
VOLUME [ "/app/bower_components", "/app/node_modules" ]  

