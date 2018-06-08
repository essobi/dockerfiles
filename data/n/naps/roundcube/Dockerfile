FROM debian:wheezy  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install python python-jinja2 php5 php5-sqlite
php5-mcrypt \  
&& apt-get clean  
  
RUN rm -Rf /var/www/*  
  
ADD http://sourceforge.net/projects/roundcubemail/files/latest/download
/tmp/roundcube.tar.gz  
RUN tar xf /tmp/roundcube.tar.gz -C /var/www/ --strip-components=1  
  
RUN a2enmod deflate && a2enmod expires && a2enmod headers  
  
ADD config.inc.php /config.inc.php.tmpl  
  
RUN chmod 777 /var/www/logs/  
RUN mkdir /data && chmod 777 /data  
  
ADD launcher.py /  
RUN chmod +x /launcher.py  
  
EXPOSE 80  
VOLUME /var/www/logs  
VOLUME /data  
  
CMD []  
ENTRYPOINT ["/launcher.py"]  

