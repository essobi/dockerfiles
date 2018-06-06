FROM catchdigital/php:7.1.10-fpm  
  
MAINTAINER Alberto Conteras <a.contreras@catchdigital.com>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y git rsync zip unzip ssh  
RUN apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Add node  
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
  
ENV NODE_VERSION 0.12.17  
RUN buildDeps='xz-utils' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Add composer dependencies  
ENV COMPOSER_HOME '/composer'  
RUN composer global require "acquia/blt:^8.9"  
  
# Add blt as global  
# COPY ./blt /usr/local/bin/blt  
# RUN chmod +x /usr/local/bin/blt  
# Add composer bin to path  
# RUN echo 'export PATH="$PATH:~/.composer/vendor/bin"' > ~/.bashrc  
RUN ln -s $COMPOSER_HOME/vendor/bin/blt /usr/local/bin/blt  
  
# Set directory and working permissions  
WORKDIR /var/www  
  
RUN usermod -u 1000 www-data  
RUN usermod -a -G users www-data  
  
RUN chown -R www-data:www-data /var/www  
  
# Add enviromental vars and git global config  
RUN echo 'git config --global user.name $GIT_NAME' >> ~/.bashrc  
RUN echo 'git config --global user.email $GIT_EMAIL' >> ~/.bashrc  
RUN echo 'git config --global core.fileMode false' >> ~/.bashrc  

