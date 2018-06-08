FROM debian:jessie  
MAINTAINER Robin <robin@naas.io>  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
apache2 \  
munin \  
libapache2-mod-fcgid  
&& rm -rf /var/lib/apt/lists/* \  
&& a2enmod rewrite \  
&& a2enmod fcgid  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

