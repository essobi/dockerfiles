FROM ubuntu:latest  
MAINTAINER Artistan <karl.tobias@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
# Update and Upgrade Packages  
RUN apt-get update && apt-get upgrade -y && apt-get clean  
  
# SSH Server  
RUN apt-get install -y openssh-server  
  
# NGINX  
RUN apt-get install -y nginx  
  
# PHP5  
RUN apt-get install -y php7.0 php7.0-cgi php7.0-cli php7.0-common php7.0-fpm
php7.0-gd php7.0-json php7.0-ldap php7.0-mbstring php7.0-mcrypt php7.0-mysql
php7.0-opcache php7.0-snmp php7.0-tidy php7.0-xml php7.0-xmlrpc php7.0-xsl
php7.0-zip  
  
# Configs  
ADD default /etc/nginx/sites-enabled/default  
  
RUN sed -i '1i daemon off;' /etc/nginx/nginx.conf  
RUN sed -i '/;cgi.fix_pathinfo=1/c cgi.fix_pathinfo=0'
/etc/php/7.0/fpm/php.ini  
  
RUN mkdir /etc/nginx.default /etc/php.default /var/www.default  
  
RUN cp -rp /etc/nginx/* /etc/nginx.default  
RUN cp -rp /etc/php/* /etc/php.default  
RUN cp -rp /var/www/* /var/www.default  
  
# Cleaning  
RUN apt-get clean  
  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
CMD ["/usr/local/bin/run.sh"]  

