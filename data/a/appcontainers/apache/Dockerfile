############################################################  
# Dockerfile to build Apache Service Base Container  
# Based on: appcontainers/ubuntu:vivid  
# DATE: 05/06/2015  
# COPYRIGHT: Appcontainers.com  
############################################################  
  
# Set the base image in namespace/repo format.  
# To use repos that are not on the docker hub use the
example.com/namespace/repo format.  
FROM appcontainers/ubuntu  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@appcontainers.com  
  
###################################################################  
#************************* APP VERSIONS *************************  
###################################################################  
  
  
###################################################################  
#*************** OVERRIDE ENABLED ENV VARIABLES *****************  
###################################################################  
  
ENV TERMTAG APACHE  
ENV ENV dev  
ENV MODE standalone  
ENV APP_NAME apache.local  
ENV APACHE_SVRALIAS www.apache.local localhost  
  
###################################################################  
#****************** ADD REQUIRED APP FILES **********************  
###################################################################  
  
  
###################################################################  
#******************* UPDATES & PRE-REQS *************************  
###################################################################  
  
# Clean, Update, Upgrade, and Install... then clear non English local data.  
RUN apt-get clean && \  
apt-get update && \  
apt-get -y upgrade && \  
  
# Install required packages  
DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 php7.0 php7.0-cli
php7.0-common php7.0-mysql php7.0-xmlrpc perl imagemagick php7.0-pgsql && \  
  
# Remove apt list cache to preserve some space  
apt-get clean && \  
rm -fr /var/lib/apt/lists/*  
  
# Remove locales other than english  
RUN for x in `ls /usr/share/locale | grep -v en_GB`; do rm -fr
/usr/share/locale/$x; done && \  
for x in `ls /usr/share/i18n/locales/ | grep -v en_`; do rm -fr
/usr/share/i18n/locales/$x; done  
  
# Enable the mod_env module and headers  
RUN a2enmod env ssl rewrite && \  
ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/  
  
###################################################################  
#******************* APPLICATION INSTALL ************************  
###################################################################  
  
ADD apache_deb.conf /etc/apache2/sites-available/  
  
###################################################################  
#****************** POST DEPLOY CLEAN UP ************************  
###################################################################  
  
# Stop Apache as it starts on install  
RUN service apache2 stop  
  
###################################################################  
#***************** CONFIGURE START ITEMS ************************  
###################################################################  
  
# Add Database Scripts, and Runconfig  
ADD runconfig.sh /tmp/.runconfig.sh  
  
# Set boot items  
RUN chmod +x /tmp/.runconfig.sh && \  
echo "/tmp/./.runconfig.sh" >> /root/.bashrc && \  
echo "[ -f /tmp/.runconfig.sh ] && rm -fr /tmp/.runconfig.sh" >> /root/.bashrc  
  
CMD /bin/bash -c "/tmp/.runconfig.sh && service apache2 stop &&
/usr/sbin/apache2ctl -D FOREGROUND"  
  
###################################################################  
#**************** EXPOSE APPLICATION PORTS **********************  
###################################################################  
  
# Expose ports to other containers only  
EXPOSE 80  
EXPOSE 443  
  
###################################################################  
#******************* OPTIONAL / LEGACY **************************  
###################################################################  

