FROM simplific/nginx-php  
  
ENV WORDPRESS_VERSION 4.4.2  
ADD files/01-wordpress.conf /etc/nginx/conf.d/01-wordpress.conf  
ADD files/php.ini /etc/php/php.ini  
ADD files/nginx.conf /etc/nginx/nginx.conf  
  
RUN apk --no-cache --update add curl tar php-dom \  
&& curl -L "https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz" -o
"wp.tar.gz" \  
&& mkdir -p /opt/ \  
&& tar -xzf "wp.tar.gz" -C "/opt/" \  
&& rm wp.tar.gz \  
&& chown -R nginx:www-data /opt/wordpress  
  
VOLUME "/opt/wordpress/"  

