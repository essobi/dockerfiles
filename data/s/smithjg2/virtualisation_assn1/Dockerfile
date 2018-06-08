FROM ubuntu:14.04  
MAINTAINER Joshua Smith <smithjg2@student.op.ac.nz>  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
COPY index.html /var/www/html/index.html  
  
VOLUME [ "var/www/html" ]  
  
ENTRYPOINT [ "/bin/sh", "-c", "while true; do echo ready; sleep 60; done" ]

