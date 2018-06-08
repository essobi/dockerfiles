FROM php:5.6-cli  
  
MAINTAINER Soren Media Group "inquiries@sorenmediagroup.com"  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
VOLUME /var/www/html  
  
# install nginx  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.9.0-1~jessie  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
# install hhvm  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update  
RUN apt-get install -y hhvm  
  
# configure hhvm  
RUN /usr/share/hhvm/install_fastcgi.sh  
RUN update-rc.d hhvm defaults  
RUN service hhvm restart  
RUN /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60  
  
# install wp-cli  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar  
RUN chmod +x wp-cli.phar  
RUN mv wp-cli.phar /usr/local/bin/wp  
  
# configure nginx for wp  
ADD ./nginx-site.conf /etc/nginx/sites-available/default  
  
# create file structure for wp  
RUN cd /usr/share/nginx/www  
RUN mkdir app  
RUN mkdir extensions  
RUN mkdir config  
  
# install wp  
ENV WORDPRESS_VERSION 4.2.2  
ENV WORDPRESS_UPSTREAM_VERSION 4.2.2  
ENV WORDPRESS_SHA1 d3a70d0f116e6afea5b850f793a81a97d2115039  
  
RUN curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_UPSTREAM_VERSION}.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/share/nginx/www/app \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data /usr/share/nginx/www/app  
  
# configure wp  
ADD index.php /usr/share/nginx/www  
ADD wp-config.php /usr/share/nginx/www  
RUN cd /usr/share/nginx/www  
RUN wp core install  
  
# add extensions  
RUN wp plugin install all-in-one-event-calendar --version 2.2.1  
RUN wp plugin install amazon-web-services --version 0.2.2  
RUN wp plugin install amazon-s3-and-cloudfront --version 0.8.2  
RUN wp plugin install better-notifications-for-wordpress --version 1.2  
RUN wp plugin install broken-link-checker --version 1.10.8  
RUN wp plguin install caldera-forms --version 1.2.0  
RUN wp plguin install contact-form-db --version 2.8.38  
RUN wp plugin install custom-dashboard-help --version 3.0  
RUN wp plugin install disqus-comment-system --version 2.84  
RUN wp plugin install email-post-changes --version 1.7.1  
RUN wp plugin install google-analytics-dashboard-for-wp --version 4.7.3  
RUN wp plugin install hello-dolly --version 1.6  
RUN wp plguin install image-widget --version 4.1  
RUN wp plugin install mailchimp-for-wordpress-lite --version 2.3.2  
RUN wp plugin install meta-slider --version 3.3.2  
RUN wp plugin install plugin-organizer --version 6.0.4  
RUN wp plugin install post-types-order --version 1.7.9  
RUN wp plugin install simple-staff-list --version 1.16  
RUN wp plugin install social-media-feather --version 1.7.8  
RUN wp plugin install updraftplus-backup-and-restoration --version 1.10.1  
RUN wp plugin install user-role-editor --version 4.18.4  
RUN wp plugin install velvet-blues-update-urls --version 3.2.3  
RUN wp plugin install wordfence-security --version 6.0.3  
RUN wp plugin install wordpress-seo --version 2.1.1  
RUN wp plugin install wpmandrill --version 1.33  
  
# additional configuration  
COPY docker-entrypoint.sh/entrypoint.sh  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3306  
# entrypoint  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/bin/bash"]

