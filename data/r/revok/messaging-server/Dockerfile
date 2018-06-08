FROM alectolytic/activemq:latest  
MAINTAINER "Arun Neelicattu" <arun.neelicattu@gmail.com>  
  
USER root  
RUN yum -y update && yum -y clean all  
  
ADD assets/activemq.xml ${ACTIVEMQ_CONF}/activemq.xml  
  
USER ${ACTIVEMQ_USER}  

