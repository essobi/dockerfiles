FROM bitnami/minideb-extras:stretch  
  
#RUN sed -i 's/deb.debian.org/mirror.ox.ac.uk/' /etc/apt/sources.list  
ARG DEBIAN_FRONTEND=noninteractive  
  
# for certbot  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >
/etc/apt/sources.list.d/backports.list  
  
RUN apt-get update && apt-get install -y php7.0 php7.0-xsl php7.0-pgsql
php7.0-ldap php7.0-gd apache2 wget postgresql-client libapache2-mod-shib2 php-
yaml certbot  
#ENV comanage_version 3.1.0-rc2  
#RUN wget https://github.com/Internet2/comanage-
registry/archive/${comanage_version}.tar.gz && \  
# tar xf ${comanage_version}.tar.gz && \  
# mv comanage-registry-${comanage_version} /srv/comanage && \  
# rm ${comanage_version}.tar.gz  
ADD net.cshoskin.comanage-inputs.json net.cshoskin.comanage-inputs.json  
ADD app-entrypoint.sh app-entrypoint.sh  
RUN chmod a+x /app-entrypoint.sh  
ADD nami nami  
#Unpack when we build, as we want to initialize when the package is run  
RUN nami unpack ./nami/  
RUN ln -s /opt/bitnami/net.cshoskin.comanage /srv/comanage  
  
RUN ln -s /srv/comanage/app/webroot /var/www/html/registry  
ADD comanage80.conf /etc/apache2/sites-available/  
ADD comanage443.conf /etc/apache2/sites-available/  
RUN a2dissite 000-default  
RUN a2ensite comanage80  
RUN a2ensite comanage443  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2enmod shib2  
  
#  
RUN cp -r /srv/comanage/app/tmp.dist /var/cache/registry  
RUN chown -R www-data /var/cache/registry  
RUN chmod 700 /var/cache/registry  
RUN ln -s /var/cache/registry /srv/comanage/local/tmp  
  
ADD database.php /srv/comanage/local/Config/database.php  
ADD email.php /srv/comanage/local/Config/email.php  
  
ADD start.sh /srv/comanage/local/  
RUN chmod a+x /srv/comanage/local/start.sh  
  
RUN ln -s /srv/comanage/app/AvailablePlugin/FileSource
/srv/comanage/local/Plugin/FileSource  
RUN ln -s /srv/comanage/app/AvailablePlugin/LdapSource
/srv/comanage/local/Plugin/LdapSource  
  
RUN mkdir /etc/comanage/  
RUN mv /etc/shibboleth/shibboleth2.xml /etc/comanage/  
RUN ln -s /etc/comanage/shibboleth2.xml /etc/shibboleth/shibboleth2.xml  
  
EXPOSE 80  
EXPOSE 443  
#ENV DB_PASSWORD="comanage"  
ENTRYPOINT ["/app-entrypoint.sh"]  
CMD ["nami","start"]  
  

