FROM redboxdigital/php:7.0-debian  
  
# Node.  
# Copied from node:latest  
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
ENV NODE_VERSION 7.8.0  
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
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN set -xe; \  
\  
apt-get update && apt-get install -y \  
bash \  
curl \  
git \  
mysql-client \  
netcat-openbsd \  
openssh-client \  
pv \  
redis-tools \  
tree \  
vim \  
zip \  
; \  
curl -sS https://getcomposer.org/installer | \  
php -- \  
\--filename=composer \  
\--install-dir=/usr/local/bin \  
; \  
curl -sS -o /usr/local/bin/n98-magerun2
"https://files.magerun.net/n98-magerun2.phar"; \  
chmod a+x /usr/local/bin/n98-magerun2; \  
curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony; \  
chmod a+x /usr/local/bin/symfony;  
  
CMD ["bash"]  

