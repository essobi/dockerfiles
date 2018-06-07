FROM centos:6.6  
MAINTAINER "Jean Lalande" <jeanlalande@gmail.com>  
  
# largely based on dgraziotin/mysql and adapted to run on CentOS 6  
# MAINTAINER Daniel Graziotin <daniel@ineed.coffee>  
ENV DOCKER_USER_ID 501  
ENV DOCKER_USER_GID 20  
ENV BOOT2DOCKER_ID 1000  
ENV BOOT2DOCKER_GID 50  
# Tweaks to give MySQL write permissions to the app  
RUN useradd -r mysql -u ${BOOT2DOCKER_ID} && \  
usermod -G mysql mysql  
  
RUN groupmod -g $(($BOOT2DOCKER_GID \+ 10000)) $(getent group $BOOT2DOCKER_GID
| cut -d: -f1)  
RUN groupmod -g ${BOOT2DOCKER_GID} mysql  
  
# Install packages  
RUN yum -y install epel-release && yum -y update && \  
yum -y install wget git mysql-server pwgen zip unzip python-setuptools && \  
easy_install supervisor  
  
# Add image configuration and scripts  
ADD start-mysqld.sh /start-mysqld.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
RUN echo_supervisord_conf > /etc/supervisord.conf && \  
echo "[include]" >> /etc/supervisord.conf && \  
echo "files = /etc/supervisor/conf.d/*.conf" >> /etc/supervisord.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql  
  
# Add MySQL utils  
ADD create_mysql_users.sh /create_mysql_users.sh  
RUN chmod 755 /*.sh  
  
ENV MYSQL_PASS:-$(pwgen -s 12 1)  
  
# Add volumes for the app and MySql  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/run.sh"]  

