FROM iitgdocker/apache:2.4.6  
MAINTAINER "The Ignorant IT Guy" <iitg@gmail.com>  
  
COPY epel.repo /etc/yum.repos.d/epel.repo  
COPY remi.repo /etc/yum.repos.d/remi.repo  
  
RUN yum -y --nogpgcheck install \  
php \  
php-suhosin && \  
yum clean all  
  
# Make sure /var/www/html knows who's boss.  
RUN chown -R apache:apache /var/www/html  
  
EXPOSE 80  
EXPOSE 443  
COPY php.sh /php.sh  
RUN chmod +x /php.sh  
CMD ["/php.sh"]  

