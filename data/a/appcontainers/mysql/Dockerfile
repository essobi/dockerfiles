############################################################  
# Dockerfile to build MySQL Base Container  
# Based on: appcontainers/ubuntu  
# DATE: 08/31/2015  
# COPYRIGHT: Appcontainers.com  
############################################################  
# Set the base image to Debian Base  
FROM appcontainers/ubuntu  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@appcontainers.com  
  
###################################################################  
#************************* APP VERSIONS *************************  
###################################################################  
###################################################################  
#*************** OVERRIDE ENABLED ENV VARIABLES *****************  
###################################################################  
  
ENV ENV dev  
ENV TERMTAG MYSQL  
ENV MYSQL_USER root  
ENV MYSQL_PASS PAssw0rd  
ENV MYSQL_CLIENT 172.17.%.%  
ENV CREATEDB false  
ENV MYSQL_DB testapp  
ENV APP_USER testuser  
ENV APP_PASS testpass  
  
###################################################################  
#****************** ADD REQUIRED APP FILES **********************  
###################################################################  
  
ADD runconfig.sh /tmp/.runconfig.sh  
ADD mysql_setup.sql /tmp/.mysql_setup.sql  
ADD mysql_remote.sql /tmp/.mysql_remote.sql  
  
###################################################################  
#******************* UPDATES & PRE-REQS *************************  
###################################################################  
  
RUN apt-get clean all && \  
apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install sudo mysql-client-5.7 mysql-
common mysql-server-5.7 && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* && \  
sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/mysql.conf.d/mysqld.cnf  
  
# Remove locales other than english  
RUN for x in `ls /usr/share/locale | grep -v en_GB`; do rm -fr
/usr/share/locale/$x; done && \  
for x in `ls /usr/share/i18n/locales/ | grep -v en_`; do rm -fr
/usr/share/i18n/locales/$x; done  
  
###################################################################  
#******************* APPLICATION INSTALL ************************  
###################################################################  
###################################################################  
#****************** POST DEPLOY CLEAN UP ************************  
###################################################################  
# Debian based distros start mysql automatically.. this breaks /var/lib/ on a
persistent container, so..  
RUN rm -fr /var/lib/mysql  
  
# Debian based distros set my.cnf to listen on localhost 127.0.0.1.. change
that to all interfaces  
RUN sed -i 's/127.0.0.1/*/g' /etc/mysql/my.cnf  
  
###################################################################  
#***************** CONFIGURE START ITEMS ************************  
###################################################################  
  
RUN chmod +x /tmp/.runconfig.sh && \  
echo "/tmp/./.runconfig.sh" >> ~/.bashrc && \  
echo "[ -f /tmp/.runconfig.sh ] && rm -fr /tmp/.runconfig.sh" >> /root/.bashrc  
  
CMD /bin/bash -c "/tmp/.runconfig.sh && service mysql stop &&
/usr/bin/mysqld_safe"  
  
###################################################################  
#**************** EXPOSE APPLICATION PORTS **********************  
###################################################################  
# Expose ports to other containers only  
  
EXPOSE 3306  
  
###################################################################  
#******************* OPTIONAL / LEGACY **************************  
###################################################################  

