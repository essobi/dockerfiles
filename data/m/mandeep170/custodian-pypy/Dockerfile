FROM pypy:2-5.1.0-slim  
  
RUN pip install c7n  
  
VOLUME ["/var/log/cloud-custodian", "/etc/cloud-custodian"]  
  
ENTRYPOINT ["/usr/local/bin/custodian"]  

