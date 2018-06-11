FROM ubuntu:16.04  
MAINTAINER Viet Duong<viet.duong@hotmail.com>  
  
# Set one or more individual labels  
LABEL vietcli.docker.base.image.version="0.1.0-beta"  
LABEL vendor="[VietCLI] vietduong/mage2-image"  
LABEL vietcli.docker.base.image.release-date="2017-02-11"  
LABEL vietcli.docker.base.image.version.is-production=""  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
RUN mkdir /var/run/sshd  
RUN mkdir /run/php  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Custom Environment Variables  
ENV HTTP_SERVER_NAME magento2.local  
  
# Update apt-get  
RUN apt-get update  
RUN apt-get -y upgrade  
  
## Add repo to install PHP7.1 on Ubuntu 16  
RUN apt-get -y install software-properties-common  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
# Basic Requirements  
RUN apt-get update  
RUN apt-get -y install pwgen python-setuptools curl git nano sudo unzip
openssh-server openssl  
#RUN apt-get -y install mysql-server nginx php-fpm php-mysql  
RUN apt-get -y install nginx php7.1-fpm php7.1-mysql  
  
# Install imagemagick  
RUN apt-get -y install imagemagick  
  
# Install Xdebug  
#RUN apt-get -y install php-xdebug \  
#&& PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;") \  
#&& PHP_EXT_DIR=$(php -i | grep extension_dir | tr -s ' ' | cut -d ' ' -f 5) \  
#&& echo "[Xdebug]" >> /etc/php/$PHP_VERSION/fpm/php.ini \  
#&& echo "zend_extension=\"${PHP_EXT_DIR}/xdebug.so\"" >>
/etc/php/$PHP_VERSION/fpm/php.ini \  
#&& echo "xdebug.remote_enable = 1" >> /etc/php/$PHP_VERSION/fpm/php.ini \  
#&& echo "xdebug.remote_port = 9000" >> /etc/php/$PHP_VERSION/fpm/php.ini \  
#&& echo "xdebug.idekey = VIETCLI" >> /etc/php/$PHP_VERSION/fpm/php.ini \  
#&& echo "xdebug.max_nesting_level = 512" >> /etc/php/$PHP_VERSION/fpm/php.ini
\  
#&& echo "xdebug.file_link_format = phpstorm://open?%f:%l" >>
/etc/php/$PHP_VERSION/fpm/php.ini \  
#&& echo "[Xdebug]" >> /etc/php/$PHP_VERSION/cli/php.ini \  
#&& echo "zend_extension=\"${PHP_EXT_DIR}/xdebug.so\"" >>
/etc/php/$PHP_VERSION/cli/php.ini \  
#&& echo "xdebug.remote_enable = 1" >> /etc/php/$PHP_VERSION/cli/php.ini \  
#&& echo "xdebug.remote_port = 9000" >> /etc/php/$PHP_VERSION/cli/php.ini \  
#&& echo "xdebug.idekey = VIETCLI" >> /etc/php/$PHP_VERSION/cli/php.ini \  
#&& echo "xdebug.max_nesting_level = 512" >> /etc/php/$PHP_VERSION/cli/php.ini
\  
#&& echo "xdebug.file_link_format = phpstorm://open?%f:%l" >>
/etc/php/$PHP_VERSION/cli/php.ini \  
#&& echo "xdebug.profiler_enable=0" >> /etc/php/$PHP_VERSION/mods-
available/xdebug.ini \  
#&& echo "xdebug.remote_host=172.18.0.1" >> /etc/php/$PHP_VERSION/mods-
available/xdebug.ini \  
# Magento 2 Requirements  
RUN apt-get -y install php7.1-imagick php7.1-intl php7.1-curl php7.1-xsl
php7.1-mcrypt php7.1-mbstring php7.1-bcmath php7.1-gd php7.1-zip php7.1-soap  
  
# nginx config  
RUN sed -i -e"s/user\s*www-data;/user vietcli www-data;/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN sed -i "61i \\\\\troot /home/vietcli/files/html;" /etc/nginx/nginx.conf  
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
# php-fpm config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e
"s/;always_populate_raw_post_data\s*=\s*-1/always_populate_raw_post_data =
-1/g" /etc/php/7.1/fpm/php.ini  
#RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.1/fpm/pool.d/www.conf  
RUN sed -i -e "s/user\s*=\s*www-data/user = vietcli/g"
/etc/php/7.1/fpm/pool.d/www.conf  
RUN echo "php_admin_flag[log_errors] = on" >> /etc/php/7.1/fpm/pool.d/www.conf  
RUN echo "php_admin_value[memory_limit] = -1" >>
/etc/php/7.1/fpm/pool.d/www.conf  
RUN echo "php_admin_value[max_execution_time] = 3600" >>
/etc/php/7.1/fpm/pool.d/www.conf  
RUN echo "php_admin_value[max_input_vars] = 36000" >>
/etc/php/7.1/fpm/pool.d/www.conf  
RUN echo "php_admin_value[post_max_size] = 20M" >>
/etc/php/7.1/fpm/pool.d/www.conf  
RUN echo "php_admin_value[upload_max_filesize] = 20M" >>
/etc/php/7.1/fpm/pool.d/www.conf  
# replace # by ; RUN find /etc/php/7.0/mods-available/tmp -name "*.ini" -exec
sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;  
# nginx site conf  
ADD ./nginx-site.conf /etc/nginx/sites-available/default  
ADD ./nginx.magento2.conf /etc/nginx/sites-available/magento2.conf  
  
# Generate self-signed ssl cert  
RUN mkdir /etc/nginx/ssl/  
RUN openssl req \  
-new \  
-newkey rsa:4096 \  
-days 365 \  
-nodes \  
-x509 \  
-subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=localhost" \  
-keyout /etc/ssl/private/ssl-cert-snakeoil.key \  
-out /etc/ssl/certs/ssl-cert-snakeoil.pem  
  
# Install composer and modman  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN curl -sSL https://raw.github.com/colinmollenhour/modman/master/modman >
/usr/sbin/modman  
RUN chmod +x /usr/sbin/modman  
  
# Install Ioncube  
# php7.1-dev has issue with nginx, therefore we cannot use php-config here  
# Here is the solution : PHP_EXT_DIR=$(php -i | grep extension_dir | tr -s ' '
| cut -d ' ' -f 5)  
RUN wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar xvfz ioncube_loaders_lin_x86-64.tar.gz \  
&& PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;") \  
&& PHP_EXT_DIR=$(php -i | grep extension_dir | tr -s ' ' | cut -d ' ' -f 5) \  
# && PHP_EXT_DIR=$(php-config --extension-dir) \  
&& mkdir -p $PHP_EXT_DIR \  
&& cp "ioncube/ioncube_loader_lin_${PHP_VERSION}.so" $PHP_EXT_DIR \  
&& cp "ioncube/ioncube_loader_lin_${PHP_VERSION}_ts.so" $PHP_EXT_DIR \  
&& rm -rf ioncube ioncube_loaders_lin_x86-64.tar.gz \  
&& sed -i "925i \ \ " /etc/php/$PHP_VERSION/fpm/php.ini \  
&& sed -i "925i zend_extension =
${PHP_EXT_DIR}/ioncube_loader_lin_${PHP_VERSION}.so"
/etc/php/$PHP_VERSION/fpm/php.ini \  
&& sed -i "925i \ \ " /etc/php/${PHP_VERSION}/cli/php.ini \  
&& sed -i "925i zend_extension =
${PHP_EXT_DIR}/ioncube_loader_lin_${PHP_VERSION}.so"
/etc/php/$PHP_VERSION/cli/php.ini  
  
# Reload PHP Configurations  
RUN service php7.1-fpm restart  
  
# Add system user for Magento  
RUN useradd -m -d /home/vietcli -p $(openssl passwd -1 'vietcli') -G root -s
/bin/bash vietcli \  
&& usermod -a -G www-data vietcli \  
&& usermod -a -G sudo vietcli \  
&& mkdir -p /home/vietcli/files/html \  
&& chown -R vietcli:www-data /home/vietcli/files \  
&& chmod -R 775 /home/vietcli/files  
  
# Magento Initialization and Startup Script  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
#NETWORK PORTS  
# private expose  
EXPOSE 443  
EXPOSE 80  
EXPOSE 22  
# volume for mysql database and magento install  
VOLUME ["/home/vietcli/files", "/home/vietcli/.log", "/var/run/sshd"]  
  
CMD ["/bin/bash", "/start.sh"]

