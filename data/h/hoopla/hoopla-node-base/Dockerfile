FROM evarga/jenkins-slave  
MAINTAINER Øystien Tandberg <oystein@hoopla.no>  
  
# General utils:  
RUN apt-get update && \  
apt-get -y install wget curl git  
  
RUN apt-get -y install nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN chmod u+w /etc/sudoers && \  
echo "%jenkins ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
chmod u-w /etc/sudoers && \  
visudo --check  

