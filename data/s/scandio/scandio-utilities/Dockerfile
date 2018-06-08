FROM ubuntu:14.04  
MAINTAINER Scandio GmbH <info@scandio.de>  
  
RUN apt-get update && apt-get install -y \  
vim less rsync openssh-client mysql-client ldap-utils \  
&& apt-get clean \  
  
ENV RUN_USER root  
  
USER ${RUN_USER}  
  
WORKDIR /  
  
CMD ["/bin/bash"]  
  

