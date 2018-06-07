FROM ubuntu:16.04  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL maintainer="EfficientHealth <support@efficienthealth.com>" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.schema-version="1.0"  
  
###  
### Base PHP7.1 + Utilities  
###  
RUN \  
apt-get update -y && \  
apt-get install -y software-properties-common python-software-properties && \  
LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && \  
apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
tar \  
xz-utils \  
openssh-client \  
git \  
zip \  
unzip \  
php7.1-bcmath \  
php7.1-cli \  
php7.1-curl \  
php7.1-mysqlnd \  
php7.1-mbstring \  
php7.1-xml \  
php-redis \  
  
### rsync for build  
rsync \  
  
python-setuptools \  
python-pip && \  
pip install -q awscli && \  
php -m && \  
curl -L https://packagecloud.io/phalcon/stable/gpgkey | apt-key add \- && \  
echo "deb https://packagecloud.io/phalcon/stable/ubuntu/ xenial main" | tee
/etc/apt/sources.list.d/phalcon-stable.list && \  
echo "deb-src https://packagecloud.io/phalcon/stable/ubuntu/ xenial main" |
tee -a /etc/apt/sources.list.d/phalcon-stable.list && \  
apt-get update && \  
apt-get -y --no-install-recommends install \  
php7.1-phalcon && \  
apt-get purge -y python-pip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
  
###  
### Node  
###  
RUN groupadd --gid 1000 node && \  
useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NODE_VERSION=8.7.0  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
###  
### Composer  
###  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
###  
### Yarn  
###  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
###  
### aws-code-deploy  
###  
RUN npm install aws-code-deploy@1.0.8 --global  
  
###  
### V8 + V8JS  
###  
RUN add-apt-repository -y ppa:pinepain/libv8-6.0 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y libv8-6.0.286 libv8-6.0-dev
wget re2c php7.1-dev && \  
rm -rf /tmp/v8js.tar.gz && \  
rm -rf /tmp/v8js-1.4.1 && \  
wget https://github.com/phpv8/v8js/archive/1.4.1.tar.gz -O /tmp/v8js.tar.gz &&
\  
tar -xf /tmp/v8js.tar.gz -C /tmp && \  
cd /tmp/v8js-1.4.1 && \  
phpize && \  
./configure --with-v8js=/opt/libv8-6.0 && \  
make install && \  
cd / && \  
echo "extension=v8js.so" > /etc/php/7.1/mods-available/v8js.ini && \  
ln -s /etc/php/7.1/mods-available/v8js.ini /etc/php/7.1/cli/conf.d/20-v8js.ini
&& \  
rm -rf /tmp/v8js.tar.gz && \  
rm -rf /tmp/v8js-1.4.1 && \  
apt-get remove -y wget re2c php7.1-dev && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  

