FROM jamesmontalvo3/meza-docker-pre-yum:latest  
MAINTAINER James Montalvo  
ENV container=docker  
  
RUN git clone https://github.com/enterprisemediawiki/meza.git /opt/meza
--branch dev  
  
RUN yum -y install firewalld \  
&& systemctl start firewalld \  
&& firewall-cmd --permanent --zone=public --change-interface=docker0  
  
RUN bash /opt/meza/scripts/getmeza.sh  
  
RUN fqdn=INSERT_FQDN db_pass=1234 email=false private_net_zone=public meza
setup env monolith  
  
RUN meza install monolith  

