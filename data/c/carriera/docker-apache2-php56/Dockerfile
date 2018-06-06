FROM antage/apache2-php5  
  
RUN DEBIAN_FRONTEND=noninteractive && apt-get -q -y --purge remove php5-common
php5 php5-curl php5-dbg php5-dev php5-gd php5-intl php5-json php5-mcrypt
php5-memcache php5-mongo php5-mysql php5-phalcon php5-xdebug php5-xmlrpc
php5-xsl  
  
RUN apt-get -y -q update \  
&& DEBIAN_FRONTEND=noninteractive && apt-get -y -q install php5 php5-curl
php5-dbg php5-dev php5-gd php5-intl php5-json php5-mcrypt php5-memcache
php5-mongo php5-mysqlnd php5-phalcon php5-xdebug php5-xmlrpc php5-xsl  
  
EXPOSE 8080  
  
#COPY apache2.conf /etc/apache2/apache2.conf-new  
#RUN rm -f /etc/apache2.conf && cp -f /etc/apache2/apache2.conf-new
/etc/apache2/apache2.conf  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["apache2"]  

