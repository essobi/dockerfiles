#
http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-
releases-via-apt-ubuntu  
FROM ubuntu:latest as builder  
  
LABEL Christian Sakshaug <christian@sakshaug.net>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install software-
properties-common vim git -y && apt-add-repository ppa:ansible/ansible -y &&
apt-get update && apt-get install ansible -y  
  
CMD [ "ansible" "--help" ]  

