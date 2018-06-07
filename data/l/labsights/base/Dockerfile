FROM ubuntu:16.04  
MAINTAINER Sorin Badea <sorin@labsights.com>  
  
#----------- upgrade distribution and install ansible ----------  
RUN apt-get update;apt-get install software-properties-common -y  
RUN apt-add-repository ppa:ansible/ansible  
RUN apt-get update -y; apt-get upgrade -y;apt-get dist-upgrade -y;  
RUN apt-get install ansible -y;  
  
  
#--------------- add the playbook and run it -------------------  
ADD bootstrap.yml /tmp/bootstrap.yml  
ADD templates /tmp/templates  
  
RUN ansible-playbook /tmp/bootstrap.yml  
  
#------------------------- cleanup -----------------------------  
RUN rm -rf /tmp/bootstrap.yml;rm -rf /tmp/templates;  
RUN apt-get autoremove -y;apt-get autoclean -y;apt-get clean -y;  

