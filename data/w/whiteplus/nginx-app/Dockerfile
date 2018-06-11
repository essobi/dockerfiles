FROM buildpack-deps:jessie  
  
MAINTAINER WHITEPLUS System "sysadmin@wh-plus.com"  
# Ref: https://hub.docker.com/_/nginx/  
# Ref: https://hub.docker.com/_/php/  
# Ref: https://hub.docker.com/_/node/  
  
ENV NGINX_VERSION 1.9.5-1~jessie  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.7.0  
  
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list
\  
# gpg keys - NGNINX  
&& apt-key adv \--keyserver hkp://pgp.mit.edu:80 \--recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
# gpg keys - beats  
&& apt-key adv \--keyserver hkp://pgp.mit.edu:80 \--recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4 \  
&& echo "deb http://packages.elastic.co/beats/apt stable main" | tee -a
/etc/apt/sources.list.d/beats.list \  
# gpg keys listed at https://github.com/nodejs/node  
&& set -ex \  
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
gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$key"; \  
done \  
# APT - Update/Upgrade/Install  
&& apt-get update 1> /dev/null \  
&& apt-get upgrade -y -q \--no-install-recommends \  
&& apt-get install -y \--no-install-recommends \  
# CA-Certificates  
ca-certificates \  
# NGINX  
nginx=${NGINX_VERSION} \  
# Supervisord  
supervisor \  
# beats  
packetbeat \  
# PHP5  
php5-fpm php5-mysql php-apc php5-curl php5-gd php5-intl php5-mcrypt
php5-memcache \  
php5-sqlite php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-mongo
libapache2-mod-php5 \  
php5-xdebug \  
# NODE  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg \--batch \--decrypt \--output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
# APT - Clean  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

