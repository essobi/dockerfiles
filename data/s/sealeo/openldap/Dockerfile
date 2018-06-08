FROM debian:8.2  
LABEL maintainer="Pierre GUINAULT <speed@sealeo.org>, Alexis PEREDA
<celforyon@sealeo.org>"  
  
RUN apt-get update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install --no-install-
recommends --no-install-suggests -y \  
slapd \  
apt-utils \  
supervisor \  
wget \  
phpldapadmin \  
ldap-utils \  
vim \  
courier-ldap \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LDAP_PASSWORD password  
ENV LDAP_ORGANISATION Inc.  
ENV LDAP_DOMAIN_BASE example.com  
ENV LDAP_SERVERNAME "My LDAP server"  
ENV LDAP_SSL 1  
EXPOSE 80  
EXPOSE 389  
EXPOSE 636  
VOLUME ["/etc/ldap/slapd.d", "/var/lib/ldap", "/ssl"]  
  
COPY ./files /  
  
RUN sed -i 's/\/var\/www\/html/\/usr\/share\/phpldapadmin\/htdocs/'
/etc/apache2/sites-available/000-default.conf  
  
CMD ["/usr/bin/supervisord", "-c/etc/supervisord.conf"]  

