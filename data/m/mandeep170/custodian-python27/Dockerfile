FROM python:2.7-alpine  
  
RUN pip install c7n  
  
VOLUME ["/var/log/cloud-custodian", "/etc/cloud-custodian"]  
  
ENTRYPOINT ["/usr/local/bin/custodian"]  

