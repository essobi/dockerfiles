# Unbound DNS Server  
FROM centos:centos7  
MAINTAINER Warren Baker <warren@percol8.co.za>  
  
RUN yum -y install unbound  
COPY run-unbound.sh /run-unbound.sh  
  
EXPOSE 53  
CMD [ "/run-unbound.sh" ]  

