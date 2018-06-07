from nginx:latest  
MAINTAINER Dmitriy Didyk <didyk@plasticjam.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV DOCUMENT_ROOT /usr/share/nginx/html  
ENV WP_CLI wp --path='/usr/share/nginx/html' \--allow-root  
ENV WP_URL localhost  
  
#Install nginx php-fpm php-pdo unzip curl  
RUN apt-get update  
RUN apt-get -y install php5-fpm unzip curl apt-utils php5-curl php5-gd
php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache
php5-pspell php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl  
  
# nginx config  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 10m/" /etc/nginx/nginx.conf  
RUN sed -i -e "s|include /etc/nginx/conf.d/\\*.conf|include /etc/nginx/sites-
enabled/\\*|g" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 10M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 10M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0666/g"
/etc/php5/fpm/pool.d/www.conf  
  
# Download WordPress CLI  
RUN curl -L "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar" > /usr/local/bin/wp && \  
chmod +x /usr/local/bin/wp  
  
# Install Wordpress Site  
RUN ${WP_CLI} core download  
RUN ${WP_CLI} core config --dbname=wordpress --dbuser=wordpress
--dbpass=wordpress --skip-check  
  
RUN curl -o sqlite-plugin.zip https://downloads.wordpress.org/plugin/sqlite-
integration.1.8.1.zip  
RUN unzip sqlite-plugin.zip -d ${DOCUMENT_ROOT}/wp-content/plugins/  
RUN rm sqlite-plugin.zip  
RUN cp ${DOCUMENT_ROOT}/wp-content/plugins/sqlite-integration/db.php
${DOCUMENT_ROOT}/wp-content  
RUN cp ${DOCUMENT_ROOT}/wp-config-sample.php ${DOCUMENT_ROOT}/wp-config.php  
  
# Add Wordpress Theme & Plugins  
ADD wordpress-config/themes/ ${DOCUMENT_ROOT}/wp-content/themes  
ADD wordpress-config/plugins/ ${DOCUMENT_ROOT}/wp-content/plugins  
  
# ADD wordpress-config/uploads/ ${DOCUMENT_ROOT}/wp-content/uploads  
# Add robots.txt & sitemap  
ADD wordpress-config/robots.txt ${DOCUMENT_ROOT}/robots.txt  
ADD wordpress-config/sitemap.xml ${DOCUMENT_ROOT}/sitemap.xml  
  
#RUN chown -R www-data.www-data ${DOCUMENT_ROOT}  
COPY default /etc/nginx/sites-available/default  
RUN mkdir -p /etc/nginx/sites-enabled  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
  
# Wordpress Initialization and Startup Script  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/bin/bash", "/start.sh"]  

