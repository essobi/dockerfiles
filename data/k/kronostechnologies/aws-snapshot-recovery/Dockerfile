FROM python:3.6-alpine  
  
COPY . /aws-snapshot-recovery/  
RUN pip3 install -r /aws-snapshot-recovery/requirements  
  
ENTRYPOINT ["/aws-snapshot-recovery/bin/aws-snapshot-recovery"]  

