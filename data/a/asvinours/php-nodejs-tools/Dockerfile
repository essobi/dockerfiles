FROM asvinours/php-base:latest  
  
RUN apt-get update \  
&& apt-get install -y \  
rsync \  
cmake \  
pngquant \  
autoconf \  
automake \  
libtool \  
nasm \  
make  
  
# Install composer and phan  
RUN wget http://getcomposer.org/composer.phar \  
&& chmod +x composer.phar \  
&& mv composer.phar /usr/local/bin/composer \  
&& curl -SsL https://github.com/etsy/phan/releases/download/0.9.2/phan.phar -o
/usr/local/bin/phan \  
&& chmod +x /usr/local/bin/phan  
  
# Add PHPMD, PHPCS and PHPCPD  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x phpmd.phar \  
&& mv phpmd.phar /usr/local/bin/phpmd \  
&& wget https://phar.phpunit.de/phpcpd.phar \  
&& chmod +x phpcpd.phar \  
&& mv phpcpd.phar /usr/local/bin/phpcpd \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& chmod +x phpcbf.phar \  
&& mv phpcbf.phar /usr/local/bin/phpcbf  
  
# Install php-ast extension  
RUN git clone https://github.com/nikic/php-ast.git /tmp/php-ast \  
&& cd /tmp/php-ast \  
&& phpize \  
&& ./configure \  
&& make -j4 \  
&& make install \  
&& docker-php-ext-enable ast \  
&& cd \  
&& rm -rf /tmp/php-ast  
  
# Install nodejs  
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
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.1.2  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/bin/node  
  
# Install zstandard  
RUN mkdir -p /opt/zstd \  
&& cd /opt/zstd \  
&& git clone https://github.com/facebook/zstd.git . \  
&& make \  
&& ln -s /opt/zstd/zstd /usr/local/bin/zstd  
  
# Install zopfli  
RUN mkdir -p /opt/zopfli \  
&& cd /opt/zopfli \  
&& git clone https://github.com/google/zopfli . \  
&& make \  
&& make zopflipng \  
&& ln -s /opt/zopfli/zopfli /usr/local/bin/zopfli \  
&& ln -s /opt/zopfli/zopflipng /usr/local/bin/zopflipng  
  
# Install Brotli  
RUN mkdir -p /opt/brotli \  
&& cd /opt/brotli \  
&& git clone https://github.com/google/brotli.git . \  
&& mkdir out \  
&& cd out \  
&& ../configure-cmake \  
&& make \  
&& make test \  
&& make install  
  
RUN mkdir -p /opt/mozjpeg \  
&& cd /opt/mozjpeg \  
&& git clone https://github.com/mozilla/mozjpeg.git . \  
&& git checkout v3.2 \  
&& autoreconf -fiv \  
&& mkdir build && cd build \  
&& sh ../configure \  
&& make install \  
&& ln -s /opt/mozjpeg/bin/jpegtran /usr/local/bin/mozjpeg  
  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/local/bin/jq  
RUN chmod +x /usr/local/bin/jq  
  
RUN echo "UserKnownHostsFile /home/user/.ssh/known_hosts" >>
/etc/ssh/ssh_config  
  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV HOME /home/user  
CMD []  

