FROM osixia/openldap  
MAINTAINER developers@khipu.com  
  
RUN groupmod -g 2000 openldap && \  
usermod -u 2000 -g 2000 openldap && \  
chown openldap:openldap /run/slapd  
  
ADD daemon.sh /container/service/slapd/daemon.sh  

