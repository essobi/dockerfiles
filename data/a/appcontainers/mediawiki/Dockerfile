############################################################  
# Dockerfile to build MediaWiki server  
# Based on appcontainers/centos  
# DATE: 12/29/2015  
# COPYRIGHT: Appcontainers.com  
############################################################  
  
# Set the base image to Centos 6.6 Base  
FROM appcontainers/apache:debian  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@appcontainers.com  
  
###################################################################  
#************************* Reset Apache CTN *********************  
###################################################################  
  
# CENTOS  
# This section will handle undoing any install magic that the apache base
container did on setup.  
RUN rm -fr /etc/apache2/sites-available/apache_deb.conf && \  
rm -fr /var/www/*; mkdir -p /var/www/html && \  
rm -fr /tmp/install.log && \  
chown -R www-data:www-data /var/www/html && \  
ls -lah /var/www  
  
###################################################################  
#************************* APP VERSIONS *************************  
###################################################################  
  
ENV WIKIVER mediawiki-1.26.3  
  
###################################################################  
#*************** OVERRIDE ENABLED ENV VARIABLES *****************  
###################################################################  
  
ENV ENV dev  
ENV TERMTAG mediawiki  
ENV MODE standalone  
ENV APP_NAME mediawiki.local  
ENV APACHE_SVRALIAS www.mediawiki.local localhost  
ENV MYSQL_SERVER localhost  
ENV MYSQL_CLIENT localhost  
ENV MYSQL_USER root  
ENV MYSQL_PASS PAssw0rd  
ENV MYSQL_DB mediawiki  
ENV APP_USER admin  
ENV APP_PASS PAssw0rd  
  
###################################################################  
#****************** ADD REQUIRED APP FILES **********************  
###################################################################  
  
ADD apache_deb.conf /etc/apache2/sites-available/  
  
###################################################################  
#******************* UPDATES & PRE-REQS *************************  
###################################################################  
  
RUN apt-get clean all && \  
apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install wget tar php5 php5-cli
php5-common php5-mysql mysql-client-5.5 mysql-common mysql-server-5.5 unzip
wget && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/*  
  
# Remove locales other than english  
RUN for x in `ls /usr/share/locale | grep -v en_GB`; do rm -fr
/usr/share/locale/$x; done && \  
for x in `ls /usr/share/i18n/locales/ | grep -v en_`; do rm -fr
/usr/share/i18n/locales/$x; done  
  
# Enable the mod_env module and headers  
RUN a2enmod env ssl rewrite  
  
  
###################################################################  
#******************* APPLICATION INSTALL ************************  
###################################################################  
  
# Grab mediawiki and install it  
RUN cd /var/www/html/ && \  
wget https://releases.wikimedia.org/mediawiki/1.26/$WIKIVER.tar.gz && \  
tar -xzvf $WIKIVER.tar.gz && \  
rm *.tar.gz  
  
# Change the timezone  
RUN sed -i 's/;date.timezone\ \=/date.timezone\ \=\ \"America\/New_York\"/g'
/etc/php5/cli/php.ini  
  
###################################################################  
#****************** POST DEPLOY CLEAN UP ************************  
###################################################################  
  
# Ensure all services are stopped and fix ubuntu pid exists issue  
RUN service apache2 stop  
  
###################################################################  
#***************** CONFIGURE START ITEMS ************************  
###################################################################  
  
# Add Database Scripts, and Runconfig  
ADD runconfig.sh /tmp/.runconfig.sh  
ADD mysql_setup.sql /tmp/.mysql_setup.sql  
  
# Set boot items  
RUN chmod +x /tmp/.runconfig.sh && \  
echo "/tmp/./.runconfig.sh" >> ~/.bashrc && \  
echo "[ -f /tmp/.runconfig.sh ] && rm -fr /tmp/.runconfig.sh" >> /root/.bashrc  
  
# Set up Data Volume and Set docker run command.  
CMD /bin/bash -c "/tmp/.runconfig.sh && service apache2 stop &&
/usr/sbin/apache2ctl -D FOREGROUND"  
  
###################################################################  
#**************** EXPOSE APPLICATION PORTS **********************  
###################################################################  
# Expose ports to other containers only  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3306  
  
###################################################################  
#******************* OPTIONAL / LEGACY **************************  
###################################################################  

