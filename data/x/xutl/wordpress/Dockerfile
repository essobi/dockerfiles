FROM xutongle/php:7.1-nginx  
  
LABEL maintainer="xutongle@gmail.com"  
  
ARG WORDPRESS_VERSION  
  
# Environment settings  
ENV WORDPRESS_VERSION=${WORDPRESS_VERSION:-4.9.4}  
ENV
WORDPRESS_TGZ_URL=https://cn.wordpress.org/wordpress-${WORDPRESS_VERSION}-zh_CN.tar.gz  
RUN set -xe \  
&& mkdir -p /app \  
&& cd /root \  
&& curl -fSL ${WORDPRESS_TGZ_URL} -o
wordpress-${WORDPRESS_VERSION}-zh_CN.tar.gz \  
&& tar -xzvf wordpress-${WORDPRESS_VERSION}-zh_CN.tar.gz -C /app \--strip-
components=1 \  
&& rm -f wordpress-${WORDPRESS_VERSION}-zh_CN.tar.gz \  
&& rm -rf /app/wp-content/plugins/akismet \  
&& rm -f /app/wp-content/plugins/hello.php \  
&& chown -R www-data:www-data /app \  
&& rm -rf /usr/local/html \  
&& ln -s /app /usr/local/html  
  
VOLUME ["/app/wp-content/uploads"]  
  

