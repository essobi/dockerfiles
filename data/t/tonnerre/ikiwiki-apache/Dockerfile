FROM debian:testing  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN adduser --system --shell /bin/bash --gecos 'Git access' \  
\--home /var/lib/git --no-create-home --group --disabled-password git  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef \  
-o Dpkg::Options::=--force-confold --purge install apache2 apache2-utils \  
libapache2-mod-perl2 libapache2-mod-rpaf libxml-writer-perl ikiwiki  
RUN a2enmod auth_basic authn_core authnz_ldap authz_user cgi http2 ldap perl \  
rpaf ssl  
  
ADD ports.conf /etc/apache2/ports.conf  
ADD srv.conf /etc/apache2/conf-available/srv.conf  
ADD ldapca.conf /etc/apache2/conf-available/ldapca.conf  
  
ADD run-ikiwiki.sh /usr/local/bin/run-ikiwiki.sh  
RUN ["/usr/bin/chmod", "0555", "/usr/local/bin/run-ikiwiki.sh"]  
RUN ["/usr/bin/install", "-m", "0775", "-o", "www-data", "-g", "www-data", \  
"-d", "/var/log/apache2", "/run/apache2"]  
RUN ["/usr/bin/chown", "-R", "www-data:www-data", "/var/log/apache2", \  
"/run/apache2", "/etc/apache2/sites-available", \  
"/etc/apache2/sites-enabled", "/var/lib/apache2/site/enabled_by_admin"]  
  
RUN ["/usr/sbin/adduser", "git", "www-data"]  
RUN ["/usr/sbin/adduser", "www-data", "git"]  
  
RUN ["/usr/sbin/a2enconf", "srv"]  
RUN ["/usr/sbin/a2enconf", "ldapca"]  
  
USER www-data:git  
EXPOSE 8080/tcp 8443/tcp  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV LANG C  
  
VOLUME ["/secret", "/var/lib/git", "/srv/www", "/etc/ikiwiki",
"/etc/ldap/ssl"]  
ENTRYPOINT ["/usr/local/bin/run-ikiwiki.sh"]  

