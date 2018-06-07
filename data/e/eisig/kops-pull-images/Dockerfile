# FROM debian:jessie  
FROM busybox  
COPY bootstrap_ecr.sh /opt/bootstrap_ecr.sh  
RUN chmod u+x /opt/bootstrap_ecr.sh  
  
ENTRYPOINT ["/bin/sh", "/opt/bootstrap_ecr.sh"]

