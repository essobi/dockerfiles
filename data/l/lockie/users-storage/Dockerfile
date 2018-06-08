# based on osixia/docker-openldap  
# USAGE:  
# docker run -p 80 -p 389 -e LDAP_DOMAIN="test.com" \  
# -e LDAP_ORGANISATION="Acme widgets, inc." \  
# -e LDAP_ADMIN_PASSWORD="secret" \  
# -e LDAP_LOG_LEVEL=0 -d lockie/users-storage  
FROM phusion/baseimage:0.9.16  
MAINTAINER Andrew Kravchuk <awkravchuk@gmail.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# php-fpm package is required explicitly, see  
# https://lists.debian.org/debian-user/2015/06/msg00538.html  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y slapd nginx-light
php5-fpm ldap-account-manager && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini && \  
ln -sf /etc/nginx/sites-available/lam.conf /etc/nginx/sites-enabled/default  
  
ADD container-start.sh /etc/my_init.d/slapd  
ADD slapd.sh /etc/service/slapd/run  
ADD nginx.sh /etc/service/nginx/run  
ADD phpfpm.sh /etc/service/phpfpm/run  
ADD lam.conf /etc/nginx/sites-available/lam.conf  
  
# Set OpenLDAP data directory in a data volume  
VOLUME ["/var/lib/ldap"]  
  
EXPOSE 389 80  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

