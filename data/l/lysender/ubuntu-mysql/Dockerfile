FROM ubuntu:wily  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install mysql-server \  
supervisor && apt-get clean  
  
ADD ./start.sh /start.sh  
ADD ./config_mysql.sh /config_mysql.sh  
ADD ./config_root_account.sh /config_root_account.sh  
ADD ./config_credentials.sh /config_credentials.sh  
ADD ./config_power_credentials.sh /config_power_credentials.sh  
RUN chmod 755 /*.sh  
  
RUN mkdir -p /etc/supervisor/conf.d  
ADD ./supervisor-mysql.conf /etc/supervisor/conf.d/mysql.conf  
  
# Configure MySQL  
# Allow external connections  
RUN sed -i 's/bind-address/#bind-address/g' /etc/mysql/mysql.conf.d/mysqld.cnf  
# Configure default DB  
RUN /config_mysql.sh  
  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  
  
EXPOSE 3306  
CMD ["/bin/bash", "/start.sh"]  
  

