FROM ansible/ubuntu14.04-ansible:stable  
MAINTAINER luisperlazaro@gmail.com  
  
COPY provisioning /tmp/provisioning  
  
WORKDIR /tmp/provisioning  
RUN ansible-playbook -c local alfresco_base.yml --tags "common"  
RUN ansible-playbook -c local alfresco_base.yml --tags "java"  
RUN ansible-playbook -c local alfresco_base.yml --tags "alfresco"  
  
WORKDIR /opt/alfresco  

