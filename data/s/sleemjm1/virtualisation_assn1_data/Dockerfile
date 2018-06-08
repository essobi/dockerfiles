# version 1.0.0  
FROM ubuntu:14.04  
MAINTAINER Joe Sleeman "sleemjm1@student.op.ac.nz"  
RUN apt-get update  
  
COPY index.html /var/www/html/index.html  
  
VOLUME ["var/www/html"]  
  
ENTRYPOINT [ "/bin/sh", "-c", "while true; do echo data container; sleep 60;
done" ]  

