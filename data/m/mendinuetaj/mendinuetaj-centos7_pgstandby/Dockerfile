FROM centos:centos7  
MAINTAINER Jose Luis Mendinueta  
  
#Descargar todo el software necesario  
#------------------------------------  
RUN yum -y update; yum clean all  
RUN yum -y install sudo epel-release wget; yum clean all  
RUN wget
https://download.postgresql.org/pub/repos/yum/9.2/redhat/rhel-7-x86_64/pgdg-
centos92-9.2-3.noarch.rpm  
RUN rpm -Uhv pgdg-centos92-9.2-3.noarch.rpm ; yum clean all  
RUN yum -y install vim postgresql92-server postgresql92-contrib repmgr92
supervisor rsync openssh-clients net-tools ; yum clean all  
  
#Configuracion  
#------------------------------------  
#Configurar la replicacion  
#------------------------------------  
#Ejecutar el script de configuracion  
ADD ./supervisord.conf /etc/supervisord.conf  
ADD ./repmgr_configurator.sh /repmgr_configurator.sh  
RUN chmod +x /repmgr_configurator.sh  
  
CMD ["/bin/bash", "/repmgr_configurator.sh"]  
  

