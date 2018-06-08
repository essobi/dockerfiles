FROM ubuntu:14.04  
MAINTAINER "Thomas Helander" <thomas.helander@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -yq && \  
apt-get install -yq software-properties-common && \  
apt-get dist-upgrade -yq && \  
add-apt-repository cloud-archive:liberty && \  
apt-get update -yq  
  
RUN apt-get install -yq python-openstackclient mariadb-client crudini  
  
RUN apt-get install -yq glance python-glanceclient  
  
VOLUME [ "/var/lib/glance/images/", "/var/log/glance" ]  
  
EXPOSE 9292  
COPY docker-entrypoint.sh /  
CMD [ "/docker-entrypoint.sh" ]  

