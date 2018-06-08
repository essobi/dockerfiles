############################################################  
# Dockerfile to build a Oxwall Social Media server  
# Based on appcontainers/centos66  
############################################################  
  
# Set the base image to Centos 6.6 Base  
FROM appcontainers/centos66  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@appcontainers.com  
  
#*************************  
#* Versions *  
#*************************  
ENV OXVER oxwall-1.7.2  
  
  
#**********************************  
#* Override Enabled ENV Variables *  
#**********************************  
ENV APP_NAME oxwall.local  
ENV APACHE_SVRALIAS www.oxwall.local localhost  
ENV MYSQL_SERVER localhost  
ENV MYSQL_PASS P@ssw0rd  
ENV MYSQL_DB oxwall  
ENV APP_USER admin  
ENV APP_PASS P@ssw0rd  
  
  
  
#*************************  
#* Update and Pre-Reqs *  
#*************************  
RUN yum clean all && \  
yum -y update && \  
yum -y install httpd mod_rewrite mod_ssl mod_env php php-common php-cli php-
mysql php-mbstring php-mcrypt php-gd mysql mysql-server gd unzip memcached &&
\  
rm -fr /var/cache/*  
  
  
#**************************  
#* Add Required Files *  
#**************************  
ADD $OXVER.zip /var/www/html/  
ADD runconfig.sh /tmp/  
ADD mysql_setup.sql /tmp/  
ADD oxwall.conf /etc/httpd/conf.d/  
  
  
#*************************  
#* Application Install *  
#*************************  
RUN mkdir /var/www/html/oxwall && \  
unzip /var/www/html/$OXVER.zip -d /var/www/html/oxwall/  
  
  
#************************  
#* Post Deploy Clean Up *  
#************************  
  
  
  
#**************************  
#* Config Startup Items *  
#**************************  
RUN chmod +x /tmp/runconfig.sh && \  
echo "/tmp/./runconfig.sh" >> ~/.bashrc  
  
CMD /bin/bash  
  
#****************************  
#* Expose Applicatoin Ports *  
#****************************  
# Expose ports to other containers only  
EXPOSE 80  
EXPOSE 443  

