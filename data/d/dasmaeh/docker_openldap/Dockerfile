FROM osixia/openldap  
MAINTAINER Jan Köster <dasmaeh@cbjck.de>  
  
ADD startup.sh /container/service/slapd/startup.sh  
RUN rm -rf
/container/service/slapd/assets/config/bootstrap/schema/mmc/dhcp.schema  
RUN rm -rf
/container/service/slapd/assets/config/bootstrap/schema/mmc/dnszone.schema  
RUN rm -rf
/container/service/slapd/assets/config/bootstrap/schema/mmc/mmc.schema  
RUN rm -rf
/container/service/slapd/assets/config/bootstrap/schema/mmc/openssh-lpk.schema  
RUN rm -rf
/container/service/slapd/assets/config/bootstrap/schema/mmc/samba.schema  
RUN rm -rf
/container/service/slapd/assets/config/bootstrap/schema/mmc/zarafa.schema  
ADD bootstrap /container/service/slapd/assets/config/bootstrap  

