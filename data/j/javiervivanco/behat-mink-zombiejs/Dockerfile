FROM alpine:3.2  
RUN apk update  
RUN apk add --no-progress \  
bash \  
binutils-libs \  
ca-certificates \  
g++ \  
gcc \  
git \  
make \  
nodejs \  
openssh-client \  
openssl \  
php-bcmath \  
php-calendar \  
php-cli \  
php-common \  
php-ctype \  
php-curl \  
php-dom \  
php-intl \  
php-json \  
php-pdo \  
php-pdo_sqlite \  
php-pdo_mysql \  
php-pdo_pgsql \  
php-mcrypt \  
php-sqlite3 \  
php-pear \  
php-phar \  
php-posix \  
php-sockets \  
php-xml \  
python \  
php-zip \  
php-openssl \  
sudo  
RUN addgroup -g 1000 user  
RUN adduser user -D -u 1000 -G user  
RUN echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/user  
RUN mkdir /data  
RUN chown user:user /data  
VOLUME /data  
USER user  
RUN sudo npm install -g zombie@v2.5.1  
ENV NODE_PATH /usr/lib/node_modules/  
ADD https://getcomposer.org/composer.phar /usr/local/bin/composer  
RUN sudo chmod 755 /usr/local/bin/composer  
RUN mkdir -p /home/user/.composer  
ADD composer.json /home/user/.composer/  
RUN composer global install  
ENV PATH $PATH:/home/user/bin/  
RUN sudo apk del binutils-libs g++ gcc make python --purge

