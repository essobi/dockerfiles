############################################################  
# Dockerfile to build Self Contained Wordpress Container  
# Based on appcontainers/centos66  
############################################################  
  
# Set the base image to Centos 6.6 Base  
FROM tobkle/centos66  
  
# File Author / Maintainer  
MAINTAINER Tobias Klemmer tobias@klemmer.info  
  
#**********************************  
#* Override Enabled ENV Variables *  
#**********************************  
ENV ENV dev  
ENV TERMTAG wordpress  
ENV MODE standalone  
ENV APP_NAME wordpress.local  
ENV APACHE_SVRALIAS www.wordpress.local localhost  
ENV MYSQL_SERVER localhost  
ENV MYSQL_CLIENT localhost  
ENV MYSQL_USER root  
ENV MYSQL_PASS PAssw0rd  
ENV MYSQL_DB wordpress  
ENV APP_USER admin  
ENV APP_PASS PAssw0rd  
ENV WP_KEY "Check us out at www.klemmer.info"  
  
#*************************  
#* Update and Pre-Reqs *  
#*************************  
RUN yum clean all && \  
yum -y update && \  
yum -y install httpd mod_rewrite mod_ssl mod_env php php-common php-cli php-
mysql mysql mysql-server unzip && \  
yum clean all && \  
rm -fr /var/cache/* && \  
  
# Remove locales other than english  
cd /usr/share/locale/ && \  
for x in `ls | grep -v -i en | grep -v -i local`;do rm -fr '$x'; done && \  
rm -fr ca* den men wen zen && \  
cd /usr/lib/locale && \  
localedef --list-archive | grep -v -i ^en | xargs localedef --delete-from-
archive && \  
mv -f locale-archive locale-archive.tmpl && \  
build-locale-archive  
  
#**************************  
#* Get Wordpress  
#**************************  
RUN wget -P /var/www/html/ https://wordpress.org/latest.zip && \  
unzip /var/www/html/latest.zip -d /var/www/html/ && \  
rm -fr /var/www/html/latest.zip && \  
cp /var/www/html/wordpress/wp-config-sample.php /var/www/html/wordpress/wp-
config.php  
  
#**************************  
#* Add Startup Files *  
#**************************  
ADD runconfig.sh /tmp/runconfig.sh  
ADD mysql_setup.sql /tmp/mysql_setup.sql  
ADD mysql_grant_privilege.sql /tmp/mysql_grant_privilege.sql  
ADD wordpress.conf /tmp/wordpress.conf  
  
#**************************  
#* Config Startup Items *  
#**************************  
RUN chmod +x /tmp/runconfig.sh && \  
echo "/tmp/runconfig.sh" >> ~/.bashrc && \  
echo "rm -fr /tmp/runconfig.sh" >> ~/.bashrc  
  
# Set up Data Volume and Set docker run command.  
CMD /bin/bash  
  
#****************************  
#* Expose Application Ports *  
#****************************  
# Expose ports to other containers only  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3306  

