FROM ruby:2.3.1-slim  
ENV TERM="xterm" \  
BUNDLE_PATH="/var/www/vendor/bundle" \  
BUNDLE_BIN="/var/www/vendor/bundle/bin" \  
BUNDLE_APP_CONFIG="/var/www/vendor/bundle" \  
PATH="/var/www/vendor/bundle/bin:$PATH" \  
DUMB_INIT_VERSION="1.2.0"  
RUN apt-get update && \  
apt-get install -y sudo wget && \  
wget https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb && \  
dpkg -i dumb-init_${DUMB_INIT_VERSION}_amd64.deb && \  
rm dumb-init_${DUMB_INIT_VERSION}_amd64.deb && \  
mkdir -p /var/www/.bundle && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/achives && \  
useradd -u 1000 -G sudo -m debian && \  
chown -R debian:debian /var/www && \  
chmod a-w /etc/sudoers  
COPY config /var/www/.bundle  
COPY sudoers /etc/  
WORKDIR /var/www  
EXPOSE 3000  
USER debian  
ENTRYPOINT ["/usr/bin/dumb-init"]  

