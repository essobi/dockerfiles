FROM ubuntu:trusty  
MAINTAINER Giorgio Consorti <g.consorti@lynxlab.com>  
  
#Environment variables to configure app  
ENV APPLICATION_DIR fossa  
ENV APPLICATION_NAME "Fossa Project - Standards Inventory"  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://mirror.hosting90.cz/mariadb/repo/10.1/ubuntu trusty main' && \  
apt-get update && \  
apt-get -y install supervisor git apache2 libapache2-mod-php5 mariadb-server
php5-mysql pwgen php-apc php5-mcrypt && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
ADD support-files/ /support-files  
RUN chmod 755 /support-files/*.sh  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
EXPOSE 80  
CMD ["/run.sh"]  

