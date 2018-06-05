FROM ubuntu:trusty  
MAINTAINER baor  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get update && apt-get -y install git nano curl apache2 libapache2-mod-
php5 mysql-server php5-mysql php5-mcrypt  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
RUN echo "Alias /icons/ /var/www/html/icons/" /etc/apache2.conf  
  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
RUN rm -rf /var/www/html  
  
RUN git clone https://github.com/baor/php-addressbook.git /var/www/html  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  
  

