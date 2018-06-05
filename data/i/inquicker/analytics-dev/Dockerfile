FROM java  
  
ENTRYPOINT ["/usr/local/bin/boot"]  
  
VOLUME ["/.boot", "/m2", "/app"]  
  
ENV BOOT_AS_ROOT=yes \  
BOOT_HOME=/.boot \  
BOOT_JVM_OPTIONS=-Xmx2g \  
BOOT_LOCAL_REPO=/m2 \  
LIBSODIUM_VERSION=1.0.11 \  
PHANTOMJS_VERSION=1.9.8 \  
SASS_LIBSASS_PATH=/tmp/libsass \  
SASS_VERSION=3.3.6  
RUN apt-get update && \  
apt-get -y install build-essential && \  
curl -LOs
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar xjf phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
cp phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/local/bin/ &&
\  
rm -r phantomjs-$PHANTOMJS_VERSION-linux-x86_64 phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
curl -LOs
https://github.com/jedisct1/libsodium/releases/download/$LIBSODIUM_VERSION/libsodium-$LIBSODIUM_VERSION.tar.gz
&& \  
tar -zxvf libsodium-$LIBSODIUM_VERSION.tar.gz && \  
(cd libsodium-$LIBSODIUM_VERSION && ./configure && make && make check && make
install) && \  
git clone \--branch $SASS_VERSION \--depth 1
https://github.com/sass/libsass.git /tmp/libsass && \  
git clone \--branch $SASS_VERSION \--depth 1 https://github.com/sass/sassc.git
/tmp/sassc && \  
cd /tmp/sassc && \  
make && \  
cp /tmp/sassc/bin/sassc /usr/local/bin/sassc && \  
curl -L -o /usr/local/bin/boot https://github.com/boot-clj/boot-
bin/releases/download/latest/boot.sh && \  
chmod +x /usr/local/bin/boot && \  
apt-get -y remove build-essential && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /app  

