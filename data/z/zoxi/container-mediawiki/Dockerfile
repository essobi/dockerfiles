# Builds docker image for mediawiki  
FROM zoxi/container-debian:latest  
  
MAINTAINER zoxi  
  
# Installation des dépendances et de Mediawiki  
ADD /scripts/install.sh /tmp/install.sh  
RUN chmod +x /tmp/*.sh && \  
/bin/bash /tmp/install.sh  
  
# Add supervisord conf  
ADD /scripts/start-apache2.sh /start-apache2.sh  
ADD /scripts/start-mysqld.sh /start-mysqld.sh  
RUN chmod +x /*.sh  
ADD /supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD /supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Config apache2  
ADD /apache/phpmyadmin.conf /etc/apache2/sites-available/phpmyadmin.conf  
ADD /apache/mediawiki.conf /etc/apache2/sites-available/mediawiki.conf  
#RUN a2ensite mediawiki  
# Environement apache2  
ENV APACHE_RUN_USER nobody  
ENV APACHE_RUN_GROUP users  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_SERVERADMIN admin@localhost  
  
# Volume  
VOLUME /config  
VOLUME /database  
  
# Ajout des droits  
RUN chown -R nobody:users /config  
RUN chown -R nobody:users /database  
  
# Port  
EXPOSE 80  
# Ajout du script de démarrage  
ADD /scripts/start.sh /start.sh  
RUN chmod +x /*.sh  
  
ENTRYPOINT ["/start.sh"]  

