FROM phusion/baseimage:0.9.22  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SELF_SERVICE_PASSWORD_VERSION 1.1-1  
# Install Apache2, PHP and LTB ssp  
RUN apt-get update && apt-get install -y apache2 libapache2-mod-php php php-
mcrypt php-ldap php-mbstring php-xml && apt-get clean  
RUN curl -L https://ltb-project.org/archives/self-service-
password_${SELF_SERVICE_PASSWORD_VERSION}_all.deb > self-service-password.deb
&& dpkg -i self-service-password.deb ; rm -f self-service-password.deb  
  
# Configure self-service-password site  
#RUN ln -s ../../mods-available/mcrypt.ini
/etc/php5/apache2/conf.d/20-mcrypt.ini  
RUN a2dissite 000-default && a2ensite self-service-password  
  
# This is where configuration goes  
ADD assets/config.inc.php /usr/share/self-service-password/conf/config.inc.php  
  
# Start Apache2 as runit service  
RUN mkdir /etc/service/apache2  
ADD assets/apache2.sh /etc/service/apache2/run  
  
# Run adding self signed certificates to system  
ADD assets/ca.sh /etc/my_init.d/ca.sh  
  
EXPOSE 80  

