FROM debian:jessie-slim  
  
RUN apt-get update && \  
apt-get install apache2 libapache2-mod-auth-cas -y && \  
rm -Rf /var/lib/apt/lists/*  
  
COPY auth_cas.conf /etc/apache2/mods-available/auth_cas.conf  
COPY default-site.conf /etc/apache2/sites-available/default.conf  
COPY httpd-foreground /usr/local/bin/httpd-foreground  
  
RUN a2enmod auth_cas && \  
a2enmod authz_groupfile && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2ensite default && \  
a2dissite 000-default  
  
EXPOSE 80  
CMD ["/usr/sbin/apachectl", "-d", "/etc/apache2", "-f", "apache2.conf", "-e",
"info", "-DFOREGROUND"]  

