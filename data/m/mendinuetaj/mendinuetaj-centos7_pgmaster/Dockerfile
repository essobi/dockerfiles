FROM centos:centos7  
MAINTAINER Jose Luis Mendinueta  
  
#Descargar todo el software necesario  
#------------------------------------  
RUN yum -y update; yum clean all  
RUN yum -y install sudo epel-release wget ; yum clean all;  
RUN wget
https://download.postgresql.org/pub/repos/yum/9.2/redhat/rhel-7-x86_64/pgdg-
centos92-9.2-3.noarch.rpm  
RUN rpm -Uhv pgdg-centos92-9.2-3.noarch.rpm ; yum clean all  
RUN yum -y install vim postgresql92-server postgresql92-contrib sudo repmgr92
openssh-server supervisor rsync openssh-clients net-tools ; yum clean all  
RUN passwd --delete root  
  
#Iniciador de la base de datos  
COPY ./postgresql-setup /usr/bin/postgresql-setup  
  
#Manejador de servicios  
COPY ./supervisord.conf /etc/supervisord.conf  
  
#Archivos de configuracion modificados  
#-------------------------------------  
#Postgres  
COPY ./postgresql.conf /postgresql.conf  
COPY ./pg_hba.conf /pg_hba.conf  
  
#SSH  
COPY ./sshd_config /etc/ssh/sshd_config  
  
#Ejecutables  
#------------  
COPY ./start_postgres.sh /start_postgres.sh  
COPY ./repmgr_configurator.sh /repmgr_configurator.sh  
  
#Estableciendo permisos de ejecucion  
RUN chmod +x /start_postgres.sh  
RUN chmod +x /usr/bin/postgresql-setup  
RUN chmod +x /repmgr_configurator.sh  
  
CMD ["/bin/bash", "/repmgr_configurator.sh"]  
  

