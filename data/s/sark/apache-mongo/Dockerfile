FROM sark/apache-php  
MAINTAINER Robin <robin@naas.io>  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
php5-mongo \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /var/www  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

