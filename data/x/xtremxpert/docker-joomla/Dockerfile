FROM xtremxpert/docker-phpapache:debian  
  
MAINTAINER Xtremxpert <xtremxpert@xtremxpert.com>  
  
ENV JOOMLA_VERSION="3.4.5" \  
JOOMLA_SHA1="098ce53f3bc44531be95c20a0faf7f80efe5fc88"  
RUN curl -o joomla.zip -SL https://github.com/joomla/joomla-
cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-
Full_Package.zip \  
&& echo "$JOOMLA_SHA1 *joomla.zip" | sha1sum -c - \  
&& unzip joomla.zip -d /var/www/html \  
&& rm joomla.zip \  
&& mv /var/www/html/htaccess.txt /var/www/html/.htaccess \  
&& rm /var/www/html/web.config.txt \  
&& rm /var/www/html/index.html \  
&& chown -R www-data:www-data /var/www/html  
  
EXPOSE 80 443  
VOLUME [/var/www/html]  
  
CMD ["/usr/bin/supervisord"]  

