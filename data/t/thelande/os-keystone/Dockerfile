FROM ubuntu:14.04  
MAINTAINER "Thomas Helander" <thomas.helander@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -yq && \  
apt-get install -yq software-properties-common && \  
apt-get dist-upgrade -yq && \  
add-apt-repository cloud-archive:liberty && \  
apt-get update -yq  
  
RUN apt-get install -yq python-openstackclient keystone apache2 \  
libapache2-mod-wsgi memcached python-memcache crudini mariadb-client  
  
EXPOSE 5000 35357  
VOLUME [ "/root", "/var/log/apache" ]  
  
COPY wsgi-keystone.conf /etc/apache2/sites-available/wsgi-keystone.conf  
COPY docker-entrypoint.sh /  
CMD [ "/docker-entrypoint.sh" ]  

