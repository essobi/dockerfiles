FROM centos:6  
RUN set -ex; \  
yum -y update; \  
yum -y install httpd php php-mbstring php-mysql php-gd php-xml  
  
ENV WORDPRESS_VERSION 4.9.5  
ENV WORDPRESS_SHA1 6992f19163e21720b5693bed71ffe1ab17a4533a  
  
RUN set -ex; \  
curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
tar -xzf wordpress.tar.gz -C /usr/src/; \  
rm -f wordpress.tar.gz  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]  
  

