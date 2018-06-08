# @isx47590131 projecte  
# isx47590131/radius:radiusserver  
# servivor radius mode debbug  
# --------------------------------  
FROM fedora:24  
MAINTAINER isx47590131 "@isx47590131 projecte"  
RUN dnf -y update vi  
RUN dnf -y install vim procps iputils iproute tree nmap mlocate man-db \  
freeradius-client freeradius freeradius-ldap freeradius-utils \  
freeradius-utils hostname openldap-clients  
RUN mkdir /opt/docker  
RUN rm /var/run/nologin  
ADD . /opt/docker/  
RUN chmod +x /opt/docker/startup.sh  
COPY clients.conf /etc/raddb/  
COPY default /etc/raddb/sites-enabled/  
COPY ldap /etc/raddb/mods-aviable/  
RUN ln -s /opt/docker/ldap /etc/raddb/mods-enabled/  
WORKDIR /opt/docker  
#CMD ["/usr/sbin/radiusd", "-d", "/etc/raddb"]  
CMD ["/opt/docker/startup.sh"]  
  

