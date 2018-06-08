FROM debian:wheezy  
MAINTAINER Robin <robin@naas.io>  
  
# add Dotdeb mirror https://www.dotdeb.org/  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 89DF5277 \  
&& echo "deb http://packages.dotdeb.org wheezy all" >
/etc/apt/sources.list.d/dotdeb.list \  
&& echo "deb http://packages.dotdeb.org wheezy-php55 all" >>
/etc/apt/sources.list.d/dotdeb.list  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
libapache2-mod-php5 \  
&& rm -rf /var/lib/apt/lists/* \  
&& a2enmod rewrite \  
&& a2enmod php5  
  
VOLUME /var/www  
  
COPY config/default /etc/apache2/sites-available/default  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

