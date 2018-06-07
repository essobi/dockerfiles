FROM ubuntu:trusty  
  
MAINTAINER Ignacio Canó <i.cano@gbh.com.do>  
  
# Install Dependecies  
RUN apt-get -y update && \  
apt-get install -y php5-fpm \  
php5-cli \  
php5-common \  
php5-dev \  
php5-memcache \  
php5-imagick \  
php5-mcrypt \  
php5-mysql \  
php5-imap \  
php5-curl \  
php-pear \  
php5-gd \  
php5-mcrypt \  
nginx \  
curl \  
zip \  
git \  
supervisor  
  
# Install WP CLI  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
  
# Install node, bower and gulp-cli  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash  
ENV NODE_VER v5.12.0  
ENV NVM_DIR "/root/.nvm"  
RUN [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" \  
&& nvm install $NODE_VER \  
&& nvm alias default $NODE_VER \  
&& nvm use default \  
&& npm install -g bower gulp-cli  
ENV BASE_NODE_PATH $NVM_DIR/versions/node  
ENV NODE_PATH $BASE_NODE_PATH/$NODE_VER/lib/node_modules  
ENV PATH $BASE_NODE_PATH/$NODE_VER/bin:$PATH  
  
# Copy confs  
COPY nginx/default /etc/nginx/sites-available  
COPY supervisord /etc/supervisor/conf.d  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php5/cli/php.ini && \  
sed -i "s/display_errors = .*/display_errors = On/" /etc/php5/cli/php.ini && \  
sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php5/cli/php.ini && \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php5/cli/php.ini && \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini && \  
sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php5/fpm/php.ini && \  
sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/"
/etc/php5/fpm/php.ini && \  
sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php5/fpm/php.ini && \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php5/fpm/php.ini && \  
sed -i "s/error_reporting = .*/error_reporting = E_ALL/" /etc/php5/fpm/php.ini
&& \  
sed -i "s/display_errors = .*/display_errors = On/" /etc/php5/fpm/php.ini && \  
sed -i "s/variables_order = .*/variables_order = \"EGPCS\"/"
/etc/php5/fpm/php.ini  
  
# Add our init script  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
RUN mkdir /app  
WORKDIR /app  
RUN touch /app/index.php && echo '<?php phpinfo();?>' > /app/index.php  
  
EXPOSE 80  
CMD ["/run.sh"]

