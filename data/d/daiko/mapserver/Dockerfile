FROM daiko/debianfr  
MAINTAINER Florestan Bredow <florestan.bredow@daiko.fr>  
MAINTAINER Amandine Sahl <amandine.sahl@gmail.com>  
  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list \  
&& apt-get update && apt-get -y install \  
apache2 \  
cgi-mapserver libapache2-mod-fcgid \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod fcgid  
  
RUN rm /etc/apache2/sites-available/000-default.conf  
COPY conf/apache2.conf /etc/apache2/sites-available/000-default.conf  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

