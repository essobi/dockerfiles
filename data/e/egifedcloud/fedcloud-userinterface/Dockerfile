# Dockerfile for building a EGI FedCloud userinterface  
FROM egifedcloud/fedcloud-coretools  
MAINTAINER Enol Fernandez <enol.fernandez@egi.eu>  
  
# gain privileges  
USER root  
  
# extra tools for docker image: myproxy, ssh client, vim and nano  
RUN apt-get -y install openssh-client vim-tiny nano  
  
# and get back to unprivileged user  
USER occi  
  
CMD /bin/bash  

