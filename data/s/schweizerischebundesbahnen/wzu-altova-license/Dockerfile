FROM schweizerischebundesbahnen/wzu-base8  
MAINTAINER Team Werkzeugunterstützung <mwe@sbb.ch>  
  
# Product  
  
ARG product=altovalicenseserver  
ENV PRODUCT ${product}  
# Ports  
  
ARG ports="8088 35355"  
ENV PORTS ${ports}  
# Add ansible  
ADD ansible /tmp/ansible  
  
# Run ansible-config  
RUN ansible-playbook -vvv /tmp/ansible/${PRODUCT}.yml --connection localhost
&& rm -rf /tmp/ansible  
  
# Standard JIRA-Port AJP  
EXPOSE ${PORTS}  
  
USER app  
  
  
# run license server  
CMD ["/opt/Altova/LicenseServer/bin/licenseserver","debug"]  

