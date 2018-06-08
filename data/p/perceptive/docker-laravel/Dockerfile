FROM perceptive/docker-php71  
  
WORKDIR /tmp  
RUN echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list  
RUN echo 'deb-src http://packages.dotdeb.org jessie all' >>
/etc/apt/sources.list  
  
RUN curl -SLO https://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg  
  
RUN apt-get update && apt-get install -y \  
libz-dev \  
libmemcached-dev \  
xz-utils \  
php7.0-memcached \  
php7.0-bz2  
#RUN pecl install memcached  
#RUN echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini  
#RUN apt-get install php-memcached  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.9.4  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz"  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"  
RUN gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc  
RUN grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c -  
RUN tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1  
  
WORKDIR /var/www/html  

