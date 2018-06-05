FROM ubuntu  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN apt-get -y update && apt-get install -y subversion apache2 libapache2-mod-
svn libapache2-svn libsvn-dev  
RUN apt-get -y update && apt-get install -y cron  
RUN apt-get -y update && apt-get install -y python python-ldap  
RUN /usr/sbin/a2enmod dav  
RUN /usr/sbin/a2enmod dav_svn  
RUN /usr/sbin/a2enmod ldap  
RUN /usr/sbin/a2enmod authnz_ldap  
RUN service apache2 restart  
  
VOLUME /svn  
VOLUME /config  
VOLUME /etc/cron.d  
  
# Set permissions  
RUN addgroup subversion  
RUN usermod -a -G subversion www-data  
RUN chown -R www-data:subversion /svn  
RUN chmod -R g+rws /svn  
RUN touch /var/log/cron.log  
  
RUN echo "0 * * * * /config/scripts/cron.sh > /dev/null 2>&1" >> /etc/crontab  
  
COPY config/apache-default.conf /etc/apache2/sites-available/000-default.conf  
COPY script/ldap_to_authz.py /ldap_to_authz.py  
COPY script/start.sh /start.sh  
  
# Configure Apache to serve up Subversion  
RUN /usr/sbin/a2enmod auth_digest  
  
EXPOSE 80  
CMD ["/start.sh"]  

