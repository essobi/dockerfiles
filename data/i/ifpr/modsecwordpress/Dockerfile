FROM wordpress  
  
# install and configure modsecurity  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libapache2-mod-security2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mv /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf  
RUN sed -i "s/SecRuleEngine DetectionOnly/SecRuleEngine On/"
/etc/modsecurity/modsecurity.conf  
RUN sed -i "s/SecResponseBodyAccess On/SecResponseBodyAccess Off/"
/etc/modsecurity/modsecurity.conf  
  
RUN a2enmod security2  
  
#copy and config OWASP rules  
COPY owasp-modsecurity-crs/ /etc/modsecurity-crs  
COPY modsecurity.conf /etc/apache2/conf-enabled/  
COPY owasp-modsecurity-crs/modsecurity_crs_10_setup.conf.example
/etc/modsecurity-crs/modsecurity_crs_10_config.conf  
COPY whitelist.conf /etc/httpd/modsecuirty.d/whitelist.conf  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.5.2  
ENV WORDPRESS_SHA1 bab94003a5d2285f6ae76407e7b1bbb75382c36e  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]

