FROM php:5.6-cli  
MAINTAINER tuschl@digitalmobil.com  
  
RUN adduser --gecos "" \--disabled-password --home /home/wp-build wp-build  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
libfontconfig1-dev libpng-dev ssh rsync sudo subversion git bzip2 zip unzip \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
; do \  
gpg --keyserver pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "copy('https://composer.github.io/installer.sig', 'composer-
setup.sig');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
trim(file_get_contents('composer-setup.sig'))) { echo 'Installer verified'; }
else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo
PHP_EOL;" && \  
php composer-setup.php --filename=composer --install-dir=/bin && \  
php -r "unlink('composer-setup.sig');" && \  
php -r "unlink('composer-setup.php');"  
  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV NODE_VERSION 6.5.0  
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
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& curl -o- -L https://yarnpkg.com/install.sh | bash  
  
# Install Bower & Grunt  
RUN npm install -g bower sass grunt grunt-cli && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Define working directory.  
WORKDIR /data  
  
COPY entrypoint.sh /entrypoint.sh  
  
# Define default command.  
CMD ["bash"]  
ENTRYPOINT ["/entrypoint.sh"]  

