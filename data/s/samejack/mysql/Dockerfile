FROM ubuntu:14.04.4  
MAINTAINER SJ Chou <sj@toright.com>  
  
# Install package  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y  
RUN apt-get -y install mysql-server libpwquality-tools  
  
RUN apt-get remove \--purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
ADD conf/start.sh /  
ADD conf/init.sh /  
ADD conf/mysql_init.sql /  
ADD conf/my.cnf /  
RUN chmod +x /start.sh && chmod +x /init.sh  
  
# Expose Ports  
EXPOSE 3306  
  
CMD ["/start.sh"]  

