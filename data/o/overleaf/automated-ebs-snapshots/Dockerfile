FROM python:2  
  
RUN pip install automated-ebs-snapshots  
  
# The command seems to be OK with running as an unprivileged user.  
USER nobody  
  
ENTRYPOINT ["/usr/local/bin/automated-ebs-snapshots"]  

