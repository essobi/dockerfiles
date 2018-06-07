# the debian wheezy image is needed to get apache 2.2 and because the httpd
image doesn't provide a2enmod etc.  
FROM debian:wheezy  
  
MAINTAINER datingcafe.de <dev@datingcafe.de>  
  
# Update repositories and install apache  
# After that remove apt status information  
RUN apt-get update && \  
apt-get install -y apache2 libapache2-mod-jk  
  
# configure env variables for apache  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# enable apache modules for communication between apache (mod_jk, for AJP)  
# and the Java VM in tomcat and for mod_rewrite  
RUN a2enmod rewrite \  
proxy \  
proxy_ajp \  
headers \  
jk  
  
#  
# enable modsecurity (including the Core Rule Set (CRS) of the OWASP)  
# see http://www.linuxquestions.org/questions/blog/rearden888-507430/howto-
set-up-modsecurity-on-debian-7-35569/  
#  
# install modsecurity and the CRS rules  
RUN apt-get install -y libapache2-modsecurity modsecurity-crs  
# activate and Load modsecurity-specific configuration  
RUN mv /etc/modsecurity/modsecurity.conf-recommended
/etc/modsecurity/modsecurity.conf  
# activate modsecurity rules  
RUN ln -s /usr/share/modsecurity-crs/modsecurity_crs_10_setup.conf
/etc/modsecurity/  
RUN cd /usr/share/modsecurity-crs/base_rules && \  
for f in * ; do ln -s /usr/share/modsecurity-crs/base_rules/$f
/etc/modsecurity/$f ; done  
RUN cd /usr/share/modsecurity-crs/optional_rules && \  
for f in * ; do ln -s /usr/share/modsecurity-crs/optional_rules/$f
/etc/modsecurity/$f ; done  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

