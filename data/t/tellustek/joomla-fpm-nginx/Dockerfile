FROM php:fpm  
MAINTAINER Shingo <shingo@tellustek.com>  
  
# Install PHP extensions  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev zip unzip \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
VOLUME /var/www/html  
  
# Define Joomla version and expected SHA1 signature  
ENV JOOMLA_VERSION 3.4.4  
ENV JOOMLA_SHA1 371ed0a987a4c66b4f711b8e27a785f84050de90  
  
# Download package and extract to web volume  
RUN curl -o joomla.zip -SL https://github.com/joomla/joomla-
cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-
Full_Package.zip \  
&& echo "$JOOMLA_SHA1 *joomla.zip" | sha1sum -c - \  
&& mkdir /usr/src/joomla \  
&& unzip joomla.zip -d /usr/src/joomla \  
&& rm joomla.zip \  
&& chown -R www-data:www-data /usr/src/joomla  
  
# Install Git  
RUN apt-get install -y git  
RUN curl -o .gitignore -SL
https://raw.githubusercontent.com/shingo0620/gitignore/master/Joomla.gitignore
\  
&& chown www-data:www-data .gitignore \  
&& mv .gitignore /usr/src/joomla  
  
# Install Nginx  
RUN apt-get install -y nginx  
  
# Copy joomla into /var/www/html  
# Forward request and error logs to docker log collector  
# Remove useless source  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./docker-entrypoint.sh /entrypoint.sh  
ADD ./makedb.php /makedb.php  
ADD ./webhook.php /var/www/html/webhook.php  
ADD ./config/nginx/default /etc/nginx/sites-available/default  
ADD ./config/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD ./config/php-fpm/php-fpm.conf /usr/local/etc/php-fpm.conf  
ADD ./config/php-fpm/php.ini /usr/local/etc/php/conf.d/php.ini  
  
EXPOSE 80 443  
ENTRYPOINT ["/entrypoint.sh"]  
CMD nginx && php-fpm  

