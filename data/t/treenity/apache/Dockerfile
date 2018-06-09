FROM debian:latest  
MAINTAINER Ronan Pozzi <contact@treenity-web.fr>  
  
RUN echo 'deb http://ftp.fr.debian.org/debian/ jessie non-free' >>
/etc/apt/sources.list  
RUN echo 'deb-src http://ftp.fr.debian.org/debian/ jessie non-free' >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install apache2 libapache2-mod-fastcgi  
  
RUN rm /etc/apache2/sites-enabled/*  
  
ADD conf-available /etc/apache2/conf-available  
ADD sites-available /etc/apache2/sites-available  
RUN a2enmod proxy proxy_fcgi rewrite \  
&& a2enconf servername \  
&& a2ensite 000-default  
  
RUN ln -sf /dev/stdout /var/log/apache2/access.log  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
EXPOSE 80 443  
VOLUME /var/www  
  
WORKDIR /var/www  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND

