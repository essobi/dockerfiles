FROM quin/ansiblecentos6  
MAINTAINER quin  
  
ADD ansible /srv/ansible  
WORKDIR /srv/ansible  
RUN ansible-playbook site.yml -c local  
  
#WORKDIR /  

