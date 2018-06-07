FROM node:6.11.5-alpine  
LABEL maintainer="John Costanzo"  
  
# Environment variables  
ENV EMBER_VERSION=2.16.0 APP_DIR=/app PATH=/root/.yarn/bin:$PATH  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache --virtual build-dependencies \  
bash \  
curl \  
git \  
gnupg \  
build-base \  
automake \  
autoconf \  
tar \  
linux-headers && \  
touch ~/.bashrc && \  
/bin/bash && \  
mkdir /app && \  
curl -o- -L https://yarnpkg.com/install.sh | bash && \  
git clone https://github.com/facebook/watchman.git && \  
cd watchman && \  
git checkout v4.7.0 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
mkdir /tmp/phantomjs && \  
curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -xvj -C /tmp/phantomjs --strip-components=1
phantomjs-2.1.1-linux-x86_64/bin && \  
mv /tmp/phantomjs/bin/phantomjs /usr/bin && \  
rm -rf /tmp/phantomjs && \  
yarn global add ember-cli@$EMBER_VERSION && \  
apk del build-dependencies && \  
rm -Rf /tmp/* ** \  
rm -rf /var/cache/apk/*  
  
EXPOSE 4200 7020 7357 9222  
  
WORKDIR /app  
  
CMD ["/entrypoint.sh"]

