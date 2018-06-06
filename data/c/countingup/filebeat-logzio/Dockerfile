FROM docker.elastic.co/beats/filebeat:6.2.2  
# Add custom filebeat config  
COPY filebeat.yml /usr/share/filebeat/filebeat.yml  
  
USER root  
  
# Set permissions  
RUN chgrp filebeat /usr/share/filebeat/filebeat.yml  
  
# Get Logz.io CA cert  
RUN cd /usr/share/filebeat/ && curl -O
https://raw.githubusercontent.com/logzio/public-
certificates/master/COMODORSADomainValidationSecureServerCA.crt  
  
# Set permissions  
RUN chgrp filebeat
/usr/share/filebeat/COMODORSADomainValidationSecureServerCA.crt  
  
# Stay as root so we can read logs in /var/lib/docker/containers/*/*.log  

