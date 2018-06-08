# @EdT Asix-M11 Curs 17-18  
# ldapserver:dataDB  
# servidor ldap creacio interactiu  
# ---------------------------------  
FROM fedora:24  
MAINTAINER isx41745190@EdT "edt asix-m11 curs 17-18"  
RUN dnf -y update vi  
RUN dnf -y install vim procps iputils iproute tree nmap \  
openldap openldap-clients openldap-servers \  
mlocate man-db  
RUN mkdir /opt/docker  
COPY * /opt/docker/  
COPY ldap.conf /etc/openldap/  
RUN chmod +x /opt/docker/install.sh /opt/docker/startup.sh  
RUN /opt/docker/install.sh  
WORKDIR /opt/docker  
CMD ["/opt/docker/startup.sh"]  

