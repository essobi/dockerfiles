FROM osixia/openldap:1.1.6  
MAINTAINER Johan Smits  
  
ADD bootstrap /container/service/slapd/assets/config/bootstrap  
RUN rm /container/service/slapd/assets/config/bootstrap/schema/mmc/mail.schema  

