#Data_Container#  
# Ubuntu Distribution and Version  
FROM ubuntu:14.04  
# Maintainer  
MAINTAINER Glenn Richardz "richgl1@student.op.ac.nz"  
#Index.html  
COPY index.html /var/www/html/index.html  
  
# Sets the Volume  
VOLUME [ "/var/www/html" ]  
  
# Entry Point  
ENTRYPOINT [ "/bin/sh", "-c", "while true; do echo This is a Data_Container;
sleep 60; done" ]  

